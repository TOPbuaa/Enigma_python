# 子模块：1.轮盘   2.反射器   3.插线板
UKW_B='YRUHQSLDPXNGOKMIEBFZCWVJAT'
Wheel_I='EKMFLGDQVZNTOWYHXUSPAIBRCJ'
Wheel_II='AJDKSIRUXBLHWTMCQGZNPYFVOE'
Wheel_III='BDFHJLCPRTXVZNYEIWGAKMUSQO'

# 旋转
# rotor_in:输入偏移量，输出偏移量
# rotor_out:输入偏移量，输出偏移量
class rotor(object):
    def __init__(self,table,position):
        self.position=ord(position)-ord('A')
        self.forward=list(range(26))
        self.reverse=list(range(26))
        for i,letter in enumerate(table):
            self.forward[i]=ord(letter)-ord('A')
            self.reverse[ord(letter)-ord('A')]=i
        # print(self.forward,'\n',self.reverse)
    def rotate(self):
        parent_rot=False
        self.position+=1
        if self.position>26:
            self.position-=26
            parent_rot=True
        return parent_rot
    def rotor_in(self,offset_in):
        offset_in=(offset_in+self.position)%26
        offset_out=(self.forward[offset_in]-self.position)%26
        return offset_out
    def rotor_out(self,offset_in):
        offset_in=(offset_in+self.position)%26
        offset_out=(self.reverse[offset_in]-self.position)%26
        return offset_out


# 反射是固定的，输入偏移量，输出偏移量
class reflector(object):
    def __init__(self,table):
        self.table=list(range(26))
        for i in range(26):
            self.table[i]=ord(table[i])-ord('A')
    def reflect(self,offset_in):
        return self.table[offset_in]

# 与第三个rotor相连接
class patch_panel(object):
    def __init__(self,pairs):
        pairs=pairs.upper().split()
        self.pairs=dict()
        for p in pairs:
            self.pairs[p[0]]=p[1]
            self.pairs[p[1]]=p[0]

    # panel_in:输入字母，输出偏移量
    def panel_in(self,letter_in):
        offset_out=ord(self.getpair(letter_in))-ord('A')
        return offset_out

    # panel_out:输入偏移量，输出字母
    def panel_out(self,offset_in):
        letter_out=self.getpair(chr(offset_in+ord('A')))
        return letter_out

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
def get_offset(letter):
    return ord(letter)-ord('A')

def test_panel():
    panel=patch_panel('bq cr di ej kw mt os px uz gh')
    assert(panel.panel_in('C')==get_offset('R'))
    assert(panel.panel_out(get_offset('Z'))=='U')
def test_reflect():
    r=reflector(UKW_B)
    assert(r.reflect(get_offset('F'))==get_offset('S'))
    assert(r.reflect(get_offset('G'))==get_offset('L'))
def test_rotor():
    rotor1=rotor(Wheel_I,'A')
    assert(rotor1.rotor_in(get_offset('D'))==get_offset('F'))
    assert(rotor1.rotor_out(get_offset('S'))==get_offset('S'))
    rotor2=rotor(Wheel_II,'A')
    assert(rotor2.rotor_in(get_offset('C'))==get_offset('D'))
    assert(rotor2.rotor_out(get_offset('S'))==get_offset('E'))
    rotor3=rotor(Wheel_III,'I')
    assert(rotor3.rotor_in(get_offset('C'))==get_offset('P'))
    assert(rotor3.rotor_out(get_offset('O'))==get_offset('J'))

    
test_rotor()
test_panel()
test_reflect()


panel=patch_panel('')
r=reflector(UKW_B)
rotor1=rotor(Wheel_I,'Z')
rotor2=rotor(Wheel_II,'H')
rotor3=rotor(Wheel_III,'C')
# encode
input='H'
rotor3.rotate()
a=panel.panel_in(input)
offset_print(a)
b=rotor3.rotor_in(a)
offset_print(b)
c=rotor2.rotor_in(b)
offset_print(c)
d=rotor1.rotor_in(c)
offset_print(d)
e=r.reflect(d)
offset_print(e)
f=rotor1.rotor_out(e)
offset_print(f)
g=rotor2.rotor_out(f)
offset_print(g)
h=rotor3.rotor_out(g)
offset_print(h)
out=panel.panel_out(h)
print(out)
