from pyPdf import PdfFileWriter, PdfFileReader

with open("PDF32000_2008-0.pdf", "rb") as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter()

    numPages = input1.getNumPages()
    print ("document has %s pages." % numPages)

    for i in range(numPages):
        page = input1.getPage(i)
        print (page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        page.trimBox.lowerLeft = (25, 25)
        page.trimBox.upperRight = (225, 225)
        page.cropBox.lowerLeft = (50, 50)
        page.cropBox.upperRight = (200, 200)
        output.addPage(page)

    with open("out.pdf", "wb") as out_f:
        output.write(out_f)