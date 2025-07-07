from fpdf import FPDF
import os

def create_invoice_pdf(client_name, address, estimate_no, issue_date, valid_until, items):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "ESTIMATE", ln=True, align="R")
    pdf.ln(10)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 5, "SecureNet\n5621 MacCorkle Avenue SW\nSuite A\nSouth Charleston WV 25303\nUnited States\n\nHarrison Korodi\n3047444034\n3047411335\nhkorodi@wvsupport.net")
    pdf.ln(5)

    pdf.multi_cell(0, 5, f"FOR\n{client_name}\n{address}\n\nEstimate No.: {estimate_no}\nIssue date: {issue_date}\nValid until: {valid_until}")
    pdf.ln(5)

    # Table header
    pdf.set_font("Arial", "B", 12)
    pdf.cell(80, 10, "DESCRIPTION", 1)
    pdf.cell(20, 10, "QTY", 1)
    pdf.cell(30, 10, "UNIT PRICE", 1)
    pdf.cell(20, 10, "DISC %", 1)
    pdf.cell(30, 10, "AMOUNT", 1)
    pdf.ln()

    total = 0
    pdf.set_font("Arial", "", 12)
    for desc, qty, price in items:
        amount = qty * price
        total += amount
        pdf.cell(80, 10, desc[:40], 1)
        pdf.cell(20, 10, str(qty), 1)
        pdf.cell(30, 10, f"{price:.2f}", 1)
        pdf.cell(20, 10, "0.00", 1)
        pdf.cell(30, 10, f"{amount:.2f}", 1)
        pdf.ln()

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(150, 10, "TOTAL (USD):", 0, 0, 'R')
    pdf.cell(30, 10, f"${total:.2f}", 0, 1, 'R')

    filename = f"output/invoice_{estimate_no}.pdf"
    os.makedirs("output", exist_ok=True)
    pdf.output(filename)
    return filename
