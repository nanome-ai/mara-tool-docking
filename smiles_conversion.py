from rdkit import Chem
from rdkit.Chem import AllChem
from datetime import datetime, date

def run(smiles: str, molecule_name: str="molecule"):
    today = date.today()
    day = today.strftime("%d%m%Y")
    now = datetime.now()
    day_time = day + f"_{now.hour}{now.minute}{now.second}"

    output_file = f'{molecule_name}_{day_time}.sdf'
  
    # Create a molecule object from SMILES
    mol = Chem.MolFromSmiles(smiles)
    
    if mol is not None:
        # Generate 3D coordinates for the molecule
        mol = Chem.AddHs(mol)  # Add hydrogen atoms
        AllChem.EmbedMolecule(mol, randomSeed=42)  # Generate 3D coordinates
        AllChem.UFFOptimizeMolecule(mol)  # Optimize the structure
        
        # Write the molecule to an SDF file
        writer = Chem.SDWriter(output_file)
        writer.write(mol)
        writer.close()
        
        print(f"SDF file created: {output_file}")
    else:
        print("Invalid SMILES string")
  