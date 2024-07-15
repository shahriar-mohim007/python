import pandas as pd

df = pd.read_excel('Recover_54.xlsx')

# Add a new column 'status' with a default value
df['status'] = 'Pending'
df.to_excel('Recover_54.xlsx', index=False)
print(df.head())