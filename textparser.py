import requests  
from lxml import html  
import sys  
import urlparse
import os
from bs4 import BeautifulSoup

# Add your range for SEC company filings
for i in range(1193001, 1194500):

	# strl ="http://www.sec.gov/Archives/edgar/data/1194251/"
	strl ="http://www.sec.gov/Archives/edgar/data/" + str(i) + "/"
	response = requests.get(strl) ## website name

	# Check for company status error
	if (response.status_code == 404):
		continue

	soup = BeautifulSoup(response.text)

	list_a = soup.find_all('a')
	for elem in list_a:
		if(elem.get('href')[-4:]==".txt"):
			article_name = elem.get('href')
			break

	# article_name = (soup.find_all('a'))[6].get('href')
	article_strl = strl+article_name
	print(article_strl)
	article_response = requests.get(article_strl) ## website name

	article_string = str(article_response.text)

	company_info = ""

	article_list = article_string.split("\n")

	company_name_index = article_list.index('\tCOMPANY DATA:\t')


	company_name_crap = article_list[company_name_index+1]
	company_name_crap_strip =  company_name_crap.strip('\t')

	print(company_name_crap_strip)
	company_name = company_name_crap_strip[26:]
	print(company_name)
	company_info = company_info + company_name + ";"
	###########################################################
	# Insert comany name in a file
	###########################################################

	article_list = article_list[article_list.index('\tCOMPANY DATA:\t') - 1 :]
	print (article_list)

	company_address_index = article_list.index('\tBUSINESS ADDRESS:\t')

	company_street1_name_crap = article_list[company_address_index+1]
	company_street1_name_crap_strip = company_street1_name_crap.strip('\t')
	print(company_street1_name_crap_strip)
	if(company_street1_name_crap_strip[:9] == "STREET 1:"):
		company_street1_name = company_street1_name_crap_strip[11:]
		print(company_street1_name)
		company_info += company_street1_name + ","

	company_street1_name_crap = article_list[company_address_index+2]
	company_street1_name_crap_strip = company_street1_name_crap.strip('\t')
	if(company_street1_name_crap_strip[:9] == "STREET 2:"):
		company_street1_name = company_street1_name_crap_strip[11:]
		print(company_street1_name)
		company_info += company_street1_name + ","

		company_street1_name_crap = article_list[company_address_index+3]
		company_street1_name_crap_strip = company_street1_name_crap.strip('\t')
		company_street1_name = company_street1_name_crap_strip[8:]
		print(company_street1_name)
		company_info += company_street1_name + ","

		company_street1_name_crap = article_list[company_address_index+4]
		company_street1_name_crap_strip = company_street1_name_crap.strip('\t')
		company_street1_name = company_street1_name_crap_strip[9:]
		print(company_street1_name)
		company_info += company_street1_name + ","

		company_street1_name_crap = article_list[company_address_index+5]
		company_street1_name_crap_strip = company_street1_name_crap.strip('\t')
		company_street1_name = company_street1_name_crap_strip[7:]
		print(company_street1_name)
		company_info += company_street1_name + ";"

		company_street1_name_crap = article_list[company_address_index+6]
		company_street1_name_crap_strip = company_street1_name_crap.strip('\t')
		company_street1_name = company_street1_name_crap_strip[17:]
		print(company_street1_name)
		company_info += company_street1_name
	else:
		company_street1_name_crap = article_list[company_address_index+2]
		company_street1_name_crap_strip = company_street1_name_crap.strip('\t')
		company_street1_name = company_street1_name_crap_strip[8:]
		print(company_street1_name)
		company_info += company_street1_name + ","

		company_street1_name_crap = article_list[company_address_index+3]
		company_street1_name_crap_strip = company_street1_name_crap.strip('\t')
		company_street1_name = company_street1_name_crap_strip[9:]
		print(company_street1_name)
		company_info += company_street1_name + ","

		company_street1_name_crap = article_list[company_address_index+4]
		company_street1_name_crap_strip = company_street1_name_crap.strip('\t')
		company_street1_name = company_street1_name_crap_strip[7:]
		print(company_street1_name)
		company_info += company_street1_name + ";"

		company_street1_name_crap = article_list[company_address_index+5]
		company_street1_name_crap_strip = company_street1_name_crap.strip('\t')
		company_street1_name = company_street1_name_crap_strip[17:]
		print(company_street1_name)
		company_info += company_street1_name + "\n\n"

	print("\n\n")
	print(company_info)
	print("\n\n")

	with open("test.txt", "a") as myfile:
		myfile.write(company_info)

