#! /Users/bin/env Python

# Script to parse and load ClinVar variant data into local mongodb. These data are used to compare and test with those in BCM's CAR API.
# XML data file (ClinVarFullRelease_2015-10.xml) is downloaded from ClinVar ftp site (ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/xml), and saved in the same directory
# No input parameter required
# Require to install pymongo module
# This script functions to load entire data to a collection. Automaticall drop existing collection before saving new data.
# Last modified by Kang Liu at 01/28/2016

import pymongo
import xml.etree.cElementTree as et


# reading ClinVar xml file
print('Start reading xml file ...')
#tree = et.parse('ClinVarFullRelease_2014-02.xml')
tree = et.parse('ClinVarFullRelease_2015-10.xml')
clinvarsets = tree.findall('ClinVarSet')
print('Total # of ClinVarSet, RCV: ', len(clinvarsets))

# parsing xml file
clinvarset_count = 0
variant_obj = {}
print('Start parsing xml data ...')
for setItem in clinvarsets:
    clinvarset_count += 1
    if clinvarset_count % 10000 == 0:
        print(clinvarset_count)

    rcv_id = setItem.find('ReferenceClinVarAssertion/ClinVarAccession').attrib['Acc']

    measureSet = setItem.find('ReferenceClinVarAssertion/MeasureSet')
    measureset_id = measureSet.attrib['ID']
    if measureset_id not in variant_obj.keys():
        variant_obj[measureset_id] = {
            'RCVAssociated': [rcv_id],
            'AlleleIncluded': []
        }
        for measure in measureSet.findall('Measure'):
            allele_id = measure.attrib['ID']
            allele_type = measure.attrib['Type']
            variant_obj[measureset_id]['AlleleIncluded'].append({
                'ID': allele_id,
                'Type': allele_type
            })
    else:
        variant_obj[measureset_id]['RCVAssociated'].append(rcv_id)
print('Total # of variant: ', len(variant_obj.keys()))

# save into db
conn = pymongo.Connection('localhost', 27017)
db = conn.Spindle
collection = db.ClinVarVariantOnlyOct2015
collection.drop()

print('Start saving data to local db ...')
for k in variant_obj:
    collection.save(variant_obj[k])
print('Done')
