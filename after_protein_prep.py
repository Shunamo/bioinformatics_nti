'''
protein_prep_script를 실행하면 현재폴더에 모든 파일이 생기므로, 모든 쓰레기 파일은 지우고 필요한 파일들은 HER2_Nb{Nb}/prep_files로 옮기는 스크립트
'''
import os
import shutil

directory = "./"

files = os.listdir(directory)


#log, nohtaeil로 시작하는 파일을 삭제하는 함수
def remove_trashes():
    for file in files:
        if file.endswith(".log") or file.startswith("nohtaeil"):
            file_path = os.path.join(directory, file)
            os.remove(file_path)

#prep_files로 파일들을 옮기는 함수
def move_to_prep_files():
    
    for Nb in [16,49,51]:
        target_directory = f"./HER2_Nb{Nb}/prep_files/"
    for file in files:
        if file.endswith("out.maegz"):
            source_path = os.path.join(directory, file)
            target_path = os.path.join(target_directory, file)

        # 파일 이동
        shutil.move(source_path, target_path)