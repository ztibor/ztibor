with open('fifa.txt') as f:
    lista=[sor.strip().split(';') for sor in f.readlines()[1:]]
print(f'3. feladat: A világranglistán {len(lista)} csapat szerepel')
print(f'4. feladat: A csapatok átlagos pontszáma: {sum([int(k[3]) for k in lista])/len(lista):.2f} pont')
print('5. feladat: A legtöbbet javító csapat: ')
top=sorted(lista,key=lambda x:x[2],reverse=True)[0]
print(f'\tHelyezés: {top[1]}\n\tCsapat: {top[0]}\n\tPontszám: {top[3]}')
van=sum([1 for k in lista if k[0]=='Magyarország'])>0
if van:
    print('6. feladat: A csapatok között van Magyarország')
else:
    print('6. feladat: A csapatok között nincs Magyarország')
print('7. feladat: Statisztika:')
stat=dict()
for k in lista:
    stat[k[2]]=stat.get(k[2],0)+1
[print(f'\t{k} helyet változott: {stat[k]} csapat') for k in stat.keys() if stat[k]>1]