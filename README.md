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

