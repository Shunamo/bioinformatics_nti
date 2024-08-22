import subprocess
import sys
def folder_generator(parent_dir, project_title):

    mkdir_script = f"""#!/bin/bash
    ssh -p 40020 tinoh@203.249.75.23 'mkdir -p /home/tinoh/{parent_dir}/{project_title}'
    """
    mkdir_script_filename = f"mkdir_script.sh"

    with open(mkdir_script_filename, 'w') as sh_file:
        sh_file.write(mkdir_script)

    subprocess.run(["chmod", "+x", mkdir_script_filename])

    try:
        process = subprocess.run(["./"+mkdir_script_filename], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print(process.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")


    scp_script = f"""#!/bin/bash
    scp -P 40020 -r ./* tinoh@203.249.75.23:/home/tinoh/{parent_dir}/{project_title}"""

    scp_script_filename = f"scp_script.sh"

    with open(scp_script_filename, 'w') as sh_file:
        sh_file.write(scp_script)

    subprocess.run(["chmod", "+x", scp_script_filename])

    try:
        process = subprocess.run(["./"+scp_script_filename], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print(process.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")

if __name__ == "__main__":
    #python3 folder_generator.py parent_dir project_title
    
#    parent_dir = sys.argv[1]
#    project_title = sys.argv[2]

    parent_dir = "Nb49_Nb51_docking_generation"

    for i in range(100,115):
        folder_generator(parent_dir, f"sw_haddock_HER2_all-act_Nb51_cdr3_{i}-act_rest-pass")
