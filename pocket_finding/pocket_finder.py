# Author: Jie Li <jerry.li@nanome.ai>
# Date created: Jul 29, 2024
import os
from datetime import datetime
import shutil
import pandas as pd
from pymol import cmd

CURR_DIR = os.path.dirname(__file__)
P2RANK_PATH = os.path.join(CURR_DIR, "p2rank/prank")

def create_timestamp():
  # helper function to create a unique timestamp
  dt = str(datetime.now())
  return dt.replace("-", "_").replace(":", "_").replace(" ", "_")

class PocketFinder:
    def __init__(self, pdb, temp_dir="/tmp", **kwargs):
        '''
        pdb can be either a file path to a .pdb file, or an RCSB pdb code
        kwargs can be ref_lig, native_ligs, or any additional parameters needed by the algorithm
        '''
        self.pdb = pdb
        self.name = os.path.basename(pdb).split(".")[0]
        self.temp_dir = temp_dir
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])
        self._prepare_working_dir()

    def _prepare_working_dir(self):
        '''
        Prepare a working directory for the algorithm
        '''
        self.working_dir = os.path.join(self.temp_dir, self.name + '.' + create_timestamp())
        os.makedirs(self.working_dir, exist_ok=True)


    def find_pockets(self, save_path):
        """
        Find pockets on a protein surface using P2Rank.
        """
        # do some housekeeping steps, like creating directory for xyz file outputs
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # run P2Rank 
        cmd = "{} predict -f {} -o {} >/dev/null 2>&1".format(P2RANK_PATH, self.pdb, self.working_dir)
        os.system(cmd)

        # parse P2Rank results
        pdb_filename = os.path.basename(self.pdb)
        points_file_path = os.path.join(self.working_dir, "visualizations/data/", pdb_filename + "_points.pdb.gz")
        result_df_path = os.path.join(self.working_dir, pdb_filename + "_predictions.csv")
        results, n_pockets = self._parse_p2rank_results(points_file_path, result_df_path, save_path)

        # create multi-frame pdb file for visualization
        self._save_visualization_pdb(save_path, n_pockets)

        # return pockets
        csv_file = self._process_result_as_csv(results, save_path)

        # clean up working directory
        self._cleanup_work_folder()

        return results, csv_file
    
    def _save_visualization_pdb(self, save_path, n_pockets):
        """
        Save a cleaned pdb file.
        """
        cmd.reinitialize()
        for i in range(n_pockets):
            cmd.load(filename=os.path.join(save_path, f'protein_and_pocket_{i + 1}.pdb'))
            if i == 0:
                cmd.create("pockets", "protein_and_pocket_1")
            else:
                cmd.create("pockets", f"protein_and_pocket_{i + 1}", 1, -1)
        cmd.save(filename=os.path.join(save_path, "all_pockets.pdb"), selection="pockets", state=0)

    
    def _process_result_as_csv(self, results, save_path):
        """
        Save the results as a csv file.
        """
        result_df = pd.DataFrame(results)
        csv_file_path = os.path.join(save_path, "pocket_scores.csv")
        result_df.to_csv(csv_file_path, index=None)
        return csv_file_path

    def _parse_p2rank_results(self, points_file, result_df, save_path):
        results = []
        pockets_info = pd.read_csv(result_df)
        columns = pockets_info.columns
        n_pockets = len(pockets_info)
        cmd.reinitialize()
        cmd.load(filename=points_file, object='points')
        cmd.load(filename=self.pdb, object='prot')
        

        for i in range(n_pockets):
            residues = pockets_info.iloc[i][columns[-2]].split() # residue_ids
            score = pockets_info.iloc[i][columns[2]] # score
            center_x = pockets_info.iloc[i][columns[6]]
            center_y = pockets_info.iloc[i][columns[7]]
            center_z = pockets_info.iloc[i][columns[8]]
            
            # point file
            cmd.select(name=f'pocket_{i + 1}', selection=f'resn STP and resi {i + 1}')
            xyz_path = os.path.join(save_path, f'pocket_{i + 1}.xyz')
            cmd.save(filename=xyz_path, selection=f'pocket_{i + 1}')

            # residue file
            cmd.select(name=f'pocket_residue_{i + 1}',
                       selection=' or '.join([f'chain {res.split("_")[0]} and resi {res.split("_")[1]}' for res in residues]))
            pocket_res_pdb_path = os.path.join(save_path, f'pocket_{i + 1}.pdb') # select residues according to information from the csv file
            cmd.save(filename=pocket_res_pdb_path, selection=f'pocket_residue_{i + 1}')

            # protein + points
            cmd.select(name=f'protein_and_pocket_{i + 1}', selection=f'polymer.protein or resn STP and resi {i + 1}')
            protein_and_pocket_path = os.path.join(save_path, f'protein_and_pocket_{i + 1}.pdb')
            cmd.save(filename=protein_and_pocket_path, selection=f'protein_and_pocket_{i + 1}')


            results.append({
                "pocket_id": i + 1,
                "score": score,
                "center_x": center_x,
                "center_y": center_y,
                "center_z": center_z
            })

        return results, n_pockets
    
    def _cleanup_work_folder(self):
        shutil.rmtree(self.working_dir)


