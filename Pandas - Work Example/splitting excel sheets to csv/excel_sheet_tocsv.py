import pandas as pd
df = pd.read_excel('MMAC_RS_Post_Process.xlsx', sheet_name=None)
print(df)
for key in df.keys():
    df[key].to_csv('%s.csv' %key)