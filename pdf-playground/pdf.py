import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):

    merger = PyPDF2.PdfFileMerger()

    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('combined.pdf')


pdf_combiner(inputs)


# with open('dummy.pdf', 'rb') as file:
#    reader = PyPDF2.PdfFileReader(file)
#    page = reader.getPage(0)
#    page.rotateCounterClockwise(90)

#    writer = PyPDF2.PdfFileWriter()
#    writer.addPage(page)
#    with open('tilt.pdf', 'wb') as new_file:
#        writer.write(new_file)
