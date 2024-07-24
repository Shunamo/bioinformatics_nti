from Bio import PDB

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

#chain A이면 chain H로 이름을 바꾼다
old_chain_id = "A"
new_chain_id = "H"

for Nb in [16,49,51]:
    input_file = f"./Nb{Nb}/Nb{Nb}_prep/Nb{Nb}_prep-out.pdb"
    output_file = f"./Nb{Nb}/Nb{Nb}_prep/Nb{Nb}_prep-out_rename_chain.pdb"


    rename_chain(input_file, output_file, old_chain_id, new_chain_id)
