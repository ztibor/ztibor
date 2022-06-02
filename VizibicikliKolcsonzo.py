'''kolcsonzesek.txt
 0    1     2    3     4    5
Név   Jazon Eóra Eperc Vóra Vperc
Mihály;C;    9;   55;   10;   56
'''
#2
class Kolcsonzes:
    #3
    def __init__(self,sor):
        s=sor.strip().split(';')
        Név,Jazon,Eóra,Eperc,Vóra,Vperc=s
        self.Név=Név
        self.Jazon=Jazon
        self.Eóra=int(Eóra)
        self.Eperc=int(Eperc)
        self.Vóra=int(Vóra)
        self.Vperc=int(Vperc)

    def kdij(self):
        kido=idomp(self.Vóra,self.Vperc)-idomp(self.Eóra,self.Eperc)
        if kido%1800==0:
            return kido//1800*2400
        else:
            return int((round(kido//1800,0)+1))*2400

def idomp(ó,p):
    return ó*3600+60*p

#4
with open('kolcsonzesek.txt',encoding='utf-8') as f:
    fejléc=f.readline()
    lista=[Kolcsonzes(k) for k in f]
f.close()

#5
print(f'5. feladat: Napi kölcsönzések száma: {len(lista)}')

#6
nev=input('6. feladat: Kérek egy nevet: ')
nevlist=[k for k in lista if k.Név==nev.strip()]
if len(nevlist)==0:
    print('\tNem volt ilyen nevű kölcsönző!')
else:
    print(f'\t{nev} kölcsönzései:')
    [print(f'\t{k.Eóra}:{k.Eperc}-{k.Vóra}:{k.Vperc}') for k in nevlist]

#7
ido=input('7. feladat: Adjon meg egy időpontot óra:perc alakban: ')
ó,p=ido.strip().split(':')
vizen=[k for k in lista if (idomp(k.Eóra,k.Eperc)<=idomp(int(ó),int(p))<=idomp(k.Vóra,k.Vperc))]
print('\tA vízen levő járművek:')
[print(f'\t{k.Eóra}:{k.Eperc}.{k.Vóra}:{k.Vperc} : {k.Név}') for k in vizen]

#8
print(f'8. feladat: A napi bevétel: {sum([k.kdij() for k in lista])} Ft')

#9
fek=[k for k in lista if k.Jazon=='F']
with open('F.txt','w',encoding='utf-8') as output:
    [print(f'{k.Eóra}:{k.Eperc}-{k.Vóra}:{k.Vperc} : {k.Név}', file=output) for k in fek]

#10
stat=dict()
for k in lista:
    stat[k.Jazon]=stat.get(k.Jazon,0)+1
print('10. feladat: Statisztika')
sor=sorted([(k,v) for k,v in stat.items()])
[print(f'\t{k[0]} - {k[1]}') for k in sor]
