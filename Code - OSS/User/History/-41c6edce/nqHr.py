from pdf2image import convert_from_path


def split_pdf_to_images(pdf_path):
    pages = convert_from_path(pdf_path, 350)

    i = 1
    for page in pages:
        image_name = "Page_" + str(i) + ".jpg"  
        page.save(image_name, "JPEG")
        i = i+1