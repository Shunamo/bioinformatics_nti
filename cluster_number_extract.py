import os
import re 

directory = "./"

Nb16_cluster = []
Nb49_cluster = []
Nb51_cluster = []

clusters_dict = {
    16: Nb16_cluster,
    49: Nb49_cluster,
    51: Nb51_cluster
}


pattern = r"cluster(\d+)_"

for Nb in [16, 49, 51]:
    middle_dir_name = f"HER2_Nb{Nb}/not_prep_files/"
    middle_path = os.path.join(directory, middle_dir_name)
    files = os.listdir(middle_path)
    
    for filename in files:
        match = re.search(pattern, filename)
        if match:
            cluster_num = match.group(1)  
            if cluster_num not in clusters_dict[Nb]:
                clusters_dict[Nb].append(cluster_num)



for Nb in [16, 49, 51]:
    tmp_array = []
    for num in clusters_dict[Nb]:
        tmp_array.append(int(num))
    
    clusters_dict[Nb] = tmp_array
    clusters_dict[Nb].sort()
    
if __name__ == "__main__":
    print(clusters_dict)
