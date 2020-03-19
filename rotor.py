# 旋转
# rotor_in:输入偏移量，输出偏移量
# rotor_out:输入偏移量，输出偏移量
class rotor(object):
    def __init__(self,wheel,position):
        table,Turnover=wheel
        self.Turnover=ord(Turnover)-ord('A')
        self.position=ord(position)-ord('A')
        self.forward=list(range(26))
        self.reverse=list(range(26))
        for i,letter in enumerate(table):
            self.forward[i]=ord(letter)-ord('A')
            self.reverse[ord(letter)-ord('A')]=i
        # print(self.forward,'\n',self.reverse)
    def rotate(self):
        parent_rot=False
        if self.position==self.Turnover:
            parent_rot=True
        self.position=(self.position+1)%26
        return parent_rot
    def middle_rotate(self,fast_result):
        if fast_result or self.position==self.Turnover:
            return self.rotate()

    def rotor_in(self,offset_in):
        offset_in=(offset_in+self.position)%26
        offset_out=(self.forward[offset_in]-self.position)%26
        return offset_out
    def rotor_out(self,offset_in):
        offset_in=(offset_in+self.position)%26
        offset_out=(self.reverse[offset_in]-self.position)%26
        return offset_out