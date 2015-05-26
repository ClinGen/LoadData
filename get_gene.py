#! /users/bin/env Python

# Script to load gene data into local mongodb
# Gene data file (gene.txt) is downloaded from HGNC website (http://www.genenames.org/cgi-bin/download), and saved in the same directory
# No input paramenter needed
# Required to install pymongo module
# This script functions to load entire data to a collection. Re-run without clear/drop the collection will duplicate documents.

import re
import pymongo
import datetime

conn = pymongo.Connection('localhost', 27017)
db = conn.Spindle
collection = db.Gene

lineNum = 0
activeGene = 0

with open('gene.txt') as f:
    for line in f:
        if '\n' in line:
            line = line.strip('\n')
        colItem = line.split('\t')

        # There are 3 HGNC status: Approced, Entry Withdrawn, Symbol Withdrawn.
        if colItem[3] == "Approved":
            activeGene += 1
            act = "Yes" # only status Approved will be assigend as active in ClinGen curation
        else:
            act = "No"

        if colItem[7].startswith('"'):
            temp = colItem[7].lstrip('"').rstrip('"')
        else:
            temp = colItem[7]
        if temp.find('", "') != -1 :
            prename = temp.split('", "')
        else:
            prename = [temp]

        if colItem[8].find(',') != -1 :
            syn = colItem[8].split(', ')
            #synlower = colItem[8].lower()
            #synlower = synlower.split(', ')
        else:
            syn = [colItem[8]]
            #synlower = [colItem[8].lower()]

        if colItem[9].startswith('"'):
            temp = colItem[9].lstrip('"').rstrip('"')
        else:
            temp = colItem[9]
        if temp.find('", "') != -1 :
            synname = temp.split('", "')
        else:
            synname = [temp]

        if lineNum > 0 :
            newdata = {
                "HGNCID": colItem[0],
                #"HGNCIDLowercase": colItem[0].lower(),
                "HGNCSymbol": colItem[1],
                #"SymbolLowercase": colItem[1].lower(),
                "HGNCName": colItem[2],
                "HGNCStatus": colItem[3],
                "LocusType": colItem[4],
                "LocusGroup": colItem[5],
                "PreviousSymbols": colItem[6],
                #"PreviousSymbolLowercase": colItem[6].lower(),
                "PreviousNames": prename,
                "Synonyms": syn,
                #"SynonymsLowercase": synlower,
                "NameSynonyms": synname,
                "Chromosome": colItem[10],
                "AccessionNumber": colItem[11],
                "EntrezID": colItem[14],
                "PMID": colItem[13],
                "OMIMID": colItem[15],
                "Active": act,
                "Date": str(datetime.date.today())
            }
            collection.save(newdata)
        lineNum += 1

print 'Total Gene saved: %d' % (lineNum)
print 'Total Aactive assigend: %d' % (activeGene)
