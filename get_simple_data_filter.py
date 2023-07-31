import pandas as pd
from pprint import pprint
from collections import Counter

# df = pd.read_excel(r"C:\Users\JagadeshP-Kairos\Downloads\500_Records_Data1.xlsx")
# category = "ItemType"
# output_var = "Country"
# sort_by = "UnitsSold"
# ItemList1 = set(df[category].tolist())


def data_filter(req_body):
    file_path = str(req_body.get("FilePath"))
    category = str(req_body.get("Category"))
    output_var = str(req_body.get("OutputVar"))
    sort_by = str(req_body.get("SortBy"))
    subset_size = req_body.get("SubsetSize", 3)
    subset_types = req_body.get("SubsetTypes", ["Top"])

    if file_path.split('.')[-1] == 'csv':
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)
    item_list1 = set(df[category].tolist())
    print(len(item_list1))
    dict1 = {}
    dict2 = {}
    lst1 = []
    out_list1 = []
    for item in item_list1:
        for idx, i in df.iterrows():
            if i[category] == item:
                # print(i[output_var])
                dict1.update({i[output_var]: i[sort_by]})
                lst1.append(dict1)
                dict1 = {}
                dict2.update({i[category]: lst1})
        out_list1.append(dict2)
        lst1 = []
        dict2 = {}
    # print(out_list1)
    
    out_df = []
    c_list = []
    n = subset_size
    top_list = []
    for st in subset_types:
        if st == "Top":
            reverse = bool(True)
            for items in out_list1:
                for idx, data in enumerate(items.values()):
                    for d in data:
                        c_list.append(list(d.values())[0])
                    sort_list = sorted(c_list, reverse=reverse)
                    top_list = sort_list[0:n]
                    for i in top_list:
                        val_index = c_list.index(i)
                        c1 = list((data[val_index]).keys())[0]
                        out_df.append([st, list(items.keys())[0], c1, i])
                c_list = []
        if st == "Bottom":
            reverse = bool(False)
            for items in out_list1:
                for idx, data in enumerate(items.values()):
                    for d in data:
                        c_list.append(list(d.values())[0])
                    sort_list = sorted(c_list, reverse=reverse)
                    top_list = sort_list[0:n]
                    for i in top_list:
                        val_index = c_list.index(i)
                        c1 = list((data[val_index]).keys())[0]
                        out_df.append([st, list(items.keys())[0], c1, i])
                c_list = []
        if st == "Middle":
            for items in out_list1:
                for idx, data in enumerate(items.values()):
                    for d in data:
                        c_list.append(list(d.values())[0])
                    sort_list = sorted(c_list, reverse=True)
                    strt_idx = (len(sort_list) // 2) - (n // 2)
                    end_idx = (len(sort_list) // 2) + (n // 2)
                    # top_list = sort_list[strt_idx:end_idx]
                    for idx in range(len(sort_list)):
                        # checking for elements in range
                        if idx >= strt_idx and idx <= end_idx:
                            top_list.append(sort_list[idx])
                    for i in top_list:
                        val_index = c_list.index(i)
                        c1 = list((data[val_index]).keys())[0]
                        out_df.append([st, list(items.keys())[0], c1, i])
                c_list = []
                top_list = []
    df1 = pd.DataFrame(out_df, columns=["SubsetType", category, output_var, sort_by])
# df2 = df1.groupby(['ItemType', 'Country']).all()
    df1.to_excel('get_simple_data_filter_1.xlsx')
    print(df1)
    return out_df

# print(data_filter())
