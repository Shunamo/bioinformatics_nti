'''
HER2_Nb{Nb}/not_prep_files에 haddock docking한 cluster을 전부 넣어 놓고 이 스크립트 실행
'''

import subprocess
import time
from cluster_number_extract import clusters_dict

for Nb in [16,49,51]:

    Nb_cluster = clusters_dict[Nb]

    for cluster in Nb_cluster:
        for i in range(1,5):

            script =f"""#!/bin/bash
"$SCHRODINGER/utilities/prepwizard" ./HER2_Nb{Nb}/not_prep_files/cluster{cluster}_{i}.pdb HER2_Nb{Nb}_cluster{cluster}_{i}-out.maegz -fillsidechains -disulfides -assign_all_residues -rehtreat -max_states 1 -epik_pH 7.4 -epik_pHt 2.0 -antibody_cdr_scheme Kabat -samplewater -propka_pH 7.4 -f S-OPLS -rmsd 0.3 -watdist 5.0 -JOBNAME cluster{cluster}_{i}_prep -HOST localhost:20
"""
            script_filename = f"./HER2_Nb{Nb}/cluster_prep.sh"

            with open(script_filename, 'w') as sh_file:
                sh_file.write(script)
            
            subprocess.run(["chmod", "+x", script_filename])

            try:
                process = subprocess.run([script_filename], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                print(process.stdout.decode())  
            except subprocess.CalledProcessError as e:
                print(f"Error: {e.stderr.decode()}")
            
            time.sleep(10)
