#! /Users/bin/env Python

# Script to load ClinVar variant data into local mongodb
# Variant data file (ClinVarFullRelease_00-latest.xml) is downloaded from ClinVar ftp site (ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/xml), and saved in the same directory
# No input parameter
# Required to install pymongo module
# This script functions to load entire data to a collection. Re-run without clear/drop the collection will duplicate documents.

import pymongo
import xml.etree.cElementTree as et

conn = pymongo.Connection('localhost', 27017)
db = conn.Spindle


# reading gene data from DB
# gene data will be grouped by Locus Type
collection = db.Gene
gene_locus = {}
g_l_count = 0
for item in collection.find({}, {"HGNCSymbol":1, "LocusType":1}):
    this_k = this_v = ''
    for k in item:
        if k == u'LocusType':
            this_v = item[k].encode()
        elif k == u'HGNCSymbol':
            this_k = item[k].encode()
        else:
            gene_locus[this_k] = this_v
            if g_l_count == 10:
                print (this_k)
                print (this_v)
    g_l_count += 1
key_list = gene_locus.keys()
print 'Done to setup gene locustype data. Set up Gene:LocusType: %d' % (g_l_count)
print (len(key_list))


# reading ClinVar xml file
tree = et.parse('ClinVarFullRelease_00-latest.xml')
clinvarsets = tree.findall('ClinVarSet')
print 'Done reading xml file.'

# parsing xml file
collection = db.Variant
clinvarset_count = 0
dbsnp_count = 0
multiple_dbsnp_count = 0
hgvs_count = 0
allele_freq_count = 0
multiple_allel_freq_count = 0
type_disease_count = 0
pethgenic_count = 0
measureset_variant_count = 0
multi-measureset_count = 0
multi_measure_count = 0

for setItem in clinvarsets:
    clinvarset_count += 1
    if clinvarset_count%10000 == 0:
        print(clinvarset_count)

    clinvar_id = setItem.find('ReferenceClinVarAssertion/ClinVarAccession').attrib['Acc']
    clinvar_title = setItem.find('Title').text
    clinical_signif = setItem.find('ReferenceClinVarAssertion/ClinicalSignificance/Description').text
    if clinical_signif == 'Pathogenic':
        pethgenic_count += 1
    dbsnp_id = []
    dbsnp_not_count = True
    allele_freq = []
    allele_freq_not_count = True
    cytogenetic_location = []
    genomic_location = []
    molecular_consequence = []
    condition_data = []
    hgvs_ids = []
    other_names = []
    gene_symbols = []
    synonym_symbols = []
    allele_info = []

    refAssertion = setItem.find('ReferenceClinVarAssertion/MeasureSet')
    measureset_type = refAssertion.attrib['Type']
    measureset_id = refAssertion.attrib['ID']
    if refAssertion.attrib['Type'] == 'Variant':
        measureset_variant_count += 1

    item_name = refAssertion.find('Name/ElementValue').text
    item_type = refAssertion.find('Measure').attrib['Type']
    item_id = refAssertion.attrib['ID']

    attributesets = refAssertion.findall('Measure/AttributeSet')
    for attr in attributesets:
        if attr.find('Attribute').attrib['Type'].startswith('HGVS'):
            hgvs_ids.append(attr.find('Attribute').text)
        elif attr.find('Attribute').attrib['Type'] == 'nucleotide change':
            other_names.append(attr.find('Attribute').text)
        elif attr.find('Attribute').attrib['Type'] == 'MolecularConsequence':
            molecular_consequence.append(attr.find('Attribute').text)
            xrefs = attr.findall('XRef')
            for xref in xrefs:
                molecular_consequence.append(xref.attrib['ID']+'@'+xref.attrib['DB'])

    cyt_locations = refAssertion.findall('Measure/CytogeneticLocation')
    if len(cyt_locations) > 0:
        for cyt_loc in cyt_locations:
            cytogenetic_location.append(cyt_loc.text)

    seq_locations = refAssertion.findall('Measure/SequenceLocation')
    if len(seq_locations) > 0:
        for seq_loc in seq_locations:
            chrom = assemb = start = stop = ''
            try:
                chrom = seq_loc.attrib['Chr']
            except:
                print seq_loc
            try:
                assemb = seq_loc.attrib['Assembly']
            except:
                print seq_loc
            try:
                start = seq_loc.attrib['start']
            except:
                print seq_loc
            try:
                stop = seq_loc.attrib['stop']
            except:
                print seq_loc

            this_loc = {
                "Chr": chrom,
                "Assembly": assemb,
                "Start": start,
                "Stop": stop
            }
            genomic_location.append(this_loc)

    temp = {}
    symbols = refAssertion.findall('Measure/MeasureRelationship/Symbol')
    for symbol in symbols:
        if symbol.find('ElementValue').text in key_list or symbol.find('ElementValue').text.decode('gbk') in key_list:
            this_locustype = gene_locus[symbol.find('ElementValue').text]
        else:
            this_locustype = ''
        temp = {"Type":symbol.find('ElementValue').attrib['Type'], "Symbol":symbol.find('ElementValue').text, "LocusType":this_locustype}
        gene_symbols.append(temp)

    measure_count = 0
    for measure in refAssertion.findall('Measure'):
        measure_count += 1
        allele = {}
        allele['Type'] = measure.attrib['Type']
        allele['ID'] =  measure.attrib['ID']
        allele_info.append(allele)

        for xref in measure.findall('XRef'):
            if xref.attrib['DB'] == 'dbSNP' and xref.attrib['ID'] not in dbsnp_id:
                dbsnp_id.append(xref.attrib['ID'])
                if dbsnp_not_count:
                    dbsnp_count += 1
                    dbsnp_not_count = False

        temp = {}
        this_value = ''
        all_source = []
        for attrSet in measure.findall('AttributeSet'):
            attr = attrSet.find('Attribute')
            if attr.attrib['Type'] is not None and attr.attrib['Type'] == 'AlleleFrequency':
                allele_freq_count += 1
                this_value = attr.text
                for xref in attrSet.findall('XRef'):
                    this_source = {}
                    for k in xref.attrib:
                        this_source[k] = xref.attrib[k]
                    all_source.append(this_source)
        temp['Value'] = this_value
        temp['Source'] = all_source
        allele_freq.append(temp)
    if measure_count > 1:
        multi_measure_count += 1
    if len(allele_freq) > 1:
        multiple_allel_freq_count += 1
    if len(dbsnp_id) > 1:
        multiple_dbsnp_count += 1

    temp = {}
    traits = setItem.findall('ReferenceClinVarAssertion/TraitSet/Trait')
    for trait in traits:
        #temp = {"Type":"", "Term":"", "Genes":[]}
        if trait.find('Name/ElementValue').attrib['Type'] == 'Preferred':
            temp["Type"] = trait.attrib['Type']
            temp["Term"] = trait.find('Name/ElementValue').text
            if trait.find('Name/XRef'):
                temp["SourceDB"] = trait.find('Name/XRef').attrib['DB']
                temp["SourceID"] = trait.find('Name/XRef').attrib['ID']
            else:
                temp["SourceDB"] = ''
                temp["SourceID"] = ''
        genes_involved = trait.findall('Symbol')
        g_temp = []
        for gene in genes_involved:
            g_temp.append(gene.find('ElementValue').text)
        temp["Genes"] = g_temp
        condition_data.append(temp)

    if len(hgvs_ids) > 0:
        hgvs_count += 1

    newdata = {
        "SpindleVariantID": str(clinvarset_count),
        "Source": "ClinVar",
        "Active": "Yes",
        "ClinVarID": clinvar_id,
        "MeasuresetType": measureset_type,
        "ClinVarVariantID": measureset_id,
        "AlleleInfo": allele_info,
        "dbSNPID": dbsnp_id,
        "VariantHGVS": hgvs_ids,
        "ClinVarTitle": clinvar_title,
        "VariantName": item_name,
        "ClinVarSubmissionID": item_id,
        "VariantType": item_type,
        "CytogeneticLocation": cytogenetic_location,
        "GenomicLocation": genomic_location,
        "OtherNames": other_names,
        "ClinicalSignificance": clinical_signif,
        "GeneSymbols": gene_symbols,
        "SynonymSymbols": synonym_symbols,
        "MolecularConsequence": molecular_consequence,
        "Conditions": condition_data,
        "AlleleFrequency": allele_freq,
        "Association": {}
    }
    collection.save(newdata)

print "Total ClinVarSet read: %d" % (clinvarset_count)
print "Total # of Measureset Variant Type: %d" % (measureset_variant_count)
print "Total with dbSNP ID: %d" % (dbsnp_count)
print "Total with Multiple dbSNP: %d" % (multiple_dbsnp_count)
print "Total with HGVS: %d" % (hgvs_count)
print "Total with Pathogenic: %d" % (pethgenic_count)
print "Total with Allele Frequency: %d" % (allele_freq_count)
print "Total with Multiple Allele Frequency: %d" % (multiple_allel_freq_count)
