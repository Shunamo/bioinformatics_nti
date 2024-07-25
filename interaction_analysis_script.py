
import subprocess
import time
import os
from cluster_number_extract import clusters_dict

Nb_list = [16,49,51]

domain_1 ="10-180"
domain_2 ="180-320"
domain_3 ="320-500"

domain_dict = {
    16 : domain_2,
    49 : domain_3,
    51 : domain_1
}
def sequential_logic():
    for Nb in Nb_list:
        Nb_cluster = clusters_dict[Nb]
        domain = domain_dict[Nb]
        for cluster in Nb_cluster:
            for i in range(1,5):
                
                structure_file_name = f"./HER2_Nb{Nb}/HER2_Nb{Nb}_cluster{cluster}_{i}.maegz"
                query_asl_1 = 'chain. B, res. 100-114'
                query_asl_2 = f'chain. A, res. {domain}'
                output_file = f"./contact/HER2_Nb{Nb}/HER2_Nb{Nb}_cluster{cluster}_{i}_contact.csv"
                script = f"""#!/bin/bash 
            $SCHRODINGER/run protein_interaction_analysis.py -max_neighbor_dist 4 "{structure_file_name}" "{query_asl_1}" "{query_asl_2}" "{output_file}" """
                script_filename = f"./contact/HER2_Nb{Nb}/contact_HER2_Nb{Nb}.sh"
                
                with open(script_filename, 'w') as sh_file:
                    sh_file.write(script)
                
                subprocess.run(["chmod", "+x", script_filename])
                try:
                    process = subprocess.run([script_filename], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
                    print(process.stdout.decode())  
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e.stderr.decode()}")  
        
                time.sleep(5)

def random_files_logic(dir):
    directory = f"./{dir}"
    files = os.listdir(directory)
    for file in files:
        domain = domain_dict[int(file[7:9])]#file명에서 Nb 번호를 추출하여 domain영역 설정
        structure_file_name =f"{directory}/{file}"
        query_asl_1 = 'chain. B, res. 100-114'
        query_asl_2 = f'chain. A, res. {domain}'
        output_file = f"{directory}/{file[:-7]}_contact.csv"#file명에서 maegz를 없애고 csv로 바꿈

        script = f"""#!/bin/bash 
            $SCHRODINGER/run protein_interaction_analysis.py -max_neighbor_dist 4 "{structure_file_name}" "{query_asl_1}" "{query_asl_2}" "{output_file}" """
        script_filename = f"{directory}/contact.sh"
        
        with open(script_filename, 'w') as sh_file:
            sh_file.write(script)
        
        subprocess.run(["chmod", "+x", script_filename])
        try:
            process = subprocess.run([script_filename], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            print(process.stdout.decode())  
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr.decode()}")  

        time.sleep(5)
