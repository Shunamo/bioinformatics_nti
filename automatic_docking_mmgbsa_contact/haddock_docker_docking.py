import os
import subprocess

def haddock_docker_docking(prepared_antibody_pdb_file, prepared_antigen_pdb_file,project_title):
    docker_image = "haddock3"

    uid = os.getuid()  # 현재 사용자의 UID 가져오기
    gid = os.getgid()  # 현재 사용자의 GID 가져오기

    host_output_dir = f"./{project_title}"
    container_output_dir = f"/software/haddock3/{project_title}"

    host_cfg_path = f"./{project_title}.cfg"
    container_cfg_path = f"/software/haddock3/{project_title}.cfg"

    host_antibody_act_pass_file_path = "./antibody.act-pass"
    container_antibody_act_pass_file_path = "/software/haddock3/antibody.act-pass"

    host_antigen_act_pass_file_path = "./antigen.act-pass"
    container_antigen_act_pass_file_path ="/software/haddock3/antigen.act-pass"
    

    host_antibody_file_path = f"./{prepared_antibody_pdb_file}"
    container_antibody_file_path = f"/software/haddock3/{prepared_antibody_pdb_file}"

    host_antigen_file_path = f"./{prepared_antigen_pdb_file}"
    container_antigen_file_path = f"/software/haddock3/{prepared_antigen_pdb_file}"


    script =f"""#!/bin/bash
mkdir -p {container_output_dir}
haddock3-restraints active_passive_to_ambig ./antigen.act-pass ./antibody.act-pass > ambig.tbl
haddock3 {project_title}.cfg
"""
    script_filename = f"./host_to_docker_script.sh"
    container_script_path = "/software/haddock3/host_to_docker_script.sh"
    with open(script_filename, 'w') as sh_file:
        sh_file.write(script)

    host_script_path = "./host_to_docker_script.sh"


    os.makedirs(host_output_dir, exist_ok=True)

    run_command = [
        "docker", "run", "--name", project_title,
        "-u", f"{uid}:{gid}",
        "-v", f"{host_output_dir}:{container_output_dir}",#container에서 생성될 output_dir를 호스트로 마운트
        "-v", f"{host_script_path}:{container_script_path}",#작성한 script파일 container로 마운트
        "-v", f"{host_cfg_path}:{container_cfg_path}",#생성된 cfg파일 container로 마운트
        "-v", f"{host_antibody_file_path}:{container_antibody_file_path}", #cfg에서 쓸 antibody.pdb 마운트
        "-v", f"{host_antigen_file_path}:{container_antigen_file_path}",#cfg에서 쓸 antigen.pdb 마운트
        "-v", f"{host_antibody_act_pass_file_path}:{container_antibody_act_pass_file_path}",# host의 act,pass를 container의 act,pass 파일로 마운트 한 후
        "-v", f"{host_antigen_act_pass_file_path}:{container_antigen_act_pass_file_path}",# 해당 파일들로 스크립트를 통해 ambig.tbl파일을 생성한다.
        "-it",
        docker_image, "/bin/bash", "-c",
        f"chmod +x {container_script_path} && {container_script_path}"
    ]


    subprocess.run(run_command, check=True)
    # Wait for the container to complete
    subprocess.run(["docker", "wait", project_title], check=True)
    #finally:
    #    #다 끝나면 컨테이너 제거
    #    subprocess.run(["docker", "rm", project_title], check=True)