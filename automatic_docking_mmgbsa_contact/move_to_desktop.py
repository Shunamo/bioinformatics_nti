import subprocess

def move_to_desktop(project_title):
    script=f"""#!/bin/bash
scp -r ./* nohtaeil@223.194.69.116:/home/nohtaeil/Desktop/automatic/{project_title}/
"""
    script_filename = f"move_to_desktop.sh"

    with open(script_filename, 'w') as sh_file:
        sh_file.write(script)

    subprocess.run(["chmod", "+x", script_filename])

    try:
        process = subprocess.run(["./"+script_filename], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print(process.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")