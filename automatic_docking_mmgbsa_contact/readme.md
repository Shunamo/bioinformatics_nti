1.>
antibody의 chain은 A로 변경되어야 한다.
antigen의 chain은 B로 변경되어야 한다.
=> rename_chain.py 사용

2.>
export SCHRODINGER = /opt/Schrodinger 하기

3.>
[project_title 양식, 없는 정보는 생략, 연결된 정보에는 '-' 를 사용]
antigen 관련 정보_antibody 관련 정보_docking tool 이름_antigen active residue 정보_antigen passive residue 정보_antibody active residue 정보_antibody passive residue 정보
(예시) 6J71에서 추출한 HER2 단백질을 Nb16과 docking하려 하고, docking tool은 haddock이며, HER2의 domain 2 전체를 active, passive 없고, Nb16의 cdr3의 101번을 active로 하고, 나머지를 passive로 하는 경우
6J71_sw_haddock_HER2-domain2-act_Nb16-cdr3-101-act-rest-pass

 