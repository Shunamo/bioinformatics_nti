'''
chain 의 ID를 변경시키는 프로그램
(input_file name과 output_file name을 같게 설정하면 덮어씌움)

template> python3 rename_chain.py input_file output_file old_chain_id new_chain_id
예시> python3 rename_chain.py HER2_prepared.pdb HER2_prepared.pdb A B

'''

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