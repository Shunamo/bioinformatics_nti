from Bio import PDB
import sys
def rename_chain(input_file, output_file, old_chain_id, new_chain_id):
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure('structure', input_file)
    
    for model in structure:
        for chain in model:
            if chain.id == old_chain_id:
                chain.id = new_chain_id
    
    io = PDB.PDBIO()
    io.set_structure(structure)
    io.save(output_file)

if __name__=="__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    old_chain_id = sys.argv[3]
    new_chain_id = sys.argv[4]

    rename_chain(input_file, output_file, old_chain_id, new_chain_id)