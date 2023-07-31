import os
import json

# Opening JSON file
f = open('data.json')

data = json.load(f)

for i in data['emp_details']:
    print(i)

# path_dir = r"C:\Users\JagadeshP-Kairos\Downloads\bardata(1031)\bardata(1031)\bar\images"
#
# for (root,dirs,files) in os.walk(path_dir, topdown=True):
#     print(root,dirs,files)
#     exit()
