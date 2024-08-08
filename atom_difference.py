from Bio import PDB

def extract_atoms(pdb_file):
    parser = PDB.PDBParser()
    structure = parser.get_structure('protein', pdb_file)
    atom_list = []
    
    for atom in structure.get_atoms():
        atom_info = {
            'name': atom.get_name(),
            'residue': atom.get_parent().get_resname(),
            'chain': atom.get_parent().get_parent().id,
            'residue_id': atom.get_parent().get_id(),
            'coord': atom.get_coord()
        }
        atom_list.append(atom_info)
    
    return atom_list

def compare_atoms(atom_list1, atom_list2):
    set1 = set((a['name'], a['residue'], a['chain'], a['residue_id']) for a in atom_list1)
    set2 = set((a['name'], a['residue'], a['chain'], a['residue_id']) for a in atom_list2)
    
    only_in_1 = set1 - set2
    only_in_2 = set2 - set1
    
    return only_in_1, only_in_2

# 예시 사용법
pdb_file1 = 'sw_Nb49_prep-out.pdb'
pdb_file2 = 'rf2_Nb49_prep-out.pdb'

atom_list1 = extract_atoms(pdb_file1)
atom_list2 = extract_atoms(pdb_file2)

only_in_1, only_in_2 = compare_atoms(atom_list1, atom_list2)

print(f"Atoms only in protein 1: {only_in_1}")
print(f"Atoms only in protein 2: {only_in_2}")
