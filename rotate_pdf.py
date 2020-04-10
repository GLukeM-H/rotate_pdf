import PyPDF2


pdf_path = input("Enter G:\\path\\to\\pdf file.pdf\n")

try:
	pdf_in = open(pdf_path, 'rb')
except FileNotFoundError as e:
	input("File not found. Press <enter> to close.")
	exit()

try:
	reader = PyPDF2.PdfFileReader(pdf_in)
except PyPDF2.utils.PdfReadError as e:
	input("Could not read file. Press <enter> to close.")
	exit()


ranges = input("List or range of pages to rotate (e.g. 3 4 5 or 3-5)\n")
ranges = ' - '.join(ranges.split('-')).split()

writer = PyPDF2.PdfFileWriter()
writer.appendPagesFromReader(reader)

try:
	for i in range(len(ranges)):
		if ranges[i] == '-':
			for j in range(int(ranges[i-1])+1,int(ranges[i+1])):
				page = writer.getPage(j-1)
				page.rotateClockwise(90)
		else:
			page = writer.getPage(int(ranges[i])-1)
			page.rotateClockwise(90)
except (IndexError, ValueError) as e:
	input("Pages out of range or could not parse page ranges. Press <enter> to close.")
	exit()

pdf_out = open(pdf_path[:-4]+' - rotated.pdf', 'wb')
writer.write(pdf_out)
pdf_out.close()
pdf_in.close()

input("A new pdf has been created:\n{} - rotated.pdf\n".format(pdf_path[:-4]))
