# 子模块：1.轮盘   2.反射器   3.插线板
UKW_B='YRUHQSLDPXNGOKMIEBFZCWVJAT'
Wheel_I='EKMFLGDQVZNTOWYHXUSPAIBRCJ'
Wheel_II='AJDKSIRUXBLHWTMCQGZNPYFVOE'
Wheel_III='BDFHJLCPRTXVZNYEIWGAKMUSQO'

# 旋转
# rotor_in:输入字母，输出字母
# rotor_out:输入字母，输出字母
class rotor(object):
    def __init__(self,table,position):
        self.position=ord(position)-ord('A')
        self.forward=dict()
        self.reverse=dict()
        for i,letter in enumerate(table):
            self.forward[chr(ord('A')+i)]=letter
            self.reverse[letter]=chr(ord('A')+i)
        # print(self.forward,'\n',self.reverse)
    def rotate(self):
        parent_rot=False
        self.position+=1
        if self.position>26:
            self.position-=26
            parent_rot=True
        return parent_rot
    def rotor_in(self,letter):
        offset=ord(letter)-ord('A')+self.position
        offset%=26
        letter=chr(ord('A')+offset)
        return self.forward[letter]
    def rotor_out(self,letter):
        offset=ord(letter)-ord('A')+self.position
        offset%=26
        letter=chr(ord('A')+offset)
        return self.reverse[letter]


# 反射是固定的，输入字母，输出字母
class reflector(object):
    def __init__(self,table):
        self.table = table
    def reflect(self,input):
        return self.table[ord(input)-ord('A')]

# 与第三个rotor相连接
class patch_panel(object):
    def __init__(self,pairs):
        pairs=pairs.upper().split()
        self.pairs=dict()
        for p in pairs:
            self.pairs[p[0]]=p[1]
            self.pairs[p[1]]=p[0]

    # panel_in:输入字母，输出偏移量
    def panel_in(self,input):
        return ord(self.getpair(input))-ord('A')

    # panel_out:输入偏移量，输出字母
    def panel_out(self,offset):
        return chr(self.getpair(chr(offset+ord('A'))))

    # 输入字母，输出字母
    def getpair(self,letter):
        if self.pairs.get(letter):
            return self.pairs[letter]
        else:
            return letter

def offset_print(*a):
    for offset in a:
        if isinstance(offset,str):
            print(offset)
        else:
            print(chr(ord('A')+offset))

def test_Enigma():
    panel=patch_panel('bq cr di ej kw mt os px uz gh')
    assert(panel.getpair('C')=='R')
    assert(panel.getpair('Z')=='U')
    r=reflector(UKW_B)
    assert(r.reflect('F')=='S')
    assert(r.reflect('G')=='L')
    rotor1=rotor(Wheel_I,'A')
    assert(rotor1.rotor_in('E')=='L')
    assert(rotor1.rotor_out('L')=='E')
    rotor2=rotor(Wheel_II,'A')
    assert(rotor2.rotor_in('W')=='F')
    assert(rotor2.rotor_in('Z')=='E')
    rotor3=rotor(Wheel_III,'D')
    assert(rotor3.rotor_in('P')=='G')
    assert(rotor3.rotor_out('J')=='V')

    
test_Enigma()

panel=patch_panel('')
r=reflector(UKW_B)
rotor1=rotor(Wheel_I,'A')
rotor2=rotor(Wheel_II,'A')
rotor3=rotor(Wheel_III,'A')
# encode
input='A'
rotor3.rotate()
a=panel.getpair(input)
print(a)
b=rotor3.rotor_in(a)
print(b)
c=rotor2.rotor_in(b)
print(c)
d=rotor1.rotor_in(c)
print(d)
e=r.reflect(d)
print(e)
f=rotor1.rotor_out(e)
print(f)
g=rotor2.rotor_out(f)
print(g)
h=rotor3.rotor_out(g)
print(h)
