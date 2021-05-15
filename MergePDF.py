from PyPDF2 import PdfFileMerger
import os
from pathlib import Path
import ocrmypdf
import sys
import subprocess

cwd = os.getcwd()
bashCommand = "ocrmypdf -c --force-ocr result.pdf output.pdf"

#MERGE A FOLDER OF PDF FILES AND CONVERT TO OCR

#ARGUMENT EXAMPLE
#search_dir = "/Users/developer/Documents/Udemy/Node-Course/Python/MergeFiles/"
search_dir = str(sys.argv[1])

def getfiles(dirpath):
    a = [s for s in os.listdir(dirpath)
         if os.path.isfile(os.path.join(dirpath, s))]
    a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
    return a

files = getfiles(search_dir)
pdfs = [file for file in files if '.pdf' in file]
merger = PdfFileMerger()

for pdf in pdfs:
  merger.append(search_dir+pdf)
  print(pdf)
merger.write("result.pdf")
merger.close()

process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()