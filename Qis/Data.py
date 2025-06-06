import pandas as pd
# Make sure the file path is correct
df = pd.read_excel('example.xlsx', engine='openpyxl')
print(df)
