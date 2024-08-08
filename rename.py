import os
directory = './'
files = os.listdir(directory)

pose_num = [i for i in range(1,31)]
        
for i in range(1,31):
    for filename in files:
        old_path = os.path.join(directory, filename)
        if filename == f"HER2_Nb49_pose_{i}-out.maegz":
            new_filename = f"HER2_Nb49_pose_{i}.maegz"
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path,new_path)
