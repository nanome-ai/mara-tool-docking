# docker image preparation

WORKDIR /opt
RUN wget https://ccsb.scripps.edu/adfr/download/1038/
RUN mv index.html ADFR_install.tar.gz
RUN tar -xzf ADFR_install.tar.gz
WORKDIR /opt/ADFRsuite_x86_64Linux_1.0
RUN ./install.sh -d /opt/ADFRSuite




Convert PDB to PDBQT for AutoDock Vina-based docking (Conversion)
This script takes a PDB file as input and optionally a boolean value describing whether hydrogens will be added to the structure. It then runs a file conversion step to create a PDBQT file that can be used to define the receptor for the docking.

* Please carefully read through the conversation to see whether a pdb file is already downloaded. If not, please make sure to run "Download PDB File from RCSB Protein Data Bank using PDB Code" tool first to obtain a pdb file.
* The input pdb file should be protein-only, which means the "Save a protein-only PDB file" should always be run beforehand to obtain a protein-only PDB structure