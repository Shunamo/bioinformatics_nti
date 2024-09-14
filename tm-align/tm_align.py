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
        print(process.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")
