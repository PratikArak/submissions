import pandas as pd
import numpy as np

file_path = "C:\\Users\\acer\\Downloads\\dataset-2.csv"
df = pd.read_csv(file_path)

ids = pd.concat([df['id_start'], df['id_end']]).unique()


distance_matrix = pd.DataFrame(np.inf, index=ids, columns=ids)


for _, row in df.iterrows():
    distance_matrix.loc[row['id_start'], row['id_end']] = row['distance']
    distance_matrix.loc[row['id_end'], row['id_start']] = row['distance']  

for k in ids:
    for i in ids:
        for j in ids:
            if distance_matrix.loc[i, k] < np.inf and distance_matrix.loc[k, j] < np.inf:
                distance_matrix.loc[i, j] = min(distance_matrix.loc[i, j], distance_matrix.loc[i, k] + distance_matrix.loc[k, j])


def unroll_distance_matrix(distance_matrix):
   
    results = []

    
    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            if id_start != id_end: 
                distance = distance_matrix.loc[id_start, id_end]
                if distance != np.inf: 
                    results.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})
    result_df = pd.DataFrame(results)

    return result_df


result_df = unroll_distance_matrix(distance_matrix)

print(result_df)
