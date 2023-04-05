import pytesseract
from pdf2image import convert_from_path
import PyPDF2
import io

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

images = convert_from_path('File 01.pdf')
pdf_writer = PyPDF2.PdfFileWriter()
for image in images:
    page = pytesseract.image_to_string(image)
    pdf = PyPDF2.PdfFileReader(page)
    pdf_writer.addPage(pdf.getPage(0))# export the searchable PDF to searchable.pdf
    
with open("searchable.pdf", "wb") as f:
    pdf_writer.write(f)