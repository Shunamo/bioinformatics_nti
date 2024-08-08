import os
import subprocess
import time
directory = "./"
#$SCHRODINGER/utilities/proplister -a -c jobname_pv.mae

files = os.listdir(directory)

for file in files:
    if not file.endswith(".maegz"): continue
    print(file)
    
    script = f"""#!/bin/bash
$SCHRODINGER/utilities/proplister -a -c {file} -o {file[:-6]}.csv"""
    
    script_filename = "./csv_extract.sh"

    with open(script_filename,'w') as sh_file:
        sh_file.write(script)
    
    subprocess.run(["chmod", "+x", script_filename])

    try:
        process = subprocess.run([script_filename], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print(process.stdout.decode())  
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")  
    time.sleep(3)
