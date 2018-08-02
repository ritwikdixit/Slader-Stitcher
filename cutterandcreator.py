
from pyPdf import PdfFileWriter, PdfFileReader
output = PdfFileWriter()

#take the screenshots from images/9/ and crop them then push them all into one pdf
for i in range(1,147):
	#problem i
	input = PdfFileReader(file('images/10/prblm'+str(i)+'.pdf', 'rb'))
	page = input.getPage(0) #for the first page
	#crop nation to approximate the area where the problem is (hardcoded again)
	y1 = 570
	y2 = 740
	page.trimBox.lowerLeft = (0, y1)
	page.trimBox.upperRight = (600, y2)
	page.cropBox.lowerLeft = (0, y1)
	page.cropBox.upperRight = (600, y2)
	#add to new file
	output.addPage(page)

outputStream = file("apstatsch10.pdf", "wb")
output.write(outputStream)
outputStream.close()