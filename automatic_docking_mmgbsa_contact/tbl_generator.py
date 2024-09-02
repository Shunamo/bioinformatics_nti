'''
./antibody.act-pass와 ./antigen.act-pass 파일을 만들어내는 프로그램
(위 파일들은 추후 ambig.tbl의 재료가 된다. 해당 스크립트는 haddock_docker_docking에 작성되어 있다.)
'''
def tbl_generator(antibody_active_residues, antibody_passive_residues,antigen_active_residues,antigen_passive_residues):

    antibody_active_residues = antibody_active_residues.split(',')
    antibody_active_residues = " ".join(antibody_active_residues)
    antibody_passive_residues = antibody_passive_residues.split(',')
    antibody_passive_residues = " ".join(antibody_passive_residues)
    
    antigen_active_residues = antigen_active_residues.split(',')
    antigen_active_residues = " ".join(antigen_active_residues)
    antigen_passive_residues = antigen_passive_residues.split(',')
    antigen_passive_residues = " ".join(antigen_passive_residues)
    
    antibody_content=f"""{antibody_active_residues}
{antibody_passive_residues}"""
    antibody_act_pass_filename = f"./antibody.act-pass"

    with open(antibody_act_pass_filename, 'w') as antibody_act_pass_filename:
        antibody_act_pass_filename.write(antibody_content)
    
    antigen_content = f"""{antigen_active_residues}
{antigen_passive_residues}"""

    antigen_act_pass_filename = f"./antigen.act-pass"

    with open(antigen_act_pass_filename, 'w') as antigen_act_pass_filename:
        antigen_act_pass_filename.write(antigen_content)