from PyPDF2 import PdfWriter, PdfReader, PdfMerger

reader = PdfReader("res1.pdf")
page = reader.pages[0]
print(page.cropbox.lower_left)
print(page.cropbox.lower_right)
print(page.cropbox.upper_left)
print(page.cropbox.upper_right)
page.mediabox.lower_right = (lower_right_new_x_coordinate, lower_right_new_y_coordinate)
page.mediabox.lower_left = (lower_left_new_x_coordinate, lower_left_new_y_coordinate)
page.mediabox.upper_right = (upper_right_new_x_coordinate, upper_right_new_y_coordinate)
page.mediabox.upper_left = (upper_left_new_x_coordinate, upper_left_new_y_coordinate)