# 反射是固定的，输入偏移量，输出偏移量
class reflector(object):
    def __init__(self, table):
        self.table = list(range(26))
        for i in range(26):
            self.table[i] = ord(table[i])-ord('A')

    def reflect(self, offset_in):
        return self.table[offset_in]
