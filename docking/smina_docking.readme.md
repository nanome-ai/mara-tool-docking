This tool runs the Smina program to dock a ligand into a protein target. The user should provide the protein target as a .pdbqt file, the ligand as a .sdf file, and the center_x, center_y, center_z, size, and exhaustiveness values for the docking box.  The center of the box should be obtained by first running the "Find pockets for docking on the input protein" tool. The tool will then run the docking algorithm and output a .sdf file containing the docked poses of the ligand.

# Input: 
* Protein target given as .pdbqt file. If no pdbqt file is available, you should run the "Convert PDB to PDBQT for AutoDock Vina-based docking" tool to obtain a pdbqt file.
* Ligand for docking, should be a .sdf file. 
* center_x, center_y, center_z: coordinates of the center of the docking box. You should first run "Find pockets for docking on the input protein" to find available pockets for docking, and ask the user to select a pocket, then you should use the center_x, center_y, center_z values for the user selected pocket as input for this tool. Do not assume the binding site is known. Do not make up numbers. Always run "Find pockets for docking on the input protein" to make sure you have reliable information.
* size: size of the docking box. Unless the user has specifically specified this value, a default value of 25 should be used.
* exhaustiveness: exhaustiveness setting for the docking. Unless the user has specifically specified this value, a default value of 8 should be used.

# Output:
* A .sdf file containing multiple poses of the ligand from the docking run. 

# General docking workflow
Docking is used to predict the binding structure of a ligand in the protein. So you should expect there is already a ligand file in the context (usually in the format of .sdf file). The protein file can be either a .pdb file or a .cif/.mmcif file.

For the ligand file, it should be generated from either the "Convert SMILES into Single Frame SDF" tool, from a user-provided sdf file, or extracted from an existing structure. Please DO NOT use "Generate conformers from a SMILES list and write them to an SDF File" for preparing sdf files for docking, because that tool generates unnecessary conformations. If the ligand is downloaded from ChEMBL using ChEMBL ID, please minimize the structure using "Minimize from a SDF File" before docking

Here is a list of related tools for the complete docking process, and the order for running these tools. It is essential to follow this docking process and please follow exactly for the order and tools here. Otherwise the docked results might be unreasonable!
1. Extract protein from PDB or mmCIF File: this is used to make sure the protein used for docking is in .pdb format and does not contain any component not required for docking (PLEASE DO NOT SKIP THIS STEP whenever the user asked for docking, because the user provided pdb file or those downloaded from rcsb might contain components that will make docking fail!)
2. Find pockets for docking on the input protein: This step finds potential binding pockets from the protein-only structure in step 1, and shows all potential pockets for the user to decide which pocket to dock. You should ALWAYS run this step to get the actual pocket position. DO NOT MAKE UP NUMBERS!
3. Convert PDB to PDBQT for AutoDock Vina-based docking: This step converts the protein-only PDB file from step 1 into a PDBQT file that is required to run docking
4. Run docking using Smina (this tool): Run the actual docking with the prepared .pdbqt file from step 3 and the ligand .sdf file from the conversation.
5. Combine structures of a protein PDB and multiple ligands in SDF: This step combines the docked results from step 4 and the protein structure from step 1 into a single .pdb file for visualization.

# docker prep

WORKDIR /opt
RUN wget https://sourceforge.net/projects/smina/files/smina.static/download -O smina