import subprocess
import sys

def gunzip(project_title):
    command = f"gunzip ./{project_title}/*_emref/*"
    try:
        process = subprocess.run(command, check=True, shell=True, text=True, capture_output=True)
        if process.stdout:
            print(process.stdout)
        if process.stderr:
            print(process.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <project_title>")
    else:
        project_title = sys.argv[1]
        gunzip(project_title)
