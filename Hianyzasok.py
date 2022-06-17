# 0     1       2           3           4
#Név;Osztály;Első nap;Utolsó nap;Mulasztott órák
#1
with open('szeptember.csv') as f:
    lista=[sor.strip().split(';') for sor in f.readlines()[1:]]
#2
print(f'2. feladat\n\tÖsszes mulasztott órák száma: {sum([int(k[4]) for k in lista])} óra.')
#3
nap=int(input('3. feladat\n\tKérem adjon meg egy napot: '))
nev=input('\tTanuló neve: ').strip()
#4
if sum([1 for k in lista if k[0]==nev])>0:
    print('4. feladat\n\tA tanuló hiányzott szeptemberben')
else:
    print('4. feladat\n\tA tanuló nem hiányzott szeptemberben')
#5
print(f'5. feladat: Hiányzók 2017.09.{nap}-n:')
[print(f'\t{k[0]} ({k[1]})') for k in lista if int(k[2])<=nap<=int(k[3])]
#6
stat=dict()
for k in lista:
    stat[k[1]]=stat.get(k[1],0)+int(k[4])
with open('osszesites.csv','w') as out:
    [print(f'{k};{stat[k]}',file=out) for k in stat.keys()]