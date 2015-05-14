#! /Users/bin/env Python

# Script to load disease/phenotype data into local mongodb
# Data file (disease.xml) is downloaded from Orphanet website (http://www.orphadata.org/cgi-bin/inc/product1.inc.php), and saved in the same directory
# No input parameter need to run
# Required to install pymongo module
# This script functions to load entire data to a collection. Re-run without clear/drop the collection will duplicate documents.

from xml.etree import ElementTree as et
import pymongo

tree = et.parse('disease.xml')
disorders = tree.findall('.//Disorder')

conn = pymongo.Connection('localhost', 27017)
db = conn.Spindle
collection = db.Disease

omimNum = 0
omimMulti = 0
synonymNum = 0
synonymMulti = 0
for dis in disorders:
	#synonym = ''
	synonym = []
	omim = []
	omimFound = False
	synFound = False

	for child in dis.getchildren():
		syns = child.findall('.//Synonym')

		for syn in syns:
			synonym.append(syn.text)

		refs = child.findall('.//ExternalReference')
		for ref in refs:
			if ref.find('Source').text == 'OMIM':
				omim.append(ref.find('Reference').text)

	newdata = {
		"ORDOID": dis.find('OrphaNumber').text,
		"FullName": dis.find('Name').text,
#		"NameLowercase": dis.find('Name').text.lower(),
		"Synonym": synonym,
#		"SynonymLowercase": synonym.lower(),
		"Type": dis.find('DisorderType/Name').text,
		"OMIMID": omim,
		"Active": "Yes"
	}
	collection.save(newdata)

	if len(omim) >0: omimNum += 1
	if len(omim) > 1: omimMulti += 1
	if len(synonym) > 0: synonymNum +=1
	if len(synonym) > 1: synonymMulti += 1

print len(disorders)
print omimNum
print synonymNum
print omimMulti
print synonymMulti
