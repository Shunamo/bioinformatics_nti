import csv
import pandas as pd
import sys
sys.path.append("../")
import subprocess
import time 
from mutations_generator import mutations
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from cluster_number_extract import clusters_dict


os.chdir(os.path.dirname(os.path.abspath(__file__)))
contact_count = pd.read_csv(f"../contact/sw_Nb49_haddock_webserver_contact_count.csv", usecols=[1], header=None)
prime_mmgbsa = pd.read_csv("../prime_mmgbsa/HER2_Nb49/sw_haddock_HER2_Nb49_output.csv",usecols=[1],header=None)

Nb49_cluster = clusters_dict[49]

mutation_contents = mutations

directory = "./"

def find_file_in_directory(directory, filename):
    # 모든 파일 iterate
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None
import pandas as pd

index = -1
max_index = len(Nb49_cluster)*4

for cluster in Nb49_cluster:
    
    for i in range(1, 5):
        index += 1
        if index + 1 > max_index:  # 인덱스 범위 확인
            continue
        
        if (len(contact_count[1][index].split(':'))<2) and int(prime_mmgbsa[1][index])> -100 :
            continue

        filename = f"residue_scanning_sw_haddock_HER2_Nb49_cluster{cluster}_{i}_prep-out.maegz"
        file_path = find_file_in_directory(directory, filename)
        if file_path:continue 
        mutation_file_name = f"residue_scanning_HER2_Nb49-mutations.txt"

        with open(mutation_file_name,'w') as mut_file:
            mut_file.write(mutation_contents)

        script =f"""#!/bin/bash
"$SCHRODINGER/run" residue_scanning_backend.py -fast -jobname residue_scanning_sw_haddock_HER2_Nb49_cluster{cluster}_{i}_prep-out -res_file residue_scanning_HER2_Nb49-mutations.txt -refine_mut prime_residue -calc hydropathy,rotatable,vdw_surf_comp,sasa_polar,sasa_nonpolar,sasa_total -dist 0.00 sw_haddock_HER2_Nb49/prep_files/sw_haddock_HER2_Nb49_cluster{cluster}_{i}_prep-out.maegz -receptor_asl 'NOT (chain.n B)' -add_res_scan_wam -HOST localhost:20 -TMPLAUNCHDIR
"""
        script_filename = f"residue_scanning_HER2_Nb49.sh"

        with open(script_filename,'w') as sh_file:
            sh_file.write(script)
        
        subprocess.run(["chmod", "+x", script_filename])

        try:
            process = subprocess.run(["./"+script_filename], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            print(process.stdout.decode())  
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr.decode()}")  
           
        
        file_path = find_file_in_directory(directory, filename)

        while not file_path:
            time.sleep(100)
            file_path = find_file_in_directory(directory, filename)
