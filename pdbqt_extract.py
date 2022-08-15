#if the user has a list of compounds they want to download the structure of and get the pdbqt files, this script is going to help
#save the CID(s) of the compounds of interest in a csv file.
#run the following script in your linux terminal as follows:
#python pdbqt_extract.py CID_filename.csv similar_compound.csv;where CID_filename.csv is the name of the csv file containing the CIDs of the compounds of interest and similar_compounds.csv is the file downloaded from pubchem containing the data of all the compounds similar to a said compound of interest.
#either one file is to be given as input for the other value must be set to zero
#the file containg the CIDs must be where the python file is.

import sys
import subprocess
import wget
import pandas as pd
import csv
import os

#if the input file is a csv file downloaded from PubChem, then some processing is needed
if sys.argv[2] != str(0):
	#saving the python file name and getting the path of the file.
	filename = str(sys.argv[2])
	path=os.getcwd()
	path=path+filename

	#cleaning the datafiles and extracting the CIDs
	df=pd.read_csv(path) #saving the csv file as panda dataframe

	#Making more uniform column labels
	df=df.rename(columns={'cid':'CID','cmpdname':'Compound Name','mw':'Molecular Weight','mf':'Molecular Formula','iupacname':'IUPAC Name'})

	#cleaning the data and keeping the required data only
	df_clean=df[['CID','Compound Name','Molecular Weight','Molecular Formula','IUPAC Name']]
	CIDs=df_clean['CID']

elif sys.argv[1] != str(0):
	#saving the python file name and getting the path of the file.
	filename = str(sys.argv[1])
	path=os.getcwd()
	path=path+filename
	
	#cleaning the datafiles and extracting the CIDs
	df=pd.read_csv(path) #saving the csv file as panda dataframe
	CIDs=df['CID'] #the CIDs must be stored in column header CID

#downloading the SDF files for the CIDs
for i in CIDs:
    SDF_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/240/record/SDF/?record_type=3d&response_type=save&response_basename=Conformer3D_CID_'+str(i)
    filename= str(i)+'.sdf'
    download_CID=wget.download(SDF_url, filename)
    print(filename+ ' downloaded') #confirming download
    
#making a folder in the cwd and moving all the sdf file there
subprocess.run('mkdir sdffiles',shell=True,stdout=subprocess.PIPE,check=True,universal_newlines=True)
subprocess.run('mv *.sdf sdffiles',shell=True,stdout=subprocess.PIPE,check=True,universal_newlines=True)

#since for docking pdbqt files are required, we convert the downloaded sdf files to pdbqt files
#coverting the sdf files to pdbqt files
for i in CIDs:
    input_file=str(i)+'.sdf'
    output_file=str(i)+'.pdbqt'
    subprocess.run('obabel '+input_file+' -O '+output_file+' --gen3d',shell=True,stdout=subprocess.PIPE,check=True,universal_newlines=True)
    print(input_file + ' coverted')

print('SUCCESS!')
