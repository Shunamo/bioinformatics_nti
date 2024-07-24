import os
from cluster_number_extract import clusters_dict
import sys
directory = './'

'''
이 함수는 HER2_Nb{Nb}/prep_files/에 있는 HER2_Nb{Nb}_cluster{cluster}_{i}-out.maegz 이러한 이름의 파일을
 HER2_Nb{Nb}_cluster{cluster}_{i}.maegz 이렇게 바꾼다.
'''
def rename_prepared_clusters():

    for Nb in [16, 49, 51]:
        middle_dir_name = f"HER2_Nb{Nb}/prep_files/"
        middle_path = os.path.join(directory, middle_dir_name)
        files = os.listdir(middle_path)
        Nb_cluster = clusters_dict[Nb]
        for cluster in Nb_cluster:
            for i in range(1, 5):
                for filename in files:
                    if filename == f"HER2_Nb{Nb}_cluster{cluster}_{i}-out.maegz":
                        old_path = os.path.join(middle_path, filename)
                        new_filename = f"HER2_Nb{Nb}_cluster{cluster}_{i}.maegz"
                        new_path = os.path.join(middle_path, new_filename)
                        os.rename(old_path, new_path)


# python rename.py rename_prepared_clusters 이렇게 실행하면 rename_prepared_clusters함수가 실행된다.
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "rename_prepared_clusters":
            rename_prepared_clusters()