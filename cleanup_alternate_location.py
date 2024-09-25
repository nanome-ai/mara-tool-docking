from pdbtools.pdb_selaltloc import run as run_pdb_selaltloc

def run(pdb_file, select_certain_altloc="None"):
    """
    Using pdbtools to retain only a certain alternate location in a PDB file. When alternate location identifiers are
    provided, only the atoms with those identifiers will be retained. Otherwise, the alternate location with the highest
    occupancy will be retained."""
    if select_certain_altloc not in [chr(n) for n in range(65,91)]:
        select_certain_altloc = None
    file_handle = open(pdb_file, "r")
    result = run_pdb_selaltloc(file_handle, select_certain_altloc)

    output_file = pdb_file.replace(".pdb", ".clean.pdb")
    with open(output_file, "w") as f:
        for line in result:
            f.write(line)
    file_handle.close()
    print("PDB file successfully processed. Resulting file:", output_file)

if __name__ == "__main__":
    pdb_file = "4WKQ.pdb"
    run(pdb_file)