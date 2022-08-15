# PDBQT-extractor
Drug discovery is a very long and cumbersome process. With the advent of computational methods like molecular docking and simulations, the burden has been reduced to some extent. But the process of creating, dowloading and coverting files required for docking is very repititive. For, this I have written a code that will extract the sdf files of ligand molecules from PubChem. PubChem is a database of chemical molecules and their activities. It is maintained by National Center for Biotechnology Information (NCBI) under National Institute of Health (NIH), USA. PubChem is a very useful database for searching chemcial structures. For docking, Autodock files known as PDBQT files are required, so the sdf files downloaded from PubChem needs to be converted to PDBQT files to make them ready for docking against protein of interest. This conversion is achieved through OpenBabel. OpenBabel is a widely used molecule file format convereter software. It is available as a linux command line tool.

For using this tool, user need to have a csv file containing the CID(s) of the compounds of interest or a CSV file downloaded from PubChem containing the details of the similar compounds. This file must be stored in a the same directory where this script is stored.

You may need to install the following python packages:
1. sys
2. subprocess
3. wget
4. pandas
5. csv
6. os

The script needs to be run as follows on your linux terminal:
$python pdbqt_extract.py CID_filename.csv similar_compound.csv
Where CID_filename.csv is the name of the csv file containing the CIDs of the compounds of interest and similar_compounds.csv is the file downloaded from pubchem containing the data of all the compounds similar to a said compound of interest.

Future prospects: Including the option to directly search for similar compounds on pubchem with the help of the script itself.
