
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