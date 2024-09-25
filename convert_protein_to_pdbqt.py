import subprocess
from datetime import datetime

# protein_prep_path = "/opt/ADFRSuite/bin/prepare_receptor"
protein_prep_path = "/home/jerry/software/ADFRSuite/bin/prepare_receptor"


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