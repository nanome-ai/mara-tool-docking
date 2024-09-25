Cleanup alternate locations for residues in a PDB file (Informatics)

Input: - pdb_file: File path to a PDB file that contains alternate locations for residues
       - select_certain_altloc: when provided, only the residues with the specified alternate location will be kept in the output file.
       Otherwise, the alternate location with the highest occupancy will be kept.
Output: A cleaned PDB file with only one location for each residue
Description: This tool runs the `pdb_selaltloc` function from pdb-tools python package to clean up alternate locations for residues in a PDB file. The citation for this tool is "Rodrigues JPGLM, Teixeira JMC, Trellet M and Bonvin AMJJ. pdb-tools: a swiss army knife for molecular structures. F1000Research 2018, 7:1961 (https://doi.org/10.12688/f1000research.17456.1) "