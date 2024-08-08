#Nb49 cluster 4의 decoy를 분석하는 코드
import pandas as pd

N = [50,60,70,80]
X = [2,4,6,8,10]


dict_list = [{} for _ in range(4)]

positive_count = [[] for _ in range(5)]
negative_count = [[] for _ in range(5)]

for j in range(5):
            positive_count[j] = [0 for _ in range(272)]#18*15이고 2가 더해진 이유는 맨위 두행인 제목과 WT행 때문 
            negative_count[j] = [0 for _ in range(272)]

for i in range(1,5):

    # CSV 파일 로드
    df = pd.read_csv(f'residue_scanning_rf2_haddock_HER2_Nb49_cluster4_{i}.csv')

    # 첫 번째 열의 데이터를 리스트로 변환
    mutant_list = df.iloc[:, 0].tolist()

    # delta affinity 열의 데이터를 리스트로 변환(교수님은 delta affinity coulmb쓰심?)
    delta_affinity_list = df.iloc[:, 50].tolist()

    dict_list[i-1] = dict(zip(mutant_list,delta_affinity_list))

print()

result = [[[] for i in range(5)] for _ in range(4)]

for x in range(5):
    x_value = X[x]#2
    for i in range(4):
        index = 0
        for key,value in dict_list[i].items():
            if abs(value) > x_value:
                if value > 0: positive_count[x][index]+=1
                else: negative_count[x][index]+=1
            index += 1

print(positive_count)
print(negative_count)

