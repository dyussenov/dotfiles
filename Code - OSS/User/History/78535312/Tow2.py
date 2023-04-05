import pytesseract
from pdf2image import convert_from_path
import PyPDF2
import io
from fpdf import FPDF
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'


img_object = Image.open(r"images_01\page_2.jpg")
img_text = pt.image_to_string(img_object)


print(img_text)



'''images = convert_from_path('File 01.pdf')
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_font("Arial", size=12)
for image in images:
    page = pytesseract.image_to_string(image)
    
    pdf.add_page()
    pdf.cell(200, 10, txt=page, ln=1, align="C")


pdf.output("simple_demo.pdf")'''