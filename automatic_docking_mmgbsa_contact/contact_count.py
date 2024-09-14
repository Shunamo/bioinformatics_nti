'''
contact 파일을 토대로 contact결과를 정리하는 함수

template> python3 mmgbsa_score_collector.py project_title number_of_files
'''

import pandas as pd
import os
import csv
import sys
def contact_count(project_title,number_of_files):

    with open(f"{project_title}_collected_contact_count.csv",'w',newline='') as f:

        for i in range(1, number_of_files+1):
            for filename in os.listdir("./"):
                if filename == f"{project_title}_emref_{i}_prep-out_contact.csv":
                    file_path = os.path.join("./", filename)
                    df = pd.read_csv(file_path, usecols=[0], header=None)  # 첫 번째 열만 읽기
                    unique_values = df[0].drop_duplicates().to_list()
                    unique_values = unique_values[1:]
                    wr = csv.writer(f)
                    wr.writerow([filename,unique_values])


if __name__ == "__main__":
    
    project_title = sys.argv[1]
    number_of_files = sys.argv[2]
    contact_count(project_title,int(number_of_files))