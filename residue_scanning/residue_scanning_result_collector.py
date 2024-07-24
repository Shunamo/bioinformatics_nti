import pandas as pd
import os

Nb16_csv_files = [f'residue_scanning_HER2_Nb16_pose_{i+1}-results.csv' for i in range(30)]
Nb49_csv_files = [f'residue_scanning_HER2_Nb49_pose_{i+1}-results.csv' for i in range(30)]
Nb51_csv_files = [f'residue_scanning_HER2_Nb51_pose_{i+1}-results.csv' for i in range(30)]

csv_dict = {
    16 : Nb16_csv_files,
    49 : Nb49_csv_files,
    51 : Nb51_csv_files
}


merged_df = pd.DataFrame()

for Nb in [16,49,51]:
    for i, file in enumerate(csv_dict[Nb]):
        try:
            df = pd.read_csv(file)
            # 1, 2열 추출 (0-indexed이므로 첫 번째 열은 0, 두 번째 열은 1)
            selected_columns = df.iloc[:, [0, 1]]

            selected_columns.columns = [f'pose_{i+1}_mutations', f'pose_{i+1}_delta_affinity']

            if merged_df.empty:
                merged_df = selected_columns
            else:
                merged_df = pd.concat([merged_df, selected_columns], axis=1)
        except:
            pass

    merged_df.to_csv(f'residue_scanning_Nb{Nb}_output.csv', index=False)

