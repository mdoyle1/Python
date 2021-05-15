#https://www.plainfieldct.org/calendar/CONCOMMIN/concommin032111.pdf

#Export Notes
#
#python exportNotes.py 03 29 1988 03 14 1989
#CHECK ALL DATES, IF 404 THEN DITCH URL IF 200 DOWNLOAD THE FILE...

import datetime
import sys
import requests
import urllib.request
from datetime import date

def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename, 'wb')
    file.write(response.read())
    file.close()
    
pdf_path = ""  

date = datetime.datetime(2021,1,1)
#INDEX # OF DAYS, IN THIS CASE 11 YEARS
for i in range(200): 
	date += datetime.timedelta(days=1)
	pdf_path = 'https://www.plainfieldct.org/calendar/CONCOMMIN/concommin{n}.pdf'.format(n=date.strftime('%m%d%y'))
	r = requests.get(pdf_path)
	r.status_code
	print(r.status_code)	
	if r.status_code == 200:
  	  print (i+'OK!')
  	  download_file(pdf_path, 'concommin{n}.pdf'.format(n=date.strftime('%m%d%y')))
	else:
	    print (i+'Boo!')




