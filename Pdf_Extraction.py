# USING PyPDF2

import PyPDF2
import numpy

page_number = 3
pdf_file = open('result.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(page_number)
page_content = page.extractText()
print (page_content.encode('utf-8'))


table_list = page_content.split('\n')
l = numpy.array_split(table_list, len(table_list)/10)
for i in range(0,11):
   print(l[i])


# USING TABULA

import tabula

# Read pdf into DataFrame
df = tabula.read_pdf("result.pdf", encoding = 'latin1', pages = 'all', area = [29.75,43.509,819.613,464.472], nospreadsheet = True)
df.to_csv("result.csv", index = False)

# Read remote pdf into DataFrame
df2 = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")

# convert PDF into CSV
tabula.convert_into("result.pdf", "output.csv" ,pages = 'all', output_format="csv" )

