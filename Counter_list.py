from collections import Counter
import ast
# z = ['blue', 'red', 'red', 'yellow', 'yellow', 'red']
# c = Counter(z)
# c_dict = (dict(c))
# a = sorted(c.items(), key=lambda x: x[1], reverse=True)
# print(a)
# for key, values in c_dict.items():
#     print(key)
# z.reverse()
# print(z)
# print(z)
# print(z[:3])

# l1 = [1.7, 3.5, 1.1, 2.2, 2.1]
# l1 = [3,2,4,1]
# l1.sort(key=float)
# s1 = set(l1)
# l2 = l1[0:3]
# print(l2)
# # Import pandas library
# import pandas as pd

# # initialize list of lists
# data = [['Geeks', 10, 1.8], ['for', 15, 2.8], ['geeks', 20, 2.7]]
#
# # Create the pandas DataFrame
# df = pd.DataFrame(data, columns=['Name', 'Age', 'other'])
#
# # print dataframe.
# print(df)

# Python3 code to demonstrate working of
# K middle elements
# Using loop

# initializing list
test_list = [9917, 9878, 9804, 9470, 9389, 9119, 9021, 7890, 6329, 6181, 6055, 5881, 5849, 5531, 5523, 5475, 4674, 4518, 4454, 4378, 3852, 3714, 3691, 3578, 3449, 3082, 3077, 2891, 2683, 2570, 2462, 2236, 2050, 1847, 1747, 1324, 1142, 274, 175, 11]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# computing strt, and end index
strt_idx = (len(test_list) // 2) - (K // 2)
end_idx = (len(test_list) // 2) + (K // 2)

# using loop to get indices
res = []
for idx in range(len(test_list)):

    # checking for elements in range
    if idx >= strt_idx and idx <= end_idx:
        res.append(test_list[idx])

# printing result
print("Extracted elements list : " + str(res))
