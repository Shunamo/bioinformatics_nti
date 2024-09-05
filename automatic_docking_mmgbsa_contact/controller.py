'''
특정 규칙을 작성하여 program.py 파일을 이용하는 코드
'''

import subprocess
import os
import time


def controller():

    sampling = 50

    domain_splits = [1,51,101,151]

    for domain in domain_splits:
        antigen_pass = list(range(domain, domain +50))
        antigen_pass = ",".join(map(str,antigen_pass))

        
        for Nb_act in range(100,115):
            
            Nb_pass = list(range(100,115))
            Nb_pass.remove(Nb_act)
            Nb_pass = ",".join(map(str,Nb_pass))
            
    

            script = f"""#!/bin/bash
python3 program.py {Nb_act} {Nb_pass} 0 {antigen_pass} 1N8Z_sw_haddock_HER2-domain-{domain}-split-pass_Nb51-{str(Nb_act)}-act-rest-pass HER2_prepared.pdb sw_Nb51_prep-out.pdb {sampling}
"""

            scripts = [script]

            for i, script in enumerate(scripts):
                script_filename = f"script{Nb_act+i}.sh"

                script_dir = f"/home/tinoh/domain_split_Nb51/1N8Z_sw_haddock_HER2-domain-{domain}-split-pass_Nb51-{str(Nb_act)}-act-rest-pass"
                full_script_path = os.path.join(script_dir, script_filename)

                with open(full_script_path, 'w') as sh_file:
                    sh_file.write(script)

                subprocess.run(["chmod", "+x", full_script_path])

                
            process = subprocess.Popen([full_script_path], cwd=script_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            stdout, stderr = process.communicate()
            print(f"Output of {script_filename}:\n{stdout.decode()}")

            if process.returncode != 0:
                print(f"Error in {script_filename}:\n{stderr.decode()}")
                # 필요에 따라 오류 발생 시 추가적인 조치를 수행할 수 있음

            # 다음 프로세스로 넘어가기 전에 결과가 모두 출력되었는지 확인
            time.sleep(60) 


if __name__ == "__main__":
    controller()


