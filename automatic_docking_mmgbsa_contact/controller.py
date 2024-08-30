import subprocess
import os
import time

def controller():
    processes = []

    for Nb_act in range(100,115):
        
        Nb_pass = list(range(100,115))
        Nb_pass.remove(Nb_act)
        Nb_pass = ",".join(map(str,Nb_pass))
        
        domain = list(range(10,181))
        domain = ",".join(map(str,domain))


        script = f"""#!/bin/bash
python3 program.py {Nb_act} {Nb_pass} {domain} 0 sw_haddock_HER2_all-act_Nb51_cdr3_{str(Nb_act)}-act_rest-pass HER2_prepared.pdb sw_Nb51_prep-out.pdb
"""

        scripts = [script]

        for i, script in enumerate(scripts):
            script_filename = f"script{Nb_act+i}.sh"

            script_dir = f"/home/tinoh/Nb49_Nb51_docking_generation/sw_haddock_HER2_all-act_Nb51_cdr3_{Nb_act+i}-act_rest-pass"
            full_script_path = os.path.join(script_dir, script_filename)

            with open(full_script_path, 'w') as sh_file:
                sh_file.write(script)

            subprocess.run(["chmod", "+x", full_script_path])

            
            process = subprocess.Popen([full_script_path], cwd=script_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
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


