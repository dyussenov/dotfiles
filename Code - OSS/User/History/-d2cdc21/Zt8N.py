from PyPDF2 import PdfFileReader, PdfFileMerger

if __name__ == '__main__':
    file_in = open('final_res3.pdf', 'rb')
    pdf_reader = PdfFileReader(file_in)
    metadata = pdf_reader.getDocumentInfo()
    print(metadata)

    pdf_merger = PdfFileMerger()
    pdf_merger.append(file_in)
    pdf_merger.addMetadata({
        '/Author': 'a',
        '/Title': 'part 3',
        '/Producer': 'a'
    })
    file_out = open('new.pdf', 'wb')
    pdf_merger.write(file_out)

    file_in.close()
    file_out.close()