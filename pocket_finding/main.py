from pocket_finder import PocketFinder
from datetime import datetime
import pandas as pd

def create_timestamp():
  # helper function to create a unique timestamp
  dt = str(datetime.now())
  return dt.replace("-", "_").replace(":", "_").replace(" ", "_")

def run(input_pdb_path):
    '''Run pocket finder with P2Rank to find potential pockets'''
    pf = PocketFinder(pdb=input_pdb_path)
    output_path = create_timestamp()
    pf.find_pockets(save_path=output_path)

    result_df = pd.read_csv(output_path + "/pocket_scores.csv")
    print("The pockets that have been found are:")
    print(result_df)
    print("Please include these pocket information in a table in the output.")
    print("You could also see the pockets in this PDB file:", output_path + "/all_pockets.pdb")
    print("You could browse its different frames for the different pockets.")