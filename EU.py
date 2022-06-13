with open('EUcsatlakozas.txt') as f:
    lista=[s.strip().split(';') for s in f]
print(f'3. feladat: EU tagállamok száma: {len(lista)} db')
print(f'4. feladat: 2007-ben {sum(1 for k in lista if k[1][:4]=="2007")} ország csatlakozott')
print(f'5. feladat: Magyarország csatlakozásának dátuma: {[k[1] for k in lista if k[0]=="Magyarország"][0]}')
if [k for k in lista if k[1][5:7]=="05"]:
    print('6. feladat: Májusban volt csatlakozás!')
else:
    print('6. feladat: Májusban nem volt csatlakozás!')
print(f'7. feladat: Legutoljára csatlakozott ország: {sorted(lista,key=lambda x:x[1],reverse=True)[0][0]}')
stat=dict()
for k in lista:
    stat[k[1][:4]]=stat.get(k[1][:4],0)+1
print('8. feladat: Statisztika')
[print(f'\t{k} - {stat[k]} ország') for k in stat.keys()]