import pandas as pd
import numpy as np

# Load the dataset
file_path = r"C:\Users\acer\Downloads\dataset-2.csv"  
df = pd.read_csv(file_path)

print("Columns in the DataFrame:", df.columns)

ids = pd.concat([df['id_start'], df['id_end']]).unique()

distance_matrix = pd.DataFrame(np.inf, index=ids, columns=ids)


np.fill_diagonal(distance_matrix.values, 0)


for _, row in df.iterrows():
    start = row['id_start'] 
    end = row['id_end']      
    distance = row['distance']   
    
  
    distance_matrix.loc[start, end] = min(distance_matrix.loc[start, end], distance)
    distance_matrix.loc[end, start] = min(distance_matrix.loc[end, start], distance)  # Ensure symmetry


for k in ids:
    for i in ids:
        for j in ids:
            if distance_matrix.loc[i, k] + distance_matrix.loc[k, j] < distance_matrix.loc[i, j]:
                distance_matrix.loc[i, j] = distance_matrix.loc[i, k] + distance_matrix.loc[k, j]

# Print the resulting distance matrix
print(distance_matrix)
