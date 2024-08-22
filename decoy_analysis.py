
import pandas as pd

N = [50,60,70,80]
X = [2,4,6,8,10]

index_list = [67,108,131,148,168,181,196,208,238,247,293,295,316,317,347,412,433,479]#총 18개

dict_list = [{} for _ in range(18)]

positive_count = [[] for _ in range(5)]
negative_count = [[] for _ in range(5)]

for j in range(5):
            positive_count[j] = [0 for _ in range(270)]
            negative_count[j] = [0 for _ in range(270)]

for i in range(18):
    index = index_list[i]
    # CSV 파일 로드
    df = pd.read_csv(f'residue_scanning_sw_HER2_domain_act_Nb16_act_{index}_prep-out-results.csv')

    # 첫 번째 열의 데이터를 리스트로 변환
    mutant_list = df.iloc[:, 0].tolist()
    # delta affinity 열의 데이터를 리스트로 변환(교수님은 delta affinity coulmb쓰심?)
    delta_affinity_list = df.iloc[:, 1].tolist()
    mutation_list_ref = []
    if len(mutation_list_ref) !=270 and len(mutant_list) == 270 : mutant_list_ref = mutant_list

    # mutant_list_ref와 mutant_list 비교하여 mutant_list에 누락된 요소 추가
    for lack in range(len(mutant_list_ref)):
        if lack >= len(mutant_list) or mutant_list_ref[lack] != mutant_list[lack]:
            mutant_list = mutant_list[:lack] + [mutant_list_ref[lack]] + mutant_list[lack:]
            delta_affinity_list = delta_affinity_list[:lack] + [0] + delta_affinity_list[lack:]

    dict_list[i] = dict(zip(mutant_list_ref,delta_affinity_list))


for x in range(5):
    x_value = X[x]#2,4,6,8,10
    for i in range(18):
        index = 0
        for key,value in dict_list[i].items():
            if abs(value) > x_value:
                if value > 0: positive_count[x][index]+=1
                else: negative_count[x][index]+=1
            index += 1



for x in range(5):

    x_value = X[x]
    print(f"절대값 {x_value}와 비교하여 양수,음수 delta affinity 값의 개수가 18개의 결과들 중에서 6개 이하인 경우는 제외하였습니다.")    
    for i in range(270):
        if ((positive_count[x][i] <= 6) and (negative_count[x][i] <= 6)) : continue
        print(mutant_list_ref[i])
        print(f"양수 delta affinity 값이 절대값 {x_value}을 넘는 residue scanning 결과의 개수 : 18개 중 {positive_count[x][i]}개 ")
        print(f"음수 delta affinity 값이 절대값 {x_value}을 넘는 residue scanning 결과의 개수 : 18개 중 {positive_count[x][i]}개 ")
    print("========================================================================")


