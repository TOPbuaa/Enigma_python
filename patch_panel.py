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