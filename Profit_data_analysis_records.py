import pandas as pd
from pprint import pprint
from collections import Counter

df = pd.read_excel(r"C:\Users\JagadeshP-Kairos\Downloads\500000_Records_Data1.xlsx")

ItemList1 = set(df["ItemType"].tolist())
print(len(ItemList1))
dict1 = {}
dict2 = {}
lst1 = []
out_list1 = []
for item in ItemList1:
    for idx, i in df.iterrows():
        if i["ItemType"] == item:
            # print(i["Country"])
            dict1.update({i["Country"]: i["TotalProfit"]})
            lst1.append(dict1)
            dict1 = {}
            dict2.update({i["ItemType"]: lst1})
    out_list1.append(dict2)
    lst1 = []
    dict2 = {}
# pprint(out_list1)

out_df = []
c_list = []
for items in out_list1:
    for i, data in enumerate(items.values()):
        for d in data:
            c_list.append(list(d.values())[0])
        sort_list = sorted(c_list, key=lambda x: float(x))
        peak_val = sort_list[-1]
        val_index = c_list.index(peak_val)
        c1 = list((data[val_index]).keys())[0]
        out_df.append([list(items.keys())[0], c1, peak_val])
        c_list = []
df1 = pd.DataFrame(out_df, columns=['ItemType', 'Country', 'TotalProfit'])
df2 = df1.groupby(['ItemType', 'Country']).first()
# print(df2)
df2.to_excel('profit_records_output_5lkhs.xlsx')
