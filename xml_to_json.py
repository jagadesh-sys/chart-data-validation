import json
import xmltodict
from pprint import pprint

with open(r"C:\Users\JagadeshP-Kairos\Downloads\test_training_dataset\0a0a66e55c96ffd21f3e362e3fbbc816_Y29udGVudC5kaWdpdGFsLm5ocy51awkxOTQuMTg5LjI3LjI4-1-0.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())

json_data = json.dumps(data_dict)
pprint(data_dict)
# print(json_data)