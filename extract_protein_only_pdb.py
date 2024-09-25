from pymol import cmd
import os
from datetime import datetime

def create_timestamp() -> str:
  # helper function to create a unique timestamp
  dt = str(datetime.now())
  return dt.replace("-", "_").replace(":", "_").replace(" ", "_")

def run(input_pdb_path, add_h):
    '''
    Extract a protein only structure from an input pdb file, removing all ligands, solvents, ions and other non-protein molecules.

    :param input_pdb_path: str, path to the input pdb file
    :param add_h: bool, whether to add H to the pdb file
    '''

    # load the input pdb file
    cmd.load(input_pdb_path)

    # remove all ligands, solvents, ions and other non-protein molecules
    cmd.remove("not polymer.protein")

    # add H to the pdb file if needed
    if add_h:
        cmd.h_add()

    # save the protein only pdb file
    base_filename = os.path.basename(input_pdb_path).split(".")[0]
    output_path = "%s.protein.%s.pdb" % (base_filename, create_timestamp())
    cmd.save(output_path)

    print("Protein only structure extracted from the input pdb file at:", output_path)