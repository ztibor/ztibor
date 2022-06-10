#  0        1        2      3      4    5
#csapat;versenyzo;eletkor;palya;korido;kor
def idomp(istr):
    s=istr.split(':')
    return 3600*int(s[0])+60*int(s[1])+int(s[2])
#2
with open('autoverseny.csv',encoding='utf-8') as f:
    lista=[k.strip().split(';') for k in f.readlines()[1:]]
#3
print(f'3. feladat: {len(lista)}')
#4
[print(f'4. feladat: {idomp(k[4])} másodperc') for k in lista if k[1]=='Fürge Ferenc' and k[3]=='Gran Prix Circuit' and k[5]=='3']
#5
vers=input('5. feladat\nKérem egy versenyző nevét:\n').strip()
#6
legjobb=sorted([k for k in lista if k[1]==vers],key=lambda x:idomp(x[4]))[0]
if legjobb:
    print(f'6. feladat: {legjobb[3]}, {legjobb[4]}')
else:
    print('Nincs ilyen versenyző az állományban')