from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader('res2 copy.pdf') 
writer = PdfWriter()

for page in reader.pages:
  page.cropbox.upper_left = (0,50)
  page.cropbox.lower_right = (595,770)
  writer.add_page(page) 
  
with open('result.pdf','wb') as fp:
    writer.write(fp) 