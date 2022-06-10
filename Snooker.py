#   0       1   2       3
#Helyezes;Nev;Orszag;Nyeremeny
with open('snooker.txt') as f:
    lista=[sor.strip().split(';') for sor in f.readlines()[1:]]
print(f'3. feladat: A világranglistán {len(lista)} versenyző szerepel.')
print(f'4. feladat: A versenyzők átlagosan {sum([int(k[3]) for k in lista])/len(lista):.2f} fontot kerestek.')
print('5. feladat: A legtöbbet kereső kínai versenyző:')
top=sorted([k for k in lista if k[2]=='Kína'],key=lambda x:int(x[3]),reverse=True)[0]
print(f'\tHelyezés: {top[0]}\n\tNév: {top[1]}\n\tOrszág: {top[2]}\n\tNyeremény összege: {int(top[3])*380} Ft')
if sum([1 for k in lista if k[2]=='Norvégia'])>0:
    print('6. feladat: A versenyzők között van norvég versenyző')
else:
    print('6. feladat: A versenyzők között nincs norvég versenyző')
print('7. feladat: Statisztika')
stat=dict()
for k in lista:
    stat[k[2]]=stat.get(k[2],0)+1
[print(f'\t{k} - {stat[k]} fő') for k in stat.keys() if stat[k]>4]