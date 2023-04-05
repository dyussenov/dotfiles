import pytesseract
from pdf2image import convert_from_path
import PyPDF2
import io
from fpdf import FPDF

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

images = convert_from_path('File 01.pdf')
pdf = FPDF()
pdf.set_font("Arial", size=12)
for image in images:
    page = pytesseract.image_to_string(image)
    
    pdf.add_page()
    pdf.cell(200, 10, txt=page, ln=1, align="C")


pdf.output("simple_demo.pdf")