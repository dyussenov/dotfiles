import platform
from tempfile import TemporaryDirectory
from pathlib import Path
 
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
 
if platform.system() == "Windows":
    # We may need to do some additional downloading and setup...
    # Windows needs a PyTesseract Download
    # https://github.com/UB-Mannheim/tesseract/wiki/Downloading-Tesseract-OCR-Engine
 
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )
 
    # Windows also needs poppler_exe
    path_to_poppler_exe = Path(r"C:\.....")
     
    # Put our output files in a sane place...
    out_directory = Path(r"~\Desktop").expanduser()
else:
    out_directory = Path("~").expanduser()    
 
# Path of the Input pdf
PDF_file = Path(r"File 01.pdf")
 
# Store all the pages of the PDF in a variable
image_file_list = []
 
text_file = out_directory / Path("out_text.txt")
 
def main():
    with TemporaryDirectory() as tempdir:
        if platform.system() == "Windows":
            pdf_pages = convert_from_path(
                PDF_file, 500, poppler_path=path_to_poppler_exe
            )
        else:
            pdf_pages = convert_from_path(PDF_file, 500)
        for page_enumeration, page in enumerate(pdf_pages, start=1):
            filename = f"{tempdir}\page_{page_enumeration:03}.jpg"
            page.save(filename, "JPEG")
            image_file_list.append(filename)
 

        with open(text_file, "a") as output_file:
            for image_file in image_file_list:
                text = str(((pytesseract.image_to_string(Image.open(image_file)))))
 
                text = text.replace("-\n", "")
                output_file.write(text)

if __name__ == "__main__":
    main()