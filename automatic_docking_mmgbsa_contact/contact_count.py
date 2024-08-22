import pandas as pd
import os
import csv
import sys
def contact_count(project_title):
    f = open(f"{project_title}_collected_contact_count.csv",'w')

    with open(f"{project_title}_collected_contact_count.csv",'a',newline='') as f:

        for i in range(1, 101):
            for filename in os.listdir("./"):
                if filename == f"{project_title}_emref_{i}_prep-out_contact.csv":
                    file_path = os.path.join("./", filename)
                    df = pd.read_csv(file_path, usecols=[0], header=None)  # 첫 번째 열만 읽기
                    unique_values = df[0].drop_duplicates().to_list()
                    unique_values = unique_values[1:]
                    wr = csv.writer(f)
                    wr.writerow([filename,unique_values])


if __name__ == "__main__":
    #python3 mmgbsa_score_collector.py project_title
    project_title = sys.argv[1]
    contact_count(project_title)