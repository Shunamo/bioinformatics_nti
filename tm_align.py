import subprocess


def tm_align(standard_pdb, compare_pdb):
    script = f"""#!/bin/bash
./TMalign_cpp {standard_pdb} {compare_pdb}
"""
    script_filename = f"tm_align.sh"

    with open(script_filename, 'w') as sh_file:
        sh_file.write(script)

    subprocess.run(["chmod", "+x", script_filename])

    try:
        process = subprocess.run(["./"+script_filename], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        content = process.stdout.decode()
        return content
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")

targets = ["1N8Z","1S78","7MN5","7MN6","8FFJ","8HGO"]

for target in targets:
    with open(f"tm-align_6J71_{target}.txt","w") as file:
        for i in range(1,5):
            file.write(tm_align(f"HER2_6J71_domain{i}.pdb",f"HER2_{target}_domain{i}.pdb"))