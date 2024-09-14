'''
prime mmgbsa 를 수행하는 프로그램
template >python3 prime_mmgbsa.py file_path project_title processor_to_use
예시 > python3 prime_mmgbsa.py ./ sw_HER2_Nb51_docking
'''

import sys
sys.path.append("../")
import subprocess
import time
import os

def prime_mmgbsa(file_path, file_name, processor_to_use):
    full_file_path = os.path.join(file_path, file_name)
    script_content = f"""#!/bin/bash
$SCHRODINGER/prime_mmgbsa  {full_file_path} -csv_output=yes -ligand="chain. A" -jobname={file_name[:-6]}_prime_mmgbsa -job_type=ENERGY -HOST=localhost:{processor_to_use}
"""
    
    script_filename = "mmgbsa_script.sh"

    with open(script_filename, 'w') as sh_file:
        sh_file.write(script_content)

    subprocess.run(["chmod", "+x", script_filename])

    try:
        process = subprocess.run([f"./{script_filename}"], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print(process.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")
    

def find_file_in_directory(directory, filename):
    # 모든 파일 iterate
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

if __name__ == "__main__":

    file_path = sys.argv[1]
    project_title = sys.argv[2]
    processor_to_use = sys.argv[3]
    
    for i in range(1,51):
        if find_file_in_directory(file_path,f"{project_title}_emref_{i}_prep-out_prime_mmgbsa-out.csv"):
            continue
        prime_mmgbsa(file_path,f'{project_title}_emref_{i}_prep-out.maegz',20)
        find_count = 0
        while True:
            if find_count == 30: break
            if find_file_in_directory(file_path,f"{project_title}_emref_{i}_prep-out_prime_mmgbsa-out.csv"):
                break
            else:
                find_count +=1
                time.sleep(10)
        
        
    
