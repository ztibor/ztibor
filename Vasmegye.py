#3
def CdvEll(id):
    s=id.split('-')
    ossz=10*int(s[0])
    for i in range(6):
        ossz+=(9-i)*int(s[1][i])
    ossz+=3*int(s[2][0])+2*int(s[2][1])+int(s[2][2])
    return ossz%11==int(s[2][3])
#2
print('2. feladat: Adatok beolvasása, tárolása')
with open('vas.txt') as f:
    lista=[sor.strip() for sor in f]
#4
print('4. feladat: Ellenőrzés')
hiba=[]
for k in lista:
    if not CdvEll(k):
        print(f'\tHibás a {k} személyi azonosító!')
        hiba.append(k)
for k in hiba:
    lista.remove(k)
#5
print(f'5. feladat: Vas megyében a vizsgált évek alatt {len(lista)} csecsemő született.')
#6
print(f'6. feladat: Fiúk száma: {sum([1 for k in lista if k[0] in ["1","3"]])}')
#7
print(f'7. feladat: Vizsgált időszak: 19{min([k[2:4] for k in lista if k[0] in ["1","2"]])} - 20{max([k[2:4] for k in lista if k[0] in ["3","4"]])}')
#8
i=0
van=False
while i<len(lista) and not van:
    van=int(lista[i][2:4])%4==0 and lista[i][4:8]=='0224'
    i+=1
if van:
    print('8. feladat: Szökőnapon született baba!')
else:
    print('8. feladat: Szökőnapon nem született baba!')
#9
stat=dict()
for k in lista:
    if k[0] in ['1','2']:
        stat[1900+int(k[2:4])]=stat.get(1900+int(k[2:4]),0)+1
    else:
        stat[2000 + int(k[2:4])] = stat.get(2000 + int(k[2:4]), 0) + 1
print('9. feladat: Statisztika')
[print(f'\t{k} - {stat[k]} fő') for k in sorted(stat.keys())]