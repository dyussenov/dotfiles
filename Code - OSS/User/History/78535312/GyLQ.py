import pytesseract
from pdf2image import convert_from_path
import PyPDF2
import io
from fpdf import FPDF
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'


'''img_object = Image.open(r"images_01/Page_4.jpg")
img_text = pytesseract.image_to_string(img_object)


print(img_text)'''

print(os.getcwd())