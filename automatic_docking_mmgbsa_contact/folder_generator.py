
"""
desktop에서 실행하여 결과물 관련 코드 전달 및 폴더를 생성하는 프로그램

해당 프로그램 실행 시
1. desktop parameter로 명시한 위치에 (있을 수도 있는) /parent_dir/project_title 을 휴지통으로 이동시킨다.
2. server_id와 server_place로 명시한 위치에 (있을 수도 있는) /parent_dir/project_title 을 휴지통으로 이동시킨다.
3. desktop parameter로 명시한 위치에 /parent_dir/project_title 을 생성한다.
4. server_id와 server_place로 명시한 위치에 /parent_dir/project_title 을 생성한다.
5. 현재 디렉터리에 있는 각종 파일들(program.py 등)을 server의 /parent_dir/project_title 에 복사한다.

template> python3 folder_generator.py parent_dir project_title desktop server_id server_port server_place
예시> python3 folder_generator.py Nb51 sw_HER2_Nb51_docking /home/nohtaeil/desktop tinoh@203.249.75.23 40020 /home/tinoh

"""

import subprocess
import sys
import os

def rm(parent_dir, project_title, desktop, server_id, server_port, server_place):
    try:
        # 로컬 디렉터리 경로
        local_path = os.path.join(desktop, parent_dir, project_title)
        # 로컬 디렉터리 휴지통으로 이동 (존재할 때만)
        if os.path.exists(local_path):
            subprocess.run(["gio", "trash", local_path], check=True)

        # 원격 디렉터리 경로
        remote_path = os.path.join(server_place, parent_dir, project_title)
        # 원격 디렉터리 휴지통으로 이동 (존재할 때만)
        ssh_check = subprocess.run(
            ["ssh", "-p", server_port, server_id, f"test -e {remote_path}"],
            check=False
        )
        if ssh_check.returncode == 0:  # 파일이나 디렉터리가 존재하는 경우
            subprocess.run(
                ["ssh", "-p", server_port, server_id, f"gio trash {remote_path}"],
                check=True
            )
    except subprocess.CalledProcessError as e:
        print(f"Error during rm: {e.stderr.decode()}")
def mkdir(parent_dir, project_title, desktop, server_id, server_port, server_place):
    try:
        # 로컬 디렉토리 생성
        os.makedirs(os.path.join(desktop, parent_dir, project_title), exist_ok=True)

        # 원격 디렉토리 생성
        subprocess.run(
            ["ssh", "-p", server_port, server_id, f"mkdir -p {os.path.join(server_place, parent_dir, project_title)}"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error during mkdir: {e.stderr.decode()}")

def rsync(parent_dir, project_title, server_id, server_port, server_place):
    try:
        # 파일을 원격 서버로 동기화
        subprocess.run(
            ["rsync", "-e", f"ssh -p {server_port}", "-r", "./", f"{server_id}:{os.path.join(server_place, parent_dir, project_title)}"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error during rsync: {e.stderr.decode()}")


def folder_generator(parent_dir,project_title,desktop,server_id,server_port,server_place):
    rm(parent_dir,project_title,desktop,server_id,server_port,server_place)
    mkdir(parent_dir,project_title,desktop,server_id,server_port,server_place)
    rsync(parent_dir,project_title,server_id,server_port,server_place)

if __name__ == "__main__":
    
    parent_dir = sys.argv[1]
    project_title = sys.argv[2]
    desktop = sys.argv[3]
    server_id= sys.argv[4]
    server_port = sys.argv[5]
    server_place = sys.argv[6]

    folder_generator(parent_dir,project_title,desktop,server_id, server_port, server_place)
