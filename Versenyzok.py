# 0         1             2        3
#név;születési_dátum;nemzetiség;rajtszám
#Lewis Hamilton;1985.01.07;brit;44
#2
with open('pilotak.csv',encoding='utf-8') as f:
    lista=[k.strip().split(';') for k in f.readlines()[1:]]
#3
print(f'3. feladat: {len(lista)}')
#4
print(f'4. feladat: {lista[len(lista)-1][0]}')
#5
print('5. feladat')
[print(f'\t{k[0]} ({k[1]}') for k in [p for p in lista if p[1][:2]<'19']]
#6
print(f'6. feladat: {sorted([k for k in lista if k[3]!=""],key=lambda x:int(x[3]))[0][2]}')
#7
stat=dict()
for k in lista:
    if k[3]!='':
        stat[k[3]]=stat.get(k[3],0)+1
print('7. feladat:',end=' ')
[print(f'{k}',end=", ") for k in stat.keys() if stat[k]>1]
