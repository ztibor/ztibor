#kifejezesek.txt
#500 mod 265
# 0   1   2
class Kif:
    def __init__(self,sor):
        s=sor.strip().split()
        self.opus1=int(s[0])
        self.oper=s[1]
        self.opus2=int(s[2])
    #6
    def Value(self):
        if not (self.oper in operok):
            return 'Hibás operátor'
        elif self.opus2==0 and (self.oper=='div' or self.oper=='/' or self.oper=='mod'):
            return 'Egyéb hiba!'
        elif self.oper=='+':
            return self.opus1+self.opus2
        elif self.oper == '-':
            return self.opus1 - self.opus2
        elif self.oper == '*':
            return self.opus1 * self.opus2
        elif self.oper == '/':
            return self.opus1 / self.opus2
        elif self.oper == 'div':
            return self.opus1 // self.opus2
        else:
            return self.opus1 % self.opus2
#1
with open('kifejezesek.txt',encoding='latin2') as f:
    lista=[Kif(k) for k in f]

#2
print(f'2. feladat: Kifejezések száma: {len(lista)}')

#3
print(f'3. feladat: Kifejezések maradékos osztással: {len([k for k in lista if k.oper=="mod"])}')

#4
van=False
i=0
while i<len(lista) and not van:
    van=lista[i].opus1 %10==0 and lista[i].opus2 %10==0
    i+=1
if van:
    print('4. feladat: Van ilyen kifejezés!')
else:
    print('4. feladat: Nincs ilyen kifejezés!')

#5
operok=['+','-','*','/','div','mod']
stat=dict()
for k in lista:
    if k.oper in operok:
        stat[k.oper]=stat.get(k.oper,0)+1
print('5. feladat: Statisztika')
[print(f'\t{k:>5} -> {stat[k]} db') for k in stat.keys()]

#7
while True:
    inp=input('7. feladat: Kérek egy kifejezést (pl.: 1 + 1): ')
    if inp.strip()=='vége':
        break
    else:
        expr=Kif(inp)
        print(f'\t{expr.opus1} {expr.oper} {expr.opus2} = {expr.Value()}')

#8
print('8. feladat: eredmenyek.txt')
with open('eredmenyek.txt','w',encoding='utf-8') as output:
    [print(f'{k.opus1} {k.oper} k{k.opus2} = {k.Value()}',file=output) for k in lista]
