import os
import pandas as pd
from fpdf import FPDF
import yagmail
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get email credentials from environment variables
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

# Create 'payslips' folder if it doesn't exist
if not os.path.exists("payslips"):
    os.makedirs("payslips")

# Public Google Sheets link (as Excel export)
google_sheet_url = "https://docs.google.com/spreadsheets/d/1jveUGJz9llySJD2fJpbW3nuMhJL60NOkg2fQC83l_AM/export?format=xlsx"

# Read the spreadsheet into a DataFrame
try:
    df = pd.read_excel(google_sheet_url)
except Exception as e:
    print("Failed to read the spreadsheet:", e)
    exit()

# Function to create a payslip PDF
def generate_payslip(employee):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Monthly Payslip", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(100, 10, txt=f"Employee ID: {employee['Employee ID']}", ln=True)
    pdf.cell(100, 10, txt=f"Name: {employee['Name']}", ln=True)
    pdf.cell(100, 10, txt=f"Basic Salary: ${employee['Basic Salary']:.2f}", ln=True)
    pdf.cell(100, 10, txt=f"Allowances: ${employee['Allowances']:.2f}", ln=True)
    pdf.cell(100, 10, txt=f"Deductions: ${employee['Deductions']:.2f}", ln=True)

    net_salary = employee['Basic Salary'] + employee['Allowances'] - employee['Deductions']
    pdf.cell(100, 10, txt=f"Net Salary: ${net_salary:.2f}", ln=True)

    filename = f"payslips/{employee['Employee ID']}.pdf"
    pdf.output(filename)
    return filename

# Function to send email with the payslip attached
def send_email(to_email, name, attachment_path):
    try:
        yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)
        subject = "Your Payslip for This Month"
        body = f"Hi {name},\n\nPlease find attached your payslip for this month.\n\nRegards,\nPayroll Team"
        yag.send(to=to_email, subject=subject, contents=body, attachments=attachment_path)
        print(f"✅ Email sent to {name} at {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email to {name} at {to_email}: {e}")

# Process each employee
for _, row in df.iterrows():
    try:
        payslip_path = generate_payslip(row)
        send_email(row['Email'], row['Name'], payslip_path)
    except Exception as e:
        print(f"⚠️ Error processing employee {row['Name']}: {e}")