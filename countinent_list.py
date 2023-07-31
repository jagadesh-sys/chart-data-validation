import pandas as pd

path = r"C:\Users\JagadeshP-Kairos\Downloads\New Microsoft Excel Worksheet (2).xlsx"

df = pd.read_excel(path)

df1 = (df["Continent"]).tolist()
print(len(df1))
out = set(df1)
print(out)
print(len(out))