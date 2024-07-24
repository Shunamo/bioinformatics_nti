from Bio import PDB

def renumber_residues(input_file, output_file, start_residue=1):
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure('structure', input_file)
    
    residue_number = start_residue
    for model in structure:
        for chain in model:
            for residue in chain:
                # Update the residue ID
                new_id = (' ', residue_number, ' ')
                residue.id = new_id
                residue_number += 1
    
    io = PDB.PDBIO()
    io.set_structure(structure)
    io.save(output_file)

# Example usage
input_file = "./Nb51/Nb51.pdb"
output_file = "./Nb51/Nb51_renumbered.pdb"
renumber_residues(input_file, output_file)
