
import pandas as pd
import os
import csv
import sys
sys.path.append("../")

from cluster_number_extract import clusters_dict


for Nb in [16,49,51]:

    f = open(f"HER2_Nb{Nb}_output.csv",'w')

    with open(f"HER2_Nb{Nb}_output.csv",'a',newline='') as f:
        Nb_cluster = clusters_dict[Nb]
        for cluster in Nb_cluster:
            for i in range(1, 5):
                for filename in os.listdir(f'./'):
                    if filename == f"HER2_Nb{Nb}_cluster{cluster}_{i}_prime_mmgbsa-out.csv":
                        file_path = os.path.join(f'./', filename)
                        data = pd.read_csv(file_path)
                    
                    # 필요한 데이터 추출
                        extract = data['r_psp_MMGBSA_dG_Bind'].iloc[0]
                        wr = csv.writer(f)
                        wr.writerow([filename,extract])

