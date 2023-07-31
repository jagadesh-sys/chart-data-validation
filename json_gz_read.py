# import json
# import gzip
# with gzip.open(r"C:\Users\JagadeshP-Kairos\PycharmProjects\pythonProject\venv\Lib\site-packages\spellchecker\resources\en.json.gz") as f:
#     data = f.read() # returns a byte string `b'`
# json.loads(data)
# import random
# for i in range(0,6619):
#     num1 = random.randint(0, 100)
#     print(num1)

{
"Count" : 20,
	"DataType" : "Complex",
	"Entity" : "Person",
	"EntityStructure" : [
		{
			"Label" : "Customer Name",
			"Entity" : "Full Name",
			"Properties" : [
				{"Key" : "Locale",
				"Value" : "US"}	
			]
		},
{
			"Label" : "Gender",
			"Entity" : "List",
			"Properties" : [],
			"ListItems" : ["Green","Blue"]
		},

		 {
			"Label" : "Age",
			"Entity" : "Integer",
			"Properties" : [
				{"Key" : "Min Value",
				"Value" : "18"},
				{"Key" : "Max Value",
				"Value" : "108"},
			]
		}, 	
		]	
	}
