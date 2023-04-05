import os
from pikepdf import Pdf

filename = "PDF32000_2008.pdf"
pdf = Pdf.open(filename)


file2pages = {
    0: [5, 25], # 1st splitted PDF file will contain the pages from 0 to 9 (9 is not included)
}

new_pdf_files = [ Pdf.new() for i in file2pages ]
# the current pdf file index
new_pdf_index = 0


name, ext = os.path.splitext(filename)
output_filename = f"{name}-{new_pdf_index}.pdf"
new_pdf_files[new_pdf_index].save(output_filename)
print(f"[+] File: {output_filename} saved.")