#   0     1     2          3         4
#Indulás;Cél;Rendszám;Telefonszám;Férőhely
#1
with open('autok.csv') as f:
    fejlec=f.readline()
    szolglista=[sor.strip().split(';') for sor in f]
#2
print(f'2. feladat\n\t{len(szolglista)} autós hirdet fuvart')
#3
print(f'\n3. feladat\n\tÖsszesen {sum([int(k[4]) for k in szolglista if k[0]=="Budapest" and k[1]=="Miskolc"])} férőhelyet hirdettek az autósok Budapestről Miskolcra')
#4 Több maximális férőhely ajánlat közül az egyik
rendez=sorted(szolglista,key=lambda x:x[4],reverse=True)
print(f'\n4. feladat\n\tA legtöbb férőhelyet ({rendez[0][4]}) a(z) {rendez[0][0]}-{rendez[0][1]} útvonalon ajánlották fel a hidetők')
#     0        1    2      3
#Azonosító;Indulás;Cél;Személyek
#5
with open('igenyek.csv') as g:
    fejlec=g.readline()
    igenylista=[sor.strip().split(';') for sor in g]
print('\n5. feladat')
ut_frsz=dict()
for k in szolglista:
    ut_frsz[k[0]+'-'+k[1]]=ut_frsz.get(k[0]+'-'+k[1],k[2])
for k in igenylista:
    if k[1]+'-'+k[2] in ut_frsz.keys():
        print(f'\t{k[0]} => {ut_frsz[k[1]+"-"+k[2]]}')
#6
frsz_tel=dict()
for k in szolglista:
    frsz_tel[k[2]]=frsz_tel.get(k[2],k[3])
out=list()
for k in igenylista:
    if k[1]+'-'+k[2] in ut_frsz.keys():
        frsz=ut_frsz[k[1]+"-"+k[2]]
        out.append(k[0]+': Rendszám: '+frsz+', Telefonszám: '+frsz_tel[frsz])
    else:
        out.append(k[0]+': Sajnos nem sikerült autót találni')
with open('utasuzenetek.txt','w',encoding='utf-8') as output:
    [print(f'{k}', file=output) for k in out]