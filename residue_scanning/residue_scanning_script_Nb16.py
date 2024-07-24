import sys
sys.path.append("../")
import subprocess
import time 
from mutations_generator import mutations
import os
from ..cluster_number_extract import clusters_dict

Nb16_cluster = clusters_dict[16]

mutation_contents = mutations

directory = "./"

def find_file_in_directory(directory, filename):
    # 모든 파일 iterate
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

for cluster in Nb16_cluster:
    for i in range(1,5):
        filename = f"residue_scanning_HER2_Nb16_cluster{cluster}_{i}-out.maegz"
        file_path = find_file_in_directory(directory, filename)
        if file_path: continue

        mutation_file_name = f"residue_scanning_HER2_Nb16-mutations.txt"

        with open(mutation_file_name,'w') as mut_file:
            mut_file.write(mutation_contents)

        script =f"""#!/bin/bash
"$SCHRODINGER/run" residue_scanning_backend.py -fast -jobname residue_scanning_HER2_Nb16_cluster{cluster}_{i} -res_file residue_scanning_HER2_Nb16-mutations.txt -refine_mut prime_residue -calc hydropathy,rotatable,vdw_surf_comp,sasa_polar,sasa_nonpolar,sasa_total -dist 0.00 ../HER2_Nb16/prep_files/HER2_Nb16_cluster{cluster}_{i}.maegz -receptor_asl 'NOT (chain.n B)' -add_res_scan_wam -HOST localhost:20 -TMPLAUNCHDIR
"""
        script_filename = f"residue_scanning_HER2_Nb16.sh"

        with open(script_filename,'w') as sh_file:
            sh_file.write(script)
        
        subprocess.run(["chmod", "+x", script_filename])

        try:
            process = subprocess.run([script_filename], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            print(process.stdout.decode())  
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr.decode()}")  
        
                
        

        file_path = find_file_in_directory(directory, filename)

        while not file_path:
            time.sleep(100)
            file_path = find_file_in_directory(directory, filename)
            
        