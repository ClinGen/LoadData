"""

    Usage: obtain_external_data_files.py [-h] [-s {hgnc,orphanet,clinvar}]

    Script gets source data we need from HGNC, Orphanet, or ClinVar.

    optional arguments:
      -h, --help            show this help message and exit
      -s {hgnc,orphanet,clinvar}, --source {hgnc,orphanet,clinvar}
                            (hgnc=HGNC, orphanet=Orphanet, clinvar=ClinVar)

"""

import sys
import argparse
from ftplib import FTP
import os
import gzip

purpose = 'Script gets source data we need from HGNC, Orphanet, or ClinVar.'
parser = argparse.ArgumentParser(description=purpose)

parser.add_argument("-s", "--source", choices=["hgnc", "orphanet", "clinvar"],
                    help="(hgnc=HGNC, orphanet=Orphanet, clinvar=ClinVar)")

if len(sys.argv) < 2:
    parser.print_usage()
    sys.exit(1)
else:
    args = parser.parse_args()


if args.source == "hgnc":
    print("hgnc")
    #TODO

elif args.source == "orphanet":
    print("orphanet")
    #TODO

elif args.source == "clinvar":
    print("")
    print("--------------------------------------------------")
    print("Obtaining latest ClinVar release data from the NCBI ftp site...")
    
    master_symlink_filename = "ClinVarFullRelease_00-latest.xml.gz"
    master_filename = "ClinVarFullRelease_00-latest.xml"

    # make ftp connection and identify and download the most current version of the data
    with FTP("ftp.ncbi.nlm.nih.gov") as ftp:
        ftp.login()
        unique_file_id  = None

        #get a listing of files in the clinvar xml dir
        #the unique IDs will tell us which file is symlinked to the "latest file" symlinked file so we can obtain that version
        for file in ftp.mlsd(path="pub/clinvar/xml", facts=["unique"]):
            #if file name matches the name we expect for the file symlinked to the most updated version
            if file[0] == master_symlink_filename:
                unique_file_id = file[1]["unique"]
                print("--Unique ID for {0} is {1}".format(master_symlink_filename, unique_file_id))
            #if a subsequent file has the same unique ID it is the source file for the symlink
            if file[1]["unique"] == unique_file_id and file[0] != master_symlink_filename and unique_file_id != None:
                file_to_retrieve=file[0]
                print("--The file symlinked to {0} is {1}".format(master_symlink_filename, file_to_retrieve))

        ftp.cwd('pub/clinvar/xml')
        localfile = open('data/' + file_to_retrieve, 'wb')
        ftp.retrbinary('RETR ' + file_to_retrieve, localfile.write, 1024)

        ftp.quit()
        localfile.close()

    
    #symlink the latest version to the "master" filename that should point to the most current data
    print("")
    print("--------------------------------------------------")
    print("Symlinking {0} to {1} in the ./data directory".format(master_symlink_filename, file_to_retrieve))
    if os.path.exists('data/' + master_symlink_filename):
        print("--A symlink already exists for {0}, renaming that to {0}_OLD first".format(master_symlink_filename))
        os.rename('data/' + master_symlink_filename, 'data/' + master_symlink_filename + '_OLD')
    os.symlink(file_to_retrieve, 'data/' + master_symlink_filename)

    #uncompress the downloaded file (actually the symlinked file)
    print("")
    print("--------------------------------------------------")
    print("Uncompressing {0} in the ./data directory".format(master_symlink_filename))
    gzipped_file_in = gzip.open('data/' + file_to_retrieve, 'rb')
    gzipped_file_out = open('data/' + master_filename, 'wb')
    gzipped_file_out.write( gzipped_file_in.read() )
    gzipped_file_in.close()
    gzipped_file_out.close()

    print("")
    print("--------------------------------------------------")
    print("The final ClinVar uncompressed data file {0} can be found here: data/{0}".format(master_filename))
    


print("")
print("DONE!")











