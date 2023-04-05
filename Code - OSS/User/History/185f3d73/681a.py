import cv2
import pytesseract
from pytesseract import Output
import pandas as pd

img = cv2.imread("images_01/Page_1.jpg", cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(img, (3, 3), 0)

custom_config = r' -l eng --oem 1 --psm 6  -c preserve_interword_spaces=1'
d = pytesseract.image_to_data(gauss, config=custom_config, output_type=Output.DICT)
df = pd.DataFrame(d)

# clean up blanks
df1 = df[(df.conf != '-1') & (df.text != ' ') & (df.text != '')]

# sort blocks vertically
sorted_blocks = df1.groupby('block_num').first().sort_values('top').index.tolist()
for block in sorted_blocks:
    curr = df1[df1['block_num'] == block]
    sel = curr[curr.text.str.len() > 3]
    char_w = (sel.width / sel.text.str.len()).mean()
    prev_par, prev_line, prev_left = 0, 0, 0
    text = ''
    for ix, ln in curr.iterrows():
        # add new line when necessary
        if prev_par != ln['par_num']:
            text += '\n'
            prev_par = ln['par_num']
            prev_line = ln['line_num']
            prev_left = 0
        elif prev_line != ln['line_num']:
            text += '\n'
            prev_line = ln['line_num']
            prev_left = 0

        added = 0  # num of spaces that should be added
        if ln['left'] / char_w > prev_left + 1:
            added = int((ln['left']) / char_w) - prev_left
            text += ' ' * added
        text += ln['text'] + ' '
        prev_left += len(ln['text']) + added + 1
    text += '\n'
    print(text)