from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader('res1 copy.pdf') 
writer = PdfWriter()

for page in reader.pages:
  page.cropbox.upper_left = (100,300)
  page.cropbox.lower_right = (595,300)
  writer.add_page(page) 
  
with open('result.pdf','wb') as fp:
    writer.write(fp) 