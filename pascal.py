def gen(n, r=None):
    if r is None:
        r = []
    for x in range(n):
        length_r = len(r)
        r = [1 if i == 0 or i == length_r else r[i - 1] + r[i] for i in range(length_r + 1)]
        yield r

#hayo mau ngapain mau copas ya!!
#jangan sekali sekali sekali copas lu 
#yang copas tak daoin hidupnya sengsara 7 turunan
def draw(n):
    for p in gen(n):
        print(' '.join(map(str, p)).center(n * 2) + '\n')


def draw_beautiful(n):
    ps = list(gen(n))
    max_val = len(' '.join(map(str, ps[-1])))
    for p in ps:
        print(' '.join(map(str, p)).center(max_val) + '\n')

N = int(input("Jumlah baris segitiga pascal : "))

draw_beautiful(N)

import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)
mengetik('Script Ini Di Buat Oleh Hamzah')

hijau="33[0;32m"

import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)
mengetik('follow ig ku yak 👇')

import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)
mengetik(hijau+'@hamzah080208')

