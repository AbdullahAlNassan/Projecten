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

# Functie om PDF te genereren van JSON
def generate_pdf_from_json(json_file):
    # Read JSON file
    with open(json_file) as f:
        order_data = json.load(f)

    # Generate PDF file name based on JSON file name
    pdf_file_name = os.path.splitext(os.path.basename(json_file))[0] + ".pdf"
    pdf_file_path = os.path.join(invoice_dir, pdf_file_name)

    # Create an instance of the Factuur class
    factuur = Factuur()
    factuur.add_page()
    factuur.set_margins(8, 8, 8)  # Set margins

    # Add invoice content using the read data from JSON
    factuur.factuur_body(order_data)

    # Save the invoice
    factuur.output(pdf_file_path)

    return pdf_file_path

# Functie om JSON-bestand naar verwerkte map te verplaatsen
def move_json_to_processed(json_file):
    # Construct the destination path
    destination = os.path.join(json_processed_dir, os.path.basename(json_file))
    # Move the JSON file
    shutil.move(json_file, destination)

# Iterate over the JSON files in the JSON_IN directory
for root, _, files in os.walk(json_in_dir):
    for file in files:
        if file.endswith(".json"):
            json_file_path = os.path.join(root, file)
            # Vraag om de naam van het JSON-bestand
            json_file_name = input(f"Enter the name for JSON file '{file}': ")
            # Genereer PDF van JSON en krijg het PDF-bestandpad
            pdf_file_path = generate_pdf_from_json(json_file_path)
            # Verplaats het JSON-bestand naar de verwerkte map
            move_json_to_processed(json_file_path)
            print(f"Generated PDF: {pdf_file_path}")



