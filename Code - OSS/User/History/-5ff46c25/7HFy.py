from PyPDF2 import PdfWriter, PdfReader, PdfMerger

reader = PdfReader("res1.pdf")
page = reader.pages[0]
print(page.cropbox.lower_left)
print(page.cropbox.lower_right)
print(page.cropbox.upper_left)
print(page.cropbox.upper_right)
