현재 이 폴더에 있는 HER2_prepared.pdb 는 1N8Z에서 추출한 HER2

(각종 python 프로그램의 설명과 실행방법은 .py 파일 상단에 명시해 놓았음)

1.> rename_chain.py 실행

antibody의 chain은 A로 변경되어야 한다.
antigen의 chain은 B로 변경되어야 한다.


2.> export SCHRODINGER = /opt/Schrodinger 서버에서 수행(혹은 .bashrc 파일 등을 수정)

3.> project_title 작성 양식

없는 정보는 생략, 연결된 정보에는 '-' 를 사용

antigen 관련 정보_antibody 관련 정보_docking tool 이름_antigen active residue 정보_antigen passive residue 정보_antibody active residue 정보_antibody passive residue 정보

(예시) 6J71에서 추출한 HER2 단백질을 Nb16과 docking하려 하고, docking tool은 haddock이며, HER2의 domain 2 전체를 active, passive 없고, Nb16의 cdr3의 101번을 active로 하고, 나머지를 passive로 하는 경우
    6J71_sw_haddock_HER2-domain2-act_Nb16-cdr3-101-act-rest-pass

4.> desktop <-> 원격 서버간에 파일 이동이 원활히 수행되도록 비밀번호 입력이 필요없도록 설정(ssh-keygen 기능 이용)

5.> 수행 절차
    1. (데스크탑에서) folder_generator_controller.py 실행(folder_generator 함수를 사용하는 파일로, 개별 project마다 커스터마이징 해야함)
    2. (서버에서) parent_dir/project_title 하에 있는 controller.py 실행 (controller.py에서 act,pass 등을 설정한 코드를 토대로 program.py를 실행하도록 함, controller.py는 프로그램 수행 전 필히 커스터마이징 해야함)
    3. (선택사항) 2번이 종료되면 move_to_desktop.py 실행

