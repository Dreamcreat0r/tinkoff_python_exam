from itertools import *

n, k = input().split()
n = int(n)
k = int(k)
perestanovki = []
mass = []
krasivo = 0

for i in range(n):
    mass.append(i+1)

for item in permutations(mass):
    perestanovki.append(item)

for elem in perestanovki:
    i=1
    krasota = 0
    for numb in elem:
        krasota += numb*i
        i+=1
    if krasota%k == 0:
        krasivo +=1

print(krasivo)
