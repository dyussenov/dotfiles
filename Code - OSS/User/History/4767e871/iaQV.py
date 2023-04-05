import pytesseract
from pdf2image import convert_from_path
import PyPDF2
import io
import aspose.words as aw
from PIL import Image
import os
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

images_names = os.listdir('images_01')
# create document object
doc = aw.Document()

# create a document builder object
builder = aw.DocumentBuilder(doc)

for image in images_names:
    img_object = Image.open(f"images_01/{image}")
    img_text = pytesseract.image_to_string(img_object)
    builder.write(img_text)

doc.save("out.docx")