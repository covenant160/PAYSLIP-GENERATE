import pandas as pd
from fpdf import FPDF
import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

url = "https://docs.google.com/spreadsheets/d/1jveUGJz9llySJD2fJpbW3nuMhJL60NOkg2fQC83l_AM/export?format=csv"

try:
    df = pd.read_csv(url)
except Exception as e:
    print("Error loading Google Sheet:", e)
    exit()

df["Net Salary"] = df["Basic Salary"] + df["Allowances"] - df["Deductions"]

os.makedirs("payslips", exist_ok=True)

def create_payslip(row):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Payslip", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Employee ID: {row['Employee ID']}", ln=True)
    pdf.cell(200, 10, txt=f"Name: {row['Name']}", ln=True)
    pdf.cell(200, 10, txt=f"Basic Salary: ${row['Basic Salary']}", ln=True)
    pdf.cell(200, 10, txt=f"Allowances: ${row['Allowances']}", ln=True)
    pdf.cell(200, 10, txt=f"Deductions: ${row['Deductions']}", ln=True)
    pdf.cell(200, 10, txt=f"Net Salary: ${row['Net Salary']}", ln=True)

    filename = f"payslips/{row['Employee ID']}.pdf"
    pdf.output(filename)
    return filename

try:
    yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASS)
except Exception as e:
    print("Email login failed:", e)
    exit()

for index, row in df.iterrows():
    try:
        pdf_path = create_payslip(row)
        subject = "Your Payslip for This Month"
        body = f"Hi {row['Name']},\n\nAttached is your payslip for this month.\n\nBest regards,\nHR Department"
        yag.send(to=row["Email"], subject=subject, contents=body, attachments=pdf_path)
        print(f"✅ Sent payslip to {row['Name']} at {row['Email']}")
    except Exception as e:
        print(f"❌ Error sending to {row['Name']}: {e}")


