Find pockets for docking on the input protein (Informatics)

Input: A PDB fileas the docking target
Output: Tabular information about all the found pockets, and a multi-frame PDB file to show the position of all pockets
Detail: This tool runs a pocket finding algorithm (P2Rank) to find all the pockets on the input protein. It then prints out the pocket information, and also saves a multi-frame PDB file to show the position of all the pockets on the protein structure. The user can browse through the different frames of the PDB file to see all the pockets. This tool should first be executed whenever the user asks for docking, and should prompt the user to select a pocket to run the actual docking step.

**Please output a table for the pocket information, and ask user to select a pocket!**



# Docker preparation

WORKDIR /opt
RUN apt-get update && apt-get install -y libgl1 default-jdk
RUN mamba install pymol-open-source=2.5.0

RUN git clone https://github.com/nanome-ai/mara-tool-docking.git
WORKDIR /opt/mara-tool-docking
WORKDIR /opt/mara-tool-docking/pocket_finding/

- requirements
pandas