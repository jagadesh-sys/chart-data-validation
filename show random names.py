from flask import Flask, request, jsonify
import pandas as pd
import random

df = pd.read_excel(r"C:\Users\JagadeshP-Kairos\Downloads\df.xlsx")
n = int(input("Enter the number of names to display: "))
country = str(input("Enter the country: "))
name_df = []
for idx, i in df.iterrows():
    if i["Origin"] == country:
        name_df.append(i["Name"])
set_names = list(set(name_df))
result_name = random.sample(set_names, k=n)
for r in result_name:
    print(r)
