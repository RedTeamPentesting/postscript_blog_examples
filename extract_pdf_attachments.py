#!/usr/bin/python3
# very slightly modified version of https://gist.github.com/kevinl95/29a9e18d474eb6e23372074deff2df38 with cmd arguments and by default no output
import PyPDF2
import sys
from pathlib import Path


def getAttachments(reader):
    """
    Retrieves the file attachments of the PDF as a dictionary of file names
    and the file data as a bytestring.
     :return: dictionary of filenames and bytestrings
    """
    catalog = reader.trailer["/Root"]
    fileNames = catalog["/Names"]["/EmbeddedFiles"]["/Kids"][0].getObject()["/Names"]
    attachments = {}
    for f in fileNames:
        if isinstance(f, str):
            name = f
            dataIndex = fileNames.index(f) + 1
            fDict = fileNames[dataIndex].getObject()
            fData = fDict["/EF"]["/F"].getData()
            attachments[name] = fData
    return attachments


handler = open(sys.argv[1], "rb")
reader = PyPDF2.PdfFileReader(handler)
dictionary = getAttachments(reader)

# print(dictionary)
for fName, fData in dictionary.items():
    path = Path.cwd() / ("." + str(Path(fName).resolve()))
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as outfile:
        outfile.write(fData)
