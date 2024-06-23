// Extracts code from .c files and combines it into a single pdf
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_multiple_c_to_single_pdf(src_dir, output_pdf_name):
    pdf_file_path = os.path.join(src_dir, output_pdf_name)
    pdf = canvas.Canvas(pdf_file_path, pagesize=letter)
    
    content_font = "Helvetica"
    bold_font = "Helvetica-Bold"
    
    y = 750
    
    c_files = sorted([file for file in os.listdir(src_dir) if file.endswith('.c')])
    
    for file_name in c_files:
        c_file_path = os.path.join(src_dir, file_name)
        
        with open(c_file_path, 'r') as c_file:
            content = c_file.read()
        
        pdf.setFont(bold_font, 12)
        pdf.drawString(30, y, f"File: {file_name}")
        y -= 15
        
        pdf.setFont(content_font, 10)
        lines = content.split('\n')
        for line in lines:
            pdf.drawString(30, y, line)
            y -= 15
            if y < 40:
                pdf.showPage()
                y = 750
                pdf.setFont(bold_font, 12)
                pdf.drawString(30, y, f"File: {file_name}")
                y -= 15
                pdf.setFont(content_font, 10)
        y -= 30
    
    pdf.save()
    print(f"Converted all .c files in {src_dir} to {pdf_file_path}")

src_dir = os.getcwd()
output_pdf_name = 'combined_code.pdf'

convert_multiple_c_to_single_pdf(src_dir, output_pdf_name)
