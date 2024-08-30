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
from move_to_desktop import move_to_desktop


def find_file_in_directory(directory, filename):
    # 모든 파일 iterate
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

def program(antibody_active_residues,antibody_passive_residues,antigen_active_residues,antigen_passive_residues, prepared_antibody_pdb_file, prepared_antigen_pdb_file):
    #여기에 rename_chain 자동화 코드가 들어가면 좋을듯
    try: 
        cfg_generator(project_title, prepared_antibody_pdb_file, prepared_antigen_pdb_file)
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
        for i in range(1,101):
            if find_file_in_directory('./',f"{project_title}_emref_{i}_prep-out.maegz"):
                continue
            protein_preparation(project_title,f'./{project_title}/3_emref/',f"emref_{i}.pdb" ,40)
            time.sleep(18)        
    except Exception as e:
        print(f"Error running protein_preparation : {e}")
    #protein preparation 이후 파일명은 sw_haddock_HER2_act_Nb~~_cdr3_act_emref_~_prep-out.maegz
    
    try:
        for i in range(1,101):
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

    try:
        move_to_desktop(project_title)
        print(f"move_to_desktop operated")
        return
    except Exception as e:
        print(f"Error running move_to_desktop : {e}")

if __name__=="__main__":  
    for i in range(len(sys.argv)):
        if sys.argv[i] == '0':
            sys.argv[i] =' '
    #5번째 인자로 project_title을 주면 됨
    project_title = sys.argv[5]
    program(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[6],sys.argv[7])#1,2,3,4번째 인자로 Nb_act, Nb_pass, antigen_act, antigen_pass 주면됨, 없으면 0넣을것
    
