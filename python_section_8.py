import pandas as pd

df = pd.read_csv(r"C:\Users\acer\Downloads\dataset-1.csv")
print(df.head())
df['startDay'] = pd.to_datetime(df['startDay'], errors='coerce')
df['endDay'] = pd.to_datetime(df['endDay'], errors='coerce')
df['startDay'] = pd.to_datetime(df['startDay'], format='%d-%m-%Y', errors='coerce')
df['endDay'] = pd.to_datetime(df['endDay'], format='%d-%m-%Y', errors='coerce')
print(df[df['startDay'].isna() | df['endDay'].isna()])
