import pandas as pd
from pprint import pprint
from collections import Counter

df = pd.read_excel(r"C:\Users\JagadeshP-Kairos\Downloads\500000_Records_Data1.xlsx")

ItemList1 = set(df["ItemType"].tolist())
print(len(ItemList1))
dict1 = {}
lst1 = []
outlist1 = []
for item in ItemList1:
    for idx, i in df.iterrows():
        if i["ItemType"] == item:
            # print(i["Country"])
            lst1.append(i["Country"])
            dict1.update({i["ItemType"]: lst1})
    outlist1.append(dict1)
    dict1 = {}
    lst1 = []

final_dict = {}
final_list = []
for i in outlist1:
    for countries in i.values():
        c = max(countries, key=countries.count)
        final_dict.update({list(i.keys())[0]: c})
        # final_list.append(final_dict)
df1 = pd.DataFrame.from_dict(final_dict.items())
df1.columns = ['ItemType', 'countries']
# final_dict = {}
# print(df1)
df1.to_excel("5lkh_records_final_output.xlsx", index=False)
