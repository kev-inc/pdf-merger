import os, PyPDF2, sys

#Ask user where the PDFs are
# userpdflocation=input('Folder path to PDFs that need merging:')

#Sets the scripts working directory to the location of the PDFs
# os.chdir(userpdflocation)

#Ask user for the name to save the file as
userfilename=input('What should I call the file?')

#Set Print Interval
printinterval=int(input('How many pages in a page?'))

#Get all the PDF filenames
pdf2merge = sys.argv[1:]
# for filename in os.listdir('.'):
#     if filename.endswith('.pdf'):
#         pdf2merge.append(filename)

pdfWriter = PyPDF2.PdfFileWriter()

#loop through all PDFs
pagecount = 0
for filename in pdf2merge:
    #rb for read binary
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    while pagecount % printinterval != 0:
        pdfWriter.addBlankPage()
        pagecount += 1
    #Opening each page of the PDF
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
        pagecount += 1

#save PDF to file, wb for write binary
pdfOutput = open(userfilename+'.pdf', 'wb')
#Outputting the PDF
pdfWriter.write(pdfOutput)
#Closing the PDF writer
pdfOutput.close()