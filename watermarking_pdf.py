import PyPDF2
import sys

template = PyPDF2.PdfFileReader(open(f'{sys.argv[1]}','rb'))
watermark = PyPDF2.PdfFileReader(open(f'{sys.argv[2]}','rb'))
output_pdf = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output_pdf.addPage(page)

with open(f'{sys.argv[1]}_wm.pdf','wb') as file :
    output_pdf.write(file)
