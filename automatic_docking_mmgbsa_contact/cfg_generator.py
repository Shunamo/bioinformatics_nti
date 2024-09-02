'''
haddock docking에 필요한 .cfg파일을 만들어내는 프로그램
'''

def cfg_generator(project_title, prepared_antibody_pdb_file, prepared_antigen_pdb_file,sampling):
    content=f"""run_dir = "{project_title}"
mode = "local"
ncores = 40

molecules = [
    "{prepared_antibody_pdb_file}",
    "{prepared_antigen_pdb_file}"
    ]

[topoaa]

[rigidbody]
tolerance = 20
ambig_fname = "ambig.tbl"
sampling = {sampling}

[flexref]
tolerance = 20
ambig_fname = "ambig.tbl"

[emref]
tolerance = 20
ambig_fname = "ambig.tbl"

[mdref]
tolerance = 20
ambig_fname = "ambig.tbl"

[caprieval]

[emscoring]

[mdscoring]

[alascan]
output = True
scan_residue = 'ALA'

[contactmap]

[clustfcc]
threshold = 1


"""
    cfg_file_name = f"./{project_title}.cfg"

    with open(cfg_file_name, 'w') as cfg_file_name:
        cfg_file_name.write(content)
