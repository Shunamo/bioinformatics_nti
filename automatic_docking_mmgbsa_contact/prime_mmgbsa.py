import sys
sys.path.append("../")
import subprocess
import time
import os

Nb_chain = 'B'

directory = "./"

def prime_mmgbsa(file_path, file_name, processor_to_use):
    
    script_content = f"""#!/bin/bash
$SCHRODINGER/prime_mmgbsa  {file_path}{file_name} -csv_output=yes -ligand="chain. {Nb_chain}" -jobname={file_name[:-6]}_prime_mmgbsa -job_type=ENERGY -HOST=localhost:{processor_to_use}
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
    #python3 prime_mmgbsa.py file_path project_title
    
    file_path = sys.argv[1]
    project_title = sys.argv[2]

    for i in range(1,101):
        if find_file_in_directory(file_path,f"{project_title}_emref_{i}_prep-out_prime_mmgbsa-out.csv"):
            continue
        prime_mmgbsa(file_path,f'{project_title}_emref_{i}_prep-out.maegz',20)
        time.sleep(200)
    
