import cv2
import pytesseract

img = cv2.imread('Page_1.jpg') # read an image

text = pytesseract.image_to_string(img) # extract text
print(text)

file = open('output_perferct.txt','a') # write to a file
file.write(text)
file.close()