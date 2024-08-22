import subprocess
import os
import time
'''
for Nb_act in range(100,115):
    project_title = f"sw_haddock_HER2_all-act_Nb49_cdr3_{Nb_act}-act_rest-pass"

    pre_Nb_pass = list(range(100,115))
    pre_Nb_pass.remove(Nb_act)
    Nb_pass = ",".join(map(str, pre_Nb_pass))

    antigen_act = list(range(320,501))
    antigen_act = ",".join(map(str, antigen_act))
    whole_script = f"python3 program.py {Nb_act} {Nb_pass} {antigen_act} 0 {project_title} HER2_prepared.pdb sw_Nb49_prep-out.pdb"
    print(whole_script)
'''
    
def controller():
    processes = []

    for Nb_act in range(103,115,2):
        
        Nb_pass_1 = list(range(100,115))
        Nb_pass_1.remove(Nb_act)
        Nb_pass_1 = ",".join(map(str,Nb_pass_1))

        Nb_pass_2 = list(range(100,115))
        Nb_pass_2.remove(Nb_act+1)
        Nb_pass_2 = ",".join(map(str,Nb_pass_2))




        domain = "10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180"


        script_1 = f"""#!/bin/bash
python3 program.py {Nb_act} {Nb_pass_1} {domain} 0 sw_haddock_HER2_all-act_Nb51_cdr3_{str(Nb_act)}-act_rest-pass HER2_prepared.pdb sw_Nb51_prep-out.pdb
"""
        script_2 = f"""#!/bin/bash
python3 program.py {Nb_act+1} {Nb_pass_2} {domain} 0 sw_haddock_HER2_all-act_Nb51_cdr3_{str(Nb_act+1)}-act_rest-pass HER2_prepared.pdb sw_Nb51_prep-out.pdb
"""




        scripts = [script_1, script_2]
        

        for i, script in enumerate(scripts):
            script_filename = f"script{i+1}.sh"

            script_dir = f"/home/tinoh/Nb49_Nb51_docking_generation/sw_haddock_HER2_all-act_Nb51_cdr3_{Nb_act+i}-act_rest-pass"
            full_script_path = os.path.join(script_dir, script_filename)

            with open(full_script_path, 'w') as sh_file:
                sh_file.write(script)

            subprocess.run(["chmod", "+x", full_script_path])

            
            process = subprocess.Popen([full_script_path], cwd=script_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            processes.append((process, script_filename))
        
        time.sleep(45000)
    # 모든 프로세스가 완료될 때까지 기다림
    for process, script_filename in processes:
        stdout, stderr = process.communicate()
        print(f"Output of {script_filename}:\n{stdout.decode()}")
        if process.returncode != 0:
            print(f"Error in {script_filename}:\n{stderr.decode()}")


if __name__ == "__main__":
    controller()


