'''
자동화 프로그램의 핵심이 되는 프로그램. 
<절차>
1. cfg_generator 함수를 이용하여 .cfg파일 생성
2. tbl_generator 함수를 이용하여 ./antibody.act-pass, ./antigen.act-pass 파일 생성
3. haddock_docker_docking 함수를 이용하여 docker를 실행하여 haddock docking 실행
4. gunzip 함수가 호스트에 마운트된 파일들에 접근하여 gunzip실행
5. sampling 된 개수만큼 protein preparation 수행
6. sampling 된 개수만큼 prep 된 파일들을 prime_mmgbsa 수행
7. (현재생략) interaction_analysis함수를 통해 contact 조사 
'''

import subprocess
import sys
from protein_prep_script import protein_preparation
from gunzipper import gunzip 
import os
import time 
from prime_mmgbsa import prime_mmgbsa
from interaction_analysis import interaction_analysis
from cfg_generator import cfg_generator
from tbl_generator import tbl_generator
from haddock_docker_docking import haddock_docker_docking
import glob
#현재 directory에 파일이 있는지 찾는 함수
def find_file_in_directory(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

def program(antibody_active_residues,antibody_passive_residues,antigen_active_residues,antigen_passive_residues,project_title, prepared_antibody_pdb_file, prepared_antigen_pdb_file,sampling):
    #여기에 rename_chain 자동화 코드가 들어가면 좋을듯
    try: 
        cfg_generator(project_title, prepared_antibody_pdb_file, prepared_antigen_pdb_file,sampling)
        print("cfg generator operated")
    except Exception as e:
        print(f"Error running cfg_generator: {e}")

    try:
        tbl_generator(antibody_active_residues, antibody_passive_residues, antigen_active_residues, antigen_passive_residues)
        print("tbl_generator operated")
    except Exception as e:
        print(f"Error running tbl_generator : {e}")

    try:
        haddock_docker_docking(prepared_antibody_pdb_file, prepared_antigen_pdb_file, project_title)
        print(f"haddock_docker_docking operated")
    except Exception as e:
        print(f"Error running haddock_docker_docking : {e}")
    try:
        gunzip(project_title)
        print("gunzip operated")
    except Exception as e:
        print(f"Error running gunzip : {e}")
    
    try: 
        for i in range(1,sampling + 1):
            if find_file_in_directory('./',f"{project_title}_emref_{i}_prep-out.maegz"):
                continue
            pattern = os.path.join("./", project_title, '*_emref')
            matching_dirs = glob.glob(pattern)
            if matching_dirs:
                full_file_path = matching_dirs[0]
            protein_preparation(project_title,full_file_path,f"emref_{i}.pdb" ,40)
            time.sleep(18)        
    except Exception as e:
        print(f"Error running protein_preparation : {e}")
    #protein preparation 이후 파일명은 sw_haddock_HER2_act_Nb~~_cdr3_act_emref_~_prep-out.maegz
    
    try:
        for i in range(1,sampling + 1):
            #file_path를 project title로 해야하지만, preparation이후에 현재폴더인 ./에 있을것임 아마..
            
            prime_mmgbsa('./', f"{project_title}_emref_{i}_prep-out.maegz",40)#{project_title}_emref_{i}_prep-out_prime_mmgbsa-out.csv파일 생성됨
            file_path = find_file_in_directory("./",f"{project_title}_emref_{i}_prep-out_prime_mmgbsa-out.csv")
            if file_path:
                continue
            find_count = 0
            while not file_path:
                time.sleep(30)
                file_path = find_file_in_directory("./",f"{project_title}_emref_{i}_prep-out_prime_mmgbsa-out.csv")
                find_count+=1
                if find_count ==5: 
                    print(f"{project_title}_emref_{i}_prep-out_prime_mmgbsa can not be operated")
                    break
                continue
    except Exception as e:
        print(f"Error running prime_mmgbsa: {e}")

#    try:
#        interaction_analysis('./', f"{project_title}_emref_{i}_prep-out.maegz")#{project_title}_emref_{i}_prep-out_contact.csv파일 생성됨
#    except Exception as e:
#        print(f"Error running interaction_analysis : {e}")


if __name__=="__main__":  
    for i in range(len(sys.argv)):
        if sys.argv[i] == '0':
            sys.argv[i] =' '

    antibody_active_residues = sys.argv[1]
    antibody_passive_residues = sys.argv[2]
    antigen_active_residues = sys.argv[3]
    antigen_passive_residues = sys.argv[4]
    project_title = sys.argv[5]
    prepared_antibody_pdb_file = sys.argv[6]
    prepared_antigen_pdb_file = sys.argv[7]
    sampling = int(sys.argv[8])
    
    program(antibody_active_residues,antibody_passive_residues,antigen_active_residues,antigen_passive_residues,project_title,prepared_antibody_pdb_file, prepared_antigen_pdb_file,sampling)#없으면 0넣을것
    
