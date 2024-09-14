'''
서버에서 나온 결과를 desktop으로 옮기는 코드

해당 프로그램 실행시
1. server의 /parent_dir/project_title 하에 있는 모든 데이터를 desktop_id 의 desktop_place/parent_dir/project_title 로 복사한다.

template> python3 move_to_desktop.py parent_dir project_title desktop_id desktop_place server_place
예시> python3 move_to_desktop.py Nb51 sw_HER2_Nb51_docking nohtaeil@223.194.69.116 /home/nohtaeil/Desktop /home/tinoh

'''
    
import subprocess
import sys
def move_to_desktop(parent_dir,project_title,desktop_id,desktop_place,server_place):
    script=f"""#!/bin/bash
scp -r {server_place}/{parent_dir}/{project_title}/* {desktop_id}:{desktop_place}/{parent_dir}/{project_title}
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

if __name__=="__main__":
    parent_dir = sys.argv[1]
    project_title = sys.argv[2]
    desktop_id = sys.argv[3]
    desktop_place = sys.argv[4]
    server_place =sys.argv[5]

    move_to_desktop(parent_dir,project_title,desktop_id,desktop_place,server_place)