# LoadData
Python scripts to load pre-curation data into local mongodb

1. Three python scripts to load gene, disease and variant data into local mongodb respectively.
2. Data files are downloaded from HGNC, Orphanet and ClinVar website:   
    www.genenames.org/cgi-bin/download  
    www.orphadata.org/cgi-bin/inc/product1.inc.php  
    ftp.ncbi.nlm.nih.gov/pub/clinvar/xml
3. To run the scripts, pymongo is required
4. These scripts functions to load entire data into collections. Re-run without clear/drop collection will make duplicated documents


# Obtaining the data
The `obtain_external_data_files.py` script can be used to obtain the source files necessary for loading.

Usage:  `python3 obtain_external_data_files.py [--help] [--source {hgnc,orphanet,clinvar}]`

(requires the python `requests` module: `pip3 install requests`)


# Experimental Clinvar parsers
--Generated from the April 3, 2015 `clinvar_public.xsd` available from the ClinVar ftp site using the generateDS python package
NOTE: Python2.7 only, and must `pip install lxml` first  
NOTE2: Has to read in the whole XML file so developing using smaller files (like ClinVar sample file) while still "in progress" recommended  
NOTE3: These are just starter scripts, as a proof of concept that we could generate Python data structures from the ClinVar ftp data even if the 
upstream schema changes. These would then need to be modified or used in combination with other scripts to subsequently shape the data to our 
JSON-LD needs but maybe without the heavy lifting of doing a lot of work to re-shape the parser(s) each time the schema changes.

`clinvar_sub.py [clinvar.xml]`  (just outputs input xml currently)
`clinvar_api.py [clinvar.xml]`  (just outputs input xml currently)