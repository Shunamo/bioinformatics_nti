import subprocess
import time
import os
import sys

Nb_list = [16,49,51]

domain_1 ="10-180"
domain_2 ="180-320"
domain_3 ="320-500"

domain_dict = {
    16 : domain_2,
    49 : domain_3,
    51 : domain_1,
    None : None
}
def Nb_number_return(file_name):
    if "Nb16" in file_name:
        return 16
    elif "Nb49" in file_name:
        return 49
    elif "Nb51" in file_name:
        return 51
    else:
        return None
#사용예시 > python interaction_analysis_script.py 폴더이름 이렇게 실행하면 폴더내의 모든 파일의 contact을 조사한다.
def interaction_analysis(file_path, file_name):
             
        domain = domain_dict[Nb_number_return(file_name)]#file명에서 Nb 번호를 추출하여 domain영역 설정
        if domain == None:
            print("domain 설정 오류")
            return
        
        query_asl_1 = 'chain. B, res. 100-114'
        query_asl_2 = f'chain. A, res. {domain}'
        output_file = f"{file_path}{file_name[:-6]}_contact.csv"#file명에서 maegz를 없애고 csv로 바꿈

        script = f"""#!/bin/bash 
$SCHRODINGER/run protein_interaction_analysis.py -max_neighbor_dist 4 "{file_path}{file_name}" "{query_asl_1}" "{query_asl_2}" "{output_file}" """
        script_filename = f"interaction_analysis.sh"
        
        with open(script_filename, 'w') as sh_file:
            sh_file.write(script)
        
        subprocess.run(["chmod", "+x", script_filename])
        try:
            process = subprocess.run(["./"+script_filename], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            print(process.stdout.decode())  
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr.decode()}")  

        time.sleep(5)

def find_file_in_directory(directory, filename):
    # 모든 파일 iterate
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

if __name__ == "__main__":
    #python3 interaction_analysis file_path project_title
    file_path = sys.argv[1]
    project_title = sys.argv[2]
    
    for i in range(1,101):
        if find_file_in_directory(file_path,f"{project_title}_emref_{i}_prep-out_contact.csv"):
            continue
        interaction_analysis(file_path,f'{project_title}_emref_{i}_prep-out.maegz')
        time.sleep(20)
    
