import pytesseract
from pdf2image import convert_from_path
import PyPDF2
import io
from docx import Document
from PIL import Image
import os
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

images_names = os.listdir('images_01')
# create document object
document = Document()



for image in images_names:
    img_object = Image.open(f"images_01/{image}")
    img_text = pytesseract.image_to_string(img_object)
    document.add_paragraph(img_text)
document.save('demo.docx')