import pandas as pd
import os
import csv
all_unique_values = pd.Series(dtype=object)  # 초기 시리즈 생성, 적절한 데이터 타입 지정


f = open(f"Nb51_contact_count.csv",'w')

with open(f"Nb51_contact_count.csv",'a',newline='') as f:

    for i in range(1, 501):
        for filename in os.listdir("./"):
            if filename == f"sw_HER2_domain_act_Nb51_act_{i}_prep-out_contact.csv":
                file_path = os.path.join("./", filename)
                df = pd.read_csv(file_path, usecols=[0], header=None)  # 첫 번째 열만 읽기
                unique_values = df[0].drop_duplicates().to_list()
                unique_values = unique_values[1:]
                wr = csv.writer(f)
                wr.writerow([filename,unique_values])
