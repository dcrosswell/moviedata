import requests
from bs4 import BeautifulSoup
import csv
import re

#Make request to boxofficemojo
def request():
	#url = 'http://www.boxofficemojo.com/alltime/domestic.htm'
	url = 'http://www.boxofficemojo.com/alltime/domestic.htm?page=5&p=.htm'
	response = requests.get(url)

	html = response.content
	soup = BeautifulSoup(html, "html.parser")
	#print(soup.get_text())

	data = soup.find('div', attrs={'id': 'body'}) 
	return data

#Scrape relevant data
def scrape():
	data = request()
	for s in data('p'):
		s.extract()
	text = re.split("\n\n", data.get_text())

	#print(text[5])

	out = open('./output.csv', 'w')
	writer = csv.writer(out)
	for row in text:
		new_row = re.split("\n", row)
		writer.writerow(new_row)

def mov_info():
	data = request()
	#id = ""
	#url = "/movies/?id=" + id + ".htm"

	for row in data.findAll('table')[5].findAll('tr')[1:]:
		mov = row.findAll('td')
		for link in mov[1].findAll('a', href=True):
			#print(link['href'])
			regex = re.match('.*id=([-a-zA-Z0-9]+)[.]', link['href'])
			# url = "http://www.boxofficemojo.com/movies/?id=" + regex.group(1) + ".htm"
			print(regex.group(1))
			# resp = requests.get(url)
			# html = resp.content
			# soup = BeautifulSoup(html, "html.parser")
			# data = soup.find('div', attrs={'id': 'body'})
			# print(data)
			# #tab = data.findAll('table')
			# #print(tab)


#scrape()
mov_info()