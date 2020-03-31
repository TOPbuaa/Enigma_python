import json
from break_enigma import get_chain_len
from break_enigma import key_rotate

fpath='sheet.json'
# 输入数据链并破解
#####################
# 例：secret_key='I,II,III,AAA'
cl1=[9,4,9,4]
cl2=[2, 2, 5, 5, 6, 6]
cl3=[3, 3, 4, 4, 6, 6]
##################
# # 课件上例子，无解
# cl1=[3,9,7,7]
# cl2=[2,3,9,12]
# cl3=[5,5,5,3,8]
####################################
# 输入链条长度数组，输出可能密钥
cl1.sort()
cl2.sort()
cl3.sort()
with open(fpath,'r') as f:
    sheet_json=f.readline()
    sheet=json.loads(sheet_json)
for secret_key in sheet.keys():
    if sheet[secret_key]==cl1:
        key2=key_rotate(secret_key)
        if sheet[key2]==cl2:
            key3=key_rotate(key2)
            if sheet[key3]==cl3:
                print(secret_key,key2,key3)

####################################
# # 获取测试数据
# wheel=('I','II','III')
# chars=('A','A','A')
# chain_len=get_chain_len(wheel,chars[0],chars[1],chars[2])
# print(chain_len)

# wheel=('I','II','III')
# chars=('A','A','B')
# chain_len=get_chain_len(wheel,chars[0],chars[1],chars[2])
# print(chain_len)

# wheel=('I','II','III')
# chars=('A','A','C')
# chain_len=get_chain_len(wheel,chars[0],chars[1],chars[2])
# print(chain_len)