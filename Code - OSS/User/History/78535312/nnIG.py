import pytesseract
from pdf2image import convert_from_path
import PyPDF2
import io
from fpdf import FPDF
from PIL import Image
import os
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

images_names = os.listdir('images_01')
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.set_font("Arial", size=10)

img_object = Image.open(f"images_01/Page_9.jpg")
img_text = pytesseract.image_to_string(img_object)
print(img_text)
pdf.multi_cell(0, 5, img_text)
pdf.output("a1.pdf")
'''for image in images_names:
    img_object = Image.open(f"images_01/{image}")
    img_text = pytesseract.image_to_string(img_object)
    print(img_text)'''

