#KutyaNevek.csv
#0    1
#id;kutyanév
#2
f=open('KutyaNevek.csv',encoding='utf-8-sig')
nevlista=[sor.strip().split(';') for sor in f.readlines()[1:]]

#3
print(f'3. feladat: Kutyanevek száma: {len(nevlista)}')

#kutyaFajtak.csv
#0   1     2     3
#id;név;eredeti név
#4
f=open('KutyaFajtak.csv',encoding='utf-8-sig')
fajtalista=[sor.strip().split(';') for sor in f.readlines()[1:]]

#Kutyak.csv
# 0     1       2      3               4
#id;fajta_id;név_id;életkor;utolsó orvosi ellenőrzés
#5
f=open('kutyak.csv',encoding='utf-8-sig')
kutyalista=[sor.strip().split(';') for sor in f.readlines()[1:]]

#6
korok=[int(k[3]) for k in kutyalista]
print(f'6. feladat: Kutyák átlagéletkora: {sum(korok)/len(korok):.2f}')

#7
idos=max(korok)
fajtaid_nevid=[(k[1],k[2]) for k in kutyalista if k[3]==str(idos)][0]
nev=[k[1] for k in nevlista if k[0]==fajtaid_nevid[1]][0]
fajta=[k[1] for k in fajtalista if k[0]==fajtaid_nevid[0]][0]
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