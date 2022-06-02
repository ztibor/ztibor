'''KutyaNevek.csv
0    1
id;kutyanév
1;Akina
'''
#2
with open('KutyaNevek.csv',encoding='utf-8-sig') as f:
    fejlecnev=f.readline()
    nevlista=[sor.strip().split(';') for sor in f]

#3
print(f'3. feladat: Kutyanevek száma: {len(nevlista)}')

#4
#kutyaFajtak.csv
#0   1     2     3
#id;név;eredeti név
#1;Abruzzói juhászkutya;Cane da pastore Maremmano-Abruzzese
with open('KutyaFajtak.csv',encoding='utf-8-sig') as f:
    fejlecfajta=f.readline()
    fajtalista=[sor.strip().split(';') for sor in f]

#5
#Kutyak.csv
# 0     1       2      3               4
#id;fajta_id;név_id;életkor;utolsó orvosi ellenőrzés
#1;307;107;14;2017.11.27
with open('kutyak.csv',encoding='utf-8-sig') as f:
    fejléckutya=f.readline()
    kutyalista=[sor.strip().split(';') for sor in f]

#6
korok=[int(k[3]) for k in kutyalista]
print(f'6. feladat: Kutyák átlagéletkora: {sum(korok)/len(korok):.2f}')

#7
idos=max(korok)
fajta_nev=[(k[1],k[2]) for k in kutyalista if k[3]==str(idos)][0]
nev=[k[1] for k in nevlista if k[0]==fajta_nev[1]][0]
fajta=[k[1] for k in fajtalista if k[0]==fajta_nev[0]][0]
print(f'7. feladat: Legidősebb kutya neve és fajtája: {nev}, {fajta}')

#8
stat=dict()
for k in kutyalista:
    if k[4]=='2018.01.10':
        faj=[p[1] for p in fajtalista if p[0]==k[1]][0]
        stat[faj]=stat.get(faj,0)+1
print('8. feladat: Január 10-én vizsgált kutyafajták:')
[print(f'\t{k} : {stat[k]} kutya') for k in stat.keys()]

#9
terhel=dict()
for k in kutyalista:
    terhel[k[4]]=terhel.get(k[4],0)+1
mteher=sorted([(k,v) for k,v in terhel.items()], key=lambda x:x[1],reverse=True)[0]
print(f'9. feladat: Legjobban leterhelt nap: {mteher[0]}.: {mteher[1]} kutya')

#10
nevstat=dict()
for k in kutyalista:
    nev=[p[1] for p in nevlista if p[0]==k[2]][0]
    nevstat[nev]=nevstat.get(nev,0)+1
ordstat=sorted([(k,v) for k,v in nevstat.items()],key=lambda x:x[1],reverse=True)
with open('Névstatisztika.txt','w',encoding='utf-8') as output:
    [print(f'{k[0]};{k[1]}',file=output) for k in ordstat]

