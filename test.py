import json

fpath='sheet.json'
# 输入数据链并破解
cl=[9,4,9,4]
####################################
cl.sort()
with open(fpath,'r') as f:
    sheet_json=f.readline()
    sheet=json.loads(sheet_json)
for chain_len in sheet.keys():
    if sheet[chain_len]==cl:
        print(chain_len)
