import pytesseract
from pdf2image import convert_from_path
import PyPDF2
import io

poppler_path = r'/usr/include/poppler'
pytesseract.pytesseract.tesseract_cmd = r'/usr/include/popplere'

images = convert_from_path('File 01.pdf', poppler_path=poppler_path)
pdf_writer = PyPDF2.PdfFileWriter()
for image in images:
    page = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
    pdf = PyPDF2.PdfFileReader(io.BytesIO(page))
    pdf_writer.addPage(pdf.getPage(0))# export the searchable PDF to searchable.pdf
with open("searchable.pdf", "wb") as f:
    pdf_writer.write(f)