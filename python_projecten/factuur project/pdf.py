from fpdf import FPDF
from datetime import datetime
import json

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
        # Extract data from the order
        ordernummer = order['order']['ordernummer']
        orderdatum = order['order']['orderdatum']
        klant = order['order']['klant']
        betaaltermijn = order['order']['betaaltermijn']
        producten = order['order']['producten']

        # Maak de factuur aan
        self.set_font("Arial", "", 10)

        # Voeg datum toe
        self.set_font("Arial", "", 13)
        datum = datetime.now().strftime("%d-%m-%Y")
        self.cell(0, 5, f"Datum: {datum}", ln=True)
        self.set_font("Arial", "", 10)

        # Voeg lege regel toe
        self.ln(5)

        self.multi_cell(0, 5, f"Factuurnummer: {ordernummer}", align="L")

        self.ln(5)

        # Add customer information
        for key, value in klant.items():
            self.cell(130, 5, f"{key}: {value}", ln=True)

        # Voeg lege regel toe
        self.ln(5)

        # Voeg gekleurde lijn toe om de gegevens en de totaal te scheiden
        self.set_fill_color(90, 90, 255)  # Grijze kleur instellen
        self.cell(0, 3, "", 0, 1, "C", 1)  # Lijn tekenen met dezelfde breedte als de pagina

        self.ln(5)

        # Voeg producten toe
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
            self.cell(30, 5, "", border=0)  # Lege cel toevoegen voor extra ruimte
            self.cell(50, 5, f"{product_prijs:.2f} EUR", border=0)
            self.ln()
            totaal_prijs_excl_btw += product_prijs

        self.ln(5)

        # Voeg gekleurde lijn toe om de gegevens en de totaal te scheiden
        self.set_fill_color(90, 90, 255)  # Grijze kleur instellen
        self.cell(0, 3, "", 0, 1, "C", 1)  # Lijn tekenen met dezelfde breedte als de pagina

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

         # Voeg tekst toe over betalingstermijn
        self.ln(30)  # Voeg een lege regel toe voor ruimte
        self.set_font("Arial", "B", 13)
        self.multi_cell(0, 5, f"Gelieve deze factuur binnen {betaaltermijn} na factuurdatum te betalen.", align="C")


# Read the JSON file for invoice data
with open('order_data.json') as f:
    order_data = json.load(f)

# Maak een instantie van de Factuur-klasse
factuur = Factuur()
factuur.add_page()
factuur.set_margins(8, 8, 8)  # Marges instellen

# Voeg de factuurinhoud toe met de gelezen gegevens uit de JSON
factuur.factuur_body(order_data)

# Sla de factuur op
factuur.output("factuur.pdf")

