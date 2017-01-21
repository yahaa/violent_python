import pyPdf
from pyPdf import PdfFileReader


def printMeta(fileName):
    pdfFile = PdfFileReader(file(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print '[*] PDF MetaData For : ' + str(fileName)
    for meatItem in docInfo:
        print '[+] ' + meatItem + ':' + docInfo[meatItem]

fileName = 'ANONOPS_The_Press_Release.pdf'
printMeta(fileName)
