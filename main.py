# from Enigma import Enigma
from Enigma import *

import time

# speed test
e = Enigma([Wheel_V, Wheel_I, Wheel_III], ['A', 'Q', 'L'],
           UKW_B, 'bq cr di ej kw mt os px uz gh')
t1 = time.time()
# 10MBytes
for _ in range(1000_000):
    e.code('HELLOWORLD')
t2 = time.time()
print(t2-t1)
