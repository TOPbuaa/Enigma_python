from Enigma import *
import json
from itertools import permutations

# 输入设置，输出链条长度数组
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

# 输入设置，输出旋转一次后的状态
#######################################################
def key_rotate(keys):
    # key="I,II,III,AAA" #test
    keys=keys.split(',')
    wheel=keys[0:3]
    chars=keys[3]
    W=[]
    for i in range(3):
        W.append(globals()['Wheel_'+wheel[i]]) 
    e = Enigma([W[0],W[1],W[2]], [chars[0], chars[1], chars[2]],
            UKW_B, '')
    e.single_code('A') #任意都可，目的是让其旋转一次
    char1=chr(ord('A')+e.rotor1.position)
    char2=chr(ord('A')+e.rotor2.position)
    char3=chr(ord('A')+e.rotor3.position)
    return wheel[0]+','+wheel[1]+','+wheel[2]+','+char1+char2+char3
if __name__ == "__main__":
    # 生成表格
    sheet=dict()
    list_wheel=list(permutations(['I', 'II', 'III'],3))
    # print(list_wheel,len(list_wheel))
    for wheel in list_wheel:
        for i1 in range(26):
            char1=chr(i1+ord('A'))
            for i2 in range(26):#26
                char2=chr(i2+ord('A'))
                for i3 in range(26):#26
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



