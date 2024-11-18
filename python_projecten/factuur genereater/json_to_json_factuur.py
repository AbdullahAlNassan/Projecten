import os
import json
import shutil
from fpdf import FPDF
from datetime import datetime

# Define directories
json_in_dir = "JSON_IN"
json_processed_dir = "JSON_PROCESSED"
invoice_dir = "INVOICE"

# Create directories if they don't exist
for directory in [json_in_dir, json_processed_dir, invoice_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

class Factuur(FPDF):
    def header(self):
        self.set_font("Arial", "B", 20)
        self.set_text_color(90, 90, 255)
        self.cell(80, 10, "Factuur", 0, 0, "L")

        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Factuur", 0, 0, "R")
        self.image("logo.png", 170, 10, 30)
        self.set_text_color(0, 0, 0)
        self.ln(30)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Pagina {self.page_no()}")

    def factuur_body(self, order):
        ordernummer = order['order']['ordernummer']
        orderdatum = order['order']['orderdatum']
        klant = order['order']['klant']
        betaaltermijn = order['order']['betaaltermijn']
        producten = order['order']['producten']

        self.set_font("Arial", "", 10)

        self.set_font("Arial", "", 13)
        datum = datetime.now().strftime("%d-%m-%Y")
        self.cell(0, 5, f"Datum: {datum}", ln=True)
        self.set_font("Arial", "", 10)

        self.ln(5)

        self.multi_cell(0, 5, f"Factuurnummer: {ordernummer}", align="L")

        self.ln(5)

        for key, value in klant.items():
            self.cell(130, 5, f"{key}: {value}", ln=True)

        self.ln(5)

        self.set_fill_color(90, 90, 255)
        self.cell(0, 3, "", 0, 1, "C", 1)

        self.ln(5)

        self.set_text_color(90, 90, 255)
        self.cell(100, 5, "Product", border=0)
        self.cell(20, 5, "Aantal", border=0)
        self.cell(30, 5, "", border=0)
        self.cell(20, 5, "Prijs", border=0)
        self.set_text_color(0, 0, 0)
        self.ln(10)
        totaal_prijs_excl_btw = 0
        for product in producten:
            product_naam = product['productnaam']
            aantal = product['aantal']
            prijs_excl_btw = product['prijs_per_stuk_excl_btw']
            btw_percentage = product['btw_percentage']
            product_prijs = prijs_excl_btw * (1 + (btw_percentage / 100))
            self.cell(100, 5, product_naam, border=0)
            self.cell(20, 5, str(aantal), border=0)
            self.cell(30, 5, "", border=0)
            self.cell(50, 5, f"{product_prijs:.2f} EUR", border=0)
            self.ln()
            totaal_prijs_excl_btw += product_prijs

        self.ln(5)

        self.set_fill_color(90, 90, 255)
        self.cell(0, 3, "", 0, 1, "C", 1)

        self.ln(5)

        self.ln(5)
        self.set_x(110)
        self.cell(50, 5, "Totaal excl. BTW:", 0, 0, "")
        self.cell(0, 5, f"{totaal_prijs_excl_btw:.2f} EUR")
        self.ln()
        self.set_x(110)
        self.cell(50, 5, "BTW (21%):", 0, 0, "")
        self.cell(0, 5, f"{(totaal_prijs_excl_btw * 0.21):.2f} EUR")
        self.ln()
        self.set_x(110)
        self.cell(50, 5, "Totaal incl. BTW:", 0, 0, "")
        self.cell(0, 5, f"{(totaal_prijs_excl_btw * 1.21):.2f} EUR")

        self.ln(30)
        self.set_font("Arial", "B", 13)
        self.multi_cell(0, 5, f"Gelieve deze factuur binnen {betaaltermijn} na factuurdatum te betalen.", align="C")

# Read the JSON file for invoice data
def generate_invoice(json_file):
    with open(json_file) as f:
        order_data = json.load(f)

    # Maak een instantie van de Factuur-klasse
    factuur = Factuur()
    factuur.add_page()
    factuur.set_margins(8, 8, 8)  # Marges instellen

    # Voeg de factuurinhoud toe met de gelezen gegevens uit de JSON
    factuur.factuur_body(order_data)

    # Sla de factuur op als PDF
    invoice_pdf_path = os.path.join(invoice_dir, os.path.splitext(os.path.basename(json_file))[0] + ".pdf")
    factuur.output(invoice_pdf_path)

    # Maak een JSON-bestand met dezelfde gegevens als de factuur
    invoice_json = {
        "ordernummer": order_data['order']['ordernummer'],
        "orderdatum": order_data['order']['orderdatum'],
        "klant": order_data['order']['klant'],
        "betaaltermijn": order_data['order']['betaaltermijn'],
        "producten": order_data['order']['producten']
    }
    invoice_json_path = os.path.join(invoice_dir, os.path.splitext(os.path.basename(json_file))[0] + ".json")
    with open(invoice_json_path, "w") as json_out:
        json.dump(invoice_json, json_out)

    # Verplaats de verwerkte JSON-bestanden naar de map 'JSON_PROCESSED'
    shutil.move(json_file, os.path.join(json_processed_dir, os.path.basename(json_file)))

# Loop through JSON_IN directory and generate invoices
for json_file in os.listdir(json_in_dir):
    if json_file.endswith(".json"):
        json_path = os.path.join(json_in_dir, json_file)
        generate_invoice(json_path)
