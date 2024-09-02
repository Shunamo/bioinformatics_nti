'''
folder_generator.py를 사용하기 위한 함수
customizing 해서 folder_generator을 사용하면 된다.
'''

from folder_generator import folder_generator


domain_splits = [1,41,81,121,161]

for domain in domain_splits:

    for Nb_act in range(100,115):
        folder_generator("domain_split_Nb51",f"1N8Z_sw_haddock_HER2-domain-{domain}-split-pass_Nb51-{Nb_act}-act-rest-pass","/home/nohtaeil/Desktop","tinoh@203.249.75.23","40020","/home/tinoh")