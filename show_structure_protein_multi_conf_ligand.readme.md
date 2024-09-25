Combine structures of a protein PDB and multiple ligands in SDF (Informatics)

Input:
* A PDB file as the protein target (This should be the protein-only PDB file)
* A SDF file that contains multiple structures (This should come from the docking result)

Output:
* A multi-frame PDB file that contains the protein structure and all the ligands

Description:
This tool takes a protein PDB file and a SDF file that contains multiple ligands as input. It then combines the protein structure with all the ligands to create a multi-frame PDB file. The user can browse through the different frames of the PDB file to see the protein structure and all the ligands in the same coordinate space. This tool is useful for visualizing the docking results and understanding the interactions between the protein and the ligands. It should be the final step of a docking workflow.

# dockerfile prep
RUN apt-get update && apt-get install -y libgl1
RUN mamba install pymol-open-source=2.5.0