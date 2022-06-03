#4
def ÖsszPontszám(nev):
    rp=[k for k in rovid if k[0]==nev][0]
    dont=[k for k in kur if k[0]==nev]
    rovidpont=float(rp[2])+float(rp[3])-float(rp[4])
    if len(dont)==0:
        return rovidpont
    else:
        kurpont=float(dont[0][2])+float(dont[0][3])-float(dont[0][4])
        return rovidpont+kurpont

#rovidprogramcsv, donto.csv
#Név;Ország;Technikai;Komponens;Levonás
# 0     1       2          3        4
#1
f=open('rovidprogram.csv')
rovid=[k.strip().split(';') for k in f.readlines()[1:]]
f.close()
f=open('donto.csv')
kur=[k.strip().split(';') for k in f.readlines()[1:]]
f.close()

#2
print(f'2. feladat\n\tA rövidprogramban {len(rovid)} induló volt')

#3
orszag={k[1] for k in kur}
if 'HUN' in orszag:
    print('3. feladat: A magyar versenyző bejutott a kűrbe')
else:
    print('3. feladat: A magyar versenyző nem jutott be a kűrbe')

#5#6
vers=input('5. feladat\n\tKérem a versenyző nevét: ')
nev=[k[0] for k in rovid if k[0]==vers]
if len(nev)==0:
    print('\tIlyen nevű induló nem volt')
else:
    print(f'6. feladat\n\tA versenyző összpontszáma: {ÖsszPontszám(nev[0])}')

#7
orsz=dict()
for k in kur:
    orsz[k[1]]=orsz.get(k[1],0)+1
print('7. feladat')
[print(f'\t{k}: {orsz[k]} versenyző') for k in orsz.keys() if orsz[k]>1]

#8
with open('vegeredmeny.csv','w',encoding='utf-8') as output:
    [print(f'{i+1};{k[0]};{k[1]};{ÖsszPontszám(k[0]):.2f}',file=output) for i,k in enumerate(sorted(kur,key=lambda x:ÖsszPontszám(x[0]),reverse=True))]