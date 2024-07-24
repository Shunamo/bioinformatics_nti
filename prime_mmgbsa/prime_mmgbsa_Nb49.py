import sys
sys.path.append("../")
import subprocess
import time
import os

from ..cluster_number_extract import clusters_dict

Nb49_cluster = clusters_dict[49]

Nb_chain = 'B'

directory = "./"

def find_file_in_directory(directory, filename):
    # 모든 파일 iterate
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

for cluster in Nb49_cluster:
        for i in range(1,5):
            filename = f"HER2_Nb49_cluster{cluster}_{i}_prime_mmgbsa-out.csv" 
            file_path = find_file_in_directory(directory, filename)
            if file_path: continue
            
            script_content = f"""#!/bin/bash
        $SCHRODINGER/prime_mmgbsa  ../HER2_Nb49/prep_files/HER2_Nb49_cluster{cluster}_{i}.maegz -csv_output=yes -ligand="chain. {Nb_chain}" -jobname=HER2_Nb49_cluster{cluster}_{i}_prime_mmgbsa -job_type=ENERGY
        """
            
            script_filename = "mmgbsa_script_Nb49.sh"

            with open(script_filename, 'w') as sh_file:
                sh_file.write(script_content)

            subprocess.run(["chmod", "+x", script_filename])

            try:
                process = subprocess.run([f"./{script_filename}"], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                print(process.stdout.decode())
            except subprocess.CalledProcessError as e:
                print(f"Error: {e.stderr.decode()}")

            file_path = find_file_in_directory(directory, filename)

            while not file_path:
                time.sleep(30)
                file_path = find_file_in_directory(directory, filename)


