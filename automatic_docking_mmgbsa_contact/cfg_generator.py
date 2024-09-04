'''
haddock docking에 필요한 .cfg파일을 만들어내는 프로그램
'''
import sys
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

[caprieval]

[clustfcc]


[contactmap]

[alascan]
output = True

[emscoring]

[mdref]
tolerance = 20
ambig_fname = "ambig.tbl"

[caprieval]

[mdscoring]

"""
    cfg_file_name = f"./{project_title}.cfg"

    with open(cfg_file_name, 'w') as cfg_file_name:
        cfg_file_name.write(content)

if __name__ == "__main__":
    project_title = sys.argv[1]
    prepared_antibody_pdb_file = sys.argv[2]
    prepared_antigen_pdb_file = sys.argv[3]
    sampling = sys.argv[4]

    cfg_generator(project_title, prepared_antibody_pdb_file,prepared_antigen_pdb_file,sampling)