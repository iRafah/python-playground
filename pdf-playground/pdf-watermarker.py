import PyPDF2

template = PyPDF2.PdfFileReader(open('combined.pdf', 'rb'))
watermaker = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

# Loop through the pages and merge the watermarker.
for i in range(template.getNumPages()):
    page = template.getPage(i)
    # @see https://pypdf2.readthedocs.io/en/latest/modules/PageObject.html#PyPDF2._page.PageObject.mergePage
    page.mergePage(watermaker.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
