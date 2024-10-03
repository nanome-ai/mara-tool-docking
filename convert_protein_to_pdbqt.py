import subprocess
from datetime import datetime
from Bio import PDB
from pdbtools.pdb_selaltloc import run as run_pdb_selaltloc


# protein_prep_path = "/opt/ADFRSuite/bin/prepare_receptor"
protein_prep_path = "/home/jerry/software/ADFRSuite/bin/prepare_receptor"

def set_altloc(pdb_file):
    """
    Using pdbtools to retain only a certain alternate location in a PDB file. Only the atoms with those identifiers will be retained."""
    file_handle = open(pdb_file, "r")
    result = run_pdb_selaltloc(file_handle, None)

    processed_file = pdb_file.replace(".pdb", ".set_altloc.pdb")
    with open(processed_file, "w") as f:
        for line in result:
            f.write(line)
    file_handle.close()
    return processed_file

def create_timestamp() -> str:
  # helper function to create a unique timestamp
  dt = str(datetime.now())
  return dt.replace("-", "_").replace(":", "_").replace(" ", "_")

def run(pdb_path, add_h):
    '''
    Convert a pdb file to a pdbqt file that can be used for AutoDock docking

    :param pdb_path: str, path to the pdb file
    :param add_h: bool, whether to add H to the pdb file
    '''
    # check whether need to remove alternate locations
    structure = PDB.PDBParser().get_structure("protein", pdb_path)
    for residue in structure.get_residues():
        if sum([atom.is_disordered() for atom in residue.get_atoms()]) > 0:
            pdb_path = set_altloc(pdb_path)
            print("Alternate locations found in the PDB file. Retained only the highest occupied location.")
            print('If you want to keep certain alternate locations, please run the "Cleanup alternate locations for residues in a PDB file" tool \
with the "select_certain_altloc" argument.')
            break


    # run protein preparation depending on if there's need to add H
    output_path = pdb_path.replace(".pdb", ".%s.pdbqt" % create_timestamp())
    if add_h:
        try:
            out = subprocess.run([protein_prep_path, '-r', pdb_path, '-o', output_path,\
            '-A', 'checkhydrogens'])
        except subprocess.CalledProcessError as e:
            print("Error while converting pdb to pdbqt:", e.output)
    else:
        try:
            out = subprocess.run([protein_prep_path, '-r', pdb_path, '-o', output_path,])
        except subprocess.CalledProcessError as e:
            print("Error while converting pdb to pdbqt:", e.output)
    
    print("PDB file successfully converted to PDBQT file at:", output_path)

if __name__ == "__main__":
    pdb_path = "./4WKQ.pdb"
    run(pdb_path, add_h=True)