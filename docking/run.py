from datetime import datetime
import subprocess
SMINA_BINARY = "/opt/smina"

def create_timestamp() -> str:
  # helper function to create a unique timestamp
  dt = str(datetime.now())
  return dt.replace("-", "_").replace(":", "_").replace(" ", "_")

def run(receptor, ligand, center_x, center_y, center_z, size, exhaustiveness):
    """Runs docking with smina

    Args:
        receptor (str): Path to the receptor file, should be a .pdbqt file
        ligand (str): Path to the ligand file
        output (str): Path to the output file
        center_x (float): x-coordinate of the center of the docking box
        center_y (float): y-coordinate of the center of the docking box
        center_z (float): z-coordinate of the center of the docking box
        size (float): Size of the docking box. The box will be a cube with sides of length `size`
        exhaustiveness (int): exhaustiveness setting for docking
    """
    output_file = "docking." + create_timestamp() + ".sdf"
    cmd = f'{SMINA_BINARY} --receptor {receptor} --ligand {ligand} --out {output_file} --center_x {center_x} \
        --center_y {center_y} --center_z {center_z} --size_x {size} --size_y {size} --size_z {size} \
        --exhaustiveness {exhaustiveness} --min_rmsd_filter 0.5'
    subprocess.run(cmd, shell=True, check=True)
    print(f"Docking completed. Results are given as {output_file}")