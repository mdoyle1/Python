#https://www.lisbonct.com/node/18/minutes/2010
#GRAB ALL URLS FROM DIV ID MAIN

import urllib3
import urllib.request
import requests
from bs4 import BeautifulSoup
#urllib3.disable_warnings()

year=2010
links = []
pdf_path = ""  

def getFiles(year):
	url="https://www.lisbonct.com/node/18/minutes/"+str(year)
	r = requests.get(url)
	http = urllib3.PoolManager()
	response = http.request('GET', url)
	soup = BeautifulSoup(response.data.decode('utf-8'))
	for h3 in soup.findAll('h3'):
		    for link in h3.findAll('a'):
		   	 links.append('https://www.lisbonct.com'+link.get('href'))
		   	 pdf_path = 'https://www.lisbonct.com'+link.get('href')
		   	 print(pdf_path)
		   	 r = requests.get(pdf_path)
		   	 r.status_code
		   	 print(r.status_code)
		   	 if r.status_code == 200:
  	  				print ('OK!')
  	  				response = http.request('GET', pdf_path)
  	  				file = open(pdf_path.rsplit('/', 1)[-1]+'.pdf', 'wb')
  	  				file.write(r.content)
    					file.close()
  	  		#		download_file(pdf_path, pdf_path.rsplit('/', 1)[-1]+'.pdf')
  	  						
  	  	
for x in range(2010,2021):
	getFiles(year)
	year+=1
	print(year) 				
	   	   
def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename, 'wb')
    file.write(response.read())
    file.close()
    	   
	
print(len(links))	

	

	
