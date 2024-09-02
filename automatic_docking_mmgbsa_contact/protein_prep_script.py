'''
protein preparation을 수행하는 프로그램
template > python3 protein_preparation.py project_title file_path file_name processor_to_use 
'''
import os
import subprocess
import sys
import time
def protein_preparation(project_title, file_path, file_name,processor_to_use):
    full_file_path = os.path.join(file_path, file_name)

    script =f"""#!/bin/bash
"$SCHRODINGER/utilities/prepwizard" {full_file_path} {project_title}_{file_name[:-4]}_prep-out.maegz -fillsidechains -disulfides -assign_all_residues -rehtreat -max_states 1 -epik_pH 7.4 -epik_pHt 2.0 -antibody_cdr_scheme Kabat -samplewater -propka_pH 7.4 -f S-OPLS -rmsd 0.3 -watdist 5.0 -JOBNAME {project_title}_{file_name[:-4]}_prep -HOST localhost:{processor_to_use}
"""
    script_filename = f"prep.sh"

    with open(script_filename, 'w') as sh_file:
        sh_file.write(script)

    subprocess.run(["chmod", "+x", script_filename])

    try:
        process = subprocess.run(["./"+script_filename], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
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
    #python3 protein_prep_script.py project_title file_path file_name 
    
    project_title = sys.argv[1]
    file_path = sys.argv[2]

    full_file_path = os.path.join(file_path, project_title, '03_emref')
    for i in range(1,101):
        if find_file_in_directory(file_path,f"{project_title}_emref_{i}_prep-out.maegz"):
            continue
        protein_preparation(project_title,{full_file_path},f"emref_{i}.pdb" ,20)
        time.sleep(18)
    
