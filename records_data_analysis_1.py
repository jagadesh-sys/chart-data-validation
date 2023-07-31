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
            dict1.update({i["Country"]: i["TotalCost"]})
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
    for data in list(items.values()):
        for d in data:
            c_list.append(list(d.keys())[0])
        c = Counter(c_list)
        c_dict = (dict(c))
        a = sorted(c_dict.items(), key=lambda x: x[1], reverse=True)
        rev_list = list(a)
        for c1, count in rev_list[:3]:
            for d in data:
                for k, v in d.items():
                    if k == c1:
                        cost = v
            out_df.append([list(items.keys())[0], c1, cost])
        c_dict = []
        c_list = []
df1 = pd.DataFrame(out_df, columns=['ItemType', 'Country', 'Values'])
df2 = df1.groupby(['ItemType', 'Country']).first()
df2.to_excel('records_output_5lkhs_1.xlsx')
# print(df2)
# print(df1)


# out_df = []
# for items in out_list1:
#     for data in list(items.values())[0]:
#         out_df.append([list(items.keys())[0], list(data.keys())[0], list(data.values())[0]])
# # print(out_list1)

# final_dict = {}
# final_list = []
# for i in outlist1:
#     for countries in i.values():
#         c = Counter(countries)
#         final_dict.update({list(i.keys())[0]: c})
#         # final_list.append(final_dict)
# df1 = pd.DataFrame.from_dict(z.items())
# print(df1)
# df1.columns = ['ItemType', 'countries']
# # final_dict = {}
# # print(df1)
# df1.to_excel("5lkh_records_final_output.xlsx", index=False)
