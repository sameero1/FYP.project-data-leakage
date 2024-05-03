from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
import os

def create_pdf(input_file, output_file):
    # Define styles
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    body_style = styles["BodyText"]

    # Create a new PDF document
    pdf = SimpleDocTemplate(output_file, pagesize=letter)

    # Content elements to be added to the PDF
    content = []

    # Add title
    title_text = "Audit Trail Report"
    content.append(Paragraph(title_text, title_style))

    # Add lines from the input file
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # Skip empty lines
                # Handle long lines
                while len(line) > 80:
                    content.append(Paragraph(line[:80], body_style))
                    line = line[80:]
                content.append(Paragraph(line, body_style))

    # Add content to the PDF
    pdf.build(content)

if __name__ == "__main__":
    input_file = "./audit_trail.log"
    output_file = "./example.pdf"

    # Check if input file exists
    if not os.path.exists(input_file):
        print("Input file not found.")
    else:
        create_pdf(input_file, output_file)
        print("PDF created successfully.")
