from pymol import cmd
from datetime import datetime

def create_timestamp() -> str:
  # helper function to create a unique timestamp
  dt = str(datetime.now())
  return dt.replace("-", "_").replace(":", "_").replace(" ", "_")

def run(protein_file_path, ligand_file_path):
    """
    Combine the protein structure with all the ligands to create a multi-frame PDB file.
    """
    cmd.load(ligand_file_path, "ligand")
    
    cmd.split_states("ligand")
    split_ligands = [obj for obj in cmd.get_object_list() if obj != "ligand"]

    cmd.load(protein_file_path, "pdb")
    for state_idx, ligand_name in enumerate(split_ligands):
        cmd.create("complex", f"{ligand_name} or pdb" , 1, state_idx + 1)
    
    filename = f"complex.{create_timestamp()}.pdb"
    filename_tmp = filename.replace(".pdb", ".tmp.pdb")
    cmd.save(filename_tmp, "complex", state=0)

    # rename the ligands named UNK to LIG in the PDB file, otherwise it will not display in Mol*
    with open(filename_tmp, "r") as f:
        content = f.read()

    with open(filename, "w") as f:
        f.write(content.replace("UNK", "LIG"))
        
    print("Combined PDB file created as", filename)