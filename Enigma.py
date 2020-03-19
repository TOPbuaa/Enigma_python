# 子模块：1.轮盘   2.反射器   3.插线板
from patch_panel import patch_panel
from rotor import rotor
from reflector import reflector
UKW_B='YRUHQSLDPXNGOKMIEBFZCWVJAT'
Wheel_I=('EKMFLGDQVZNTOWYHXUSPAIBRCJ','Q')
Wheel_II=('AJDKSIRUXBLHWTMCQGZNPYFVOE','E')
Wheel_III=('BDFHJLCPRTXVZNYEIWGAKMUSQO','V')
Wheel_IV=('ESOVPZJAYQUIRHXLNFTGKDCMWB','J')
Wheel_V=('VZBRGITYUPSDNHLXAWMJQOFECK','Z')

def offset_print(*a):
    for offset in a:
        if isinstance(offset,str):
            print(offset)
        else:
            print(chr(ord('A')+offset))
def get_offset(letter):
    return ord(letter)-ord('A')

class Enigma(object):
    def __init__(self,wheel,position,ref,pairs):
        self.panel=patch_panel(pairs)
        self.reflector=reflector(ref)
        self.rotor1=rotor(wheel[0],position[0])
        self.rotor2=rotor(wheel[1],position[1])
        self.rotor3=rotor(wheel[2],position[2])
    def single_code(self,input):
        fast_result=self.rotor3.rotate()
        if self.rotor2.middle_rotate(fast_result):
            self.rotor1.rotate()
        a=self.panel.panel_in(input)
        b=self.rotor3.rotor_in(a)
        c=self.rotor2.rotor_in(b)
        d=self.rotor1.rotor_in(c)
        e=self.reflector.reflect(d)
        f=self.rotor1.rotor_out(e)
        g=self.rotor2.rotor_out(f)
        h=self.rotor3.rotor_out(g)
        return self.panel.panel_out(h)
    def code(self,sin):
        sin=sin.upper()
        sout=''
        for c in sin:
            sout+=self.single_code(c)
        return sout

if __name__ == "__main__":
    e=Enigma([Wheel_V,Wheel_I,Wheel_III] , ['A','Q','L'] , UKW_B , 'bq cr di ej kw mt os px uz gh')
    plaintext='boot klar x bei j schnoor j etwa zwo siben x nov x sechs nul cbm x proviant bis zwo nul x dez x benoetige glaeser y noch vier klar x stehe marqu bruno bruno zwo funf x lage wie j schaefer j x nnn www funf y eins funf mb steigend y gute sicht vvv j rasch'.upper().replace(' ','')
    ciphertext='xuchl dxqpn qczqg akjrm vyeei jpsch kxflf qncvl octfq bjcyt jwesa qbzwo rpccp ipfzz uyvoa dnwcn kmjos pfeos hruob rlppz joicd xktlz gtuyn pzioy djejm ertbf khhsm zmwaj ggwtd lbnoq mpcpn gsrkh ftgii gsbwr jyyqp bvjiz blnlj sgbme eolqg g'.upper().replace(' ','')
    # assert(ciphertext==e.code(plaintext))
    for i in range(len(plaintext)):
        ci=e.single_code(plaintext[i])
        # print(plaintext[i],ciphertext[i],ci)
        assert(ci==ciphertext[i])
