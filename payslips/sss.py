import os
import pandas as pd
from fpdf import FPDF
import yagmail
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(dotenv_path='marques.env')  # Adjust path if necessary

# Email credentials from environment variables
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

# Create folder for payslips if it doesn't exist
if not os.path.exists("payslips"):
    os.makedirs("payslips")

# Read employee data from Excel file
df = pd.read_excel("C:/Users/uncommonstudent/Desktop/covenant/employees.xlsx")

# Function to create a payslip PDF
def generate_payslip(employee):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add title
    pdf.cell(200, 10, txt="Monthly Payslip", ln=True, align="C")
    pdf.ln(10)

    # Add employee details
    pdf.cell(100, 10, txt=f"Employee ID: {employee['Employee ID']}", ln=True)
    pdf.cell(100, 10, txt=f"Name: {employee['Name']}", ln=True)
    pdf.cell(100, 10, txt=f"Basic Salary: ${employee['Basic Salary']:.2f}", ln=True)
    pdf.cell(100, 10, txt=f"Allowances: ${employee['Allowances']:.2f}", ln=True)
    pdf.cell(100, 10, txt=f"Deductions: ${employee['Deductions']:.2f}", ln=True)

    # Calculate net salary
    net_salary = employee['Basic Salary'] + employee['Allowances'] - employee['Deductions']
    pdf.cell(100, 10, txt=f"Net Salary: ${net_salary:.2f}", ln=True)

    # Save the payslip as a PDF file
    filename = f"payslips/{employee['Employee ID']}.pdf"
    pdf.output(filename)
    return filename

# Function to send email with payslip attachment
def send_email(to_email, name, attachment_path):
    try:
        # Explicitly disable keyring storage and use email credentials directly
        yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)  # No need for keyring or .yagmail folder
        subject = "Your Payslip for This Month"
        body = f"Hi {name},\n\nPlease find attached your payslip for this month.\n\nBest regards,\nPayroll Team"
        yag.send(to=to_email, subject=subject, contents=body, attachments=attachment_path)
        print(f"Email sent to {name} at {to_email}")
    except Exception as e:
        print(f"Failed to send email to {name} at {to_email}: {e}")

# Process each employee
for _, row in df.iterrows():
    try:
        # Generate the payslip PDF
        payslip_path = generate_payslip(row)
        # Send the payslip to the employee via email
        send_email(row['Email'], row['Name'], payslip_path)
    except Exception as e:
        print(f"Error processing employee {row['Name']}: {e}")
