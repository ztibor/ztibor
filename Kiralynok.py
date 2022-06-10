import os
from random import *
# 1
class Tábla:
    # 3
    def __init__(self, c):
        self.__Urescella = c
        self.T = [[self.__Urescella for j in range(8)] for i in range(8)]
    # 4
    def Megjelenit(self):
        for i in range(8):
            for j in range(8):
                print(self.T[i][j], end='')
            print()
    # 5
    def Elhelyez(self, N):
        helyek = []
        for i in range(N):
            r = randint(0, 63)
            while r in helyek:
                r = randint(0, 63)
            helyek.append(r)
        for i in range(8):
            for j in range(8):
                if (i * 8 + j) not in helyek:
                    self.T[i][j] = self.__Urescella
                else:
                    self.T[i][j] = 'K'
    # 7
    def ÜresOszlop(self, o):
        osz = []
        for i in range(8):
            osz.append(self.T[i][o])
        if sum([1 for k in osz if k == 'K']) > 0:
            return False
        else:
            return True
    def ÜresSor(self, s):
        sor = []
        for j in range(8):
            sor.append(self.T[s][j])
        if sum([1 for k in sor if k == 'K']) > 0:
            return False
        else:
            return True
    # 8
    @property
    def ÜresOszlopokSzáma(self):
        db = 0
        for j in range(8):
            if self.ÜresOszlop(j):
                db += 1
        return db
    @property
    def ÜresSorokSzáma(self):
        db = 0
        for i in range(8):
            if self.ÜresSor(i):
                db += 1
        return db
# 4
sakk = Tábla('#')
print('4. feladat: Az üres tábla:')
sakk.Megjelenit()
# 6
print('\n6. feladat: A feltöltött tábla:')
sakk.Elhelyez(6)
sakk.Megjelenit()
# 9
print('\n9. feladat: Üres oszlopok és sorok száma:')
print(f'Oszlopok: {sakk.ÜresOszlopokSzáma}\nSorok: {sakk.ÜresSorokSzáma}')
# 10
out = 'tabla64.txt'
if os.path.isfile(out):
    os.remove(out)
out=open('tabla64.txt','w')
for i in range(64):
    t = Tábla('*')
    t.Elhelyez(i + 1)
    for i in range(8):
        s=""
        for j in range(8):
            s+=t.T[i][j]
        out.writelines(s+'\n')
    out.writelines('\n')