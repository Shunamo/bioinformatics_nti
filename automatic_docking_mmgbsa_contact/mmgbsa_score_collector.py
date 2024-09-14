'''
mmgbsa 결과를 정리하여 하나의 파일로 만드는 프로그램

template> python3 mmgbsa_score_collector.py project_title sampling
예시> python3 mmgbsa_score_collector.py sw_HER2_Nb51_docking 50
'''
import pandas as pd
import os
import csv
import sys


def mmgbsa_score_collector(project_title,sampling):
    f = open(f"{project_title}_collected_mmgbsa_score.csv",'w')

    with open(f"{project_title}_collected_mmgbsa_score.csv",'a',newline='') as f:
        for i in range(1,sampling+1):
            for filename in os.listdir(f'./'):
                if filename == f"{project_title}_emref_{i}_prep-out_prime_mmgbsa-out.csv":
                    file_path = os.path.join(f'./', filename)
                    data = pd.read_csv(file_path)
                
                # 필요한 데이터 추출
                    extract = data['r_psp_MMGBSA_dG_Bind'].iloc[0]
                    wr = csv.writer(f)
                    wr.writerow([filename,extract])

if __name__ == "__main__":
    
    project_title = sys.argv[1]
    sampling = int(sys.argv[2])
    mmgbsa_score_collector(project_title,sampling)