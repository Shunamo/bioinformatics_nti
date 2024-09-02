'''
haddock docking 실행 시 03_emref 하에 gz형식으로 zip되어 있으므로 gunzip수행 해야함
'''
import subprocess

def gunzip(project_title):
    try:
        process = subprocess.run(
            ["gunzip", f"./{project_title}/03_emref/*"],
            check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE
        )
        print(process.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")

