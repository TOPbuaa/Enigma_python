from Enigma import *
import json
from itertools import permutations

# secret_key='I,II,III,AAA'
######################################################################
def get_chain_len(wheel,char1,char2,char3):
    pairs=dict()
    Wheel=[]
    for i in range(3):
        Wheel.append(globals()['Wheel_'+wheel[i]])
    # print(Wheel)
    for i in range(26):
        char=chr(i+ord('A'))
        e = Enigma([Wheel[0],Wheel[1],Wheel[2]], [char1, char2, char3],
            UKW_B, '')
        c1=e.single_code(char)
        e.code('AA')
        c4=e.single_code(char)
        pairs[c1]=c4
    chain_len=[]
    while len(pairs)!=0:
        l=0
        char=next (iter (pairs.values()))
        next_char=char
        while True:
            l+=1
            next_char=pairs.pop(next_char)
            if next_char==char:
                break
        chain_len.append(l)
    chain_len.sort()
    return chain_len
    # # 遇到问题，list是可变变量，不能作为key
    # # 用tuple或干脆用secret_key做为key，遍历找答案
    # if chain_len in sheet:
    #     sheet[chain_len]=sheet[chain_len].append(key)
    # else:
    #     sheet[chain_len]=[key]
############################################################################

# 生成表格
sheet=dict()
list_wheel=list(permutations(['I', 'II', 'III'],3))
# print(list_wheel,len(list_wheel))
for wheel in list_wheel:
    for i1 in range(26):
        char1=chr(i1+ord('A'))
        for i2 in range(2):#26
            char2=chr(i2+ord('A'))
            for i3 in range(2):#26
                char3=chr(i3+ord('A'))
                secret_key=''
                for i in range(3):
                    secret_key+=wheel[i]+','
                secret_key+=char1+char2+char3
                chain_len=get_chain_len(wheel,char1,char2,char3)
                sheet[secret_key]=chain_len
# 将表格保存到文件
fpath='sheet.json'
with open(fpath,'w') as f:
    f.write(json.dumps(sheet))
########################################################################################



