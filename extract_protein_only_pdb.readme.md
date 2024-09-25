Save a protein-only PDB file (Informatics)

This tool takes a PDB file, remove anything that is not a protein, such as binding ligands, solvents, ions, etc., and save a cleaned PDB file as a new one. Optionally it can also add hydrogens to the resulting structure. 


# args:
- input_pdb_path: The file path to the input PDB file that might contain molecules other than the protein itself
- add_h: whether to add H to the resulting pdb file

# dockerfile prep
RUN apt-get update && apt-get install -y libgl1
RUN mamba install pymol-open-source=2.5.0