#6
def Morze2Szöveg(s):
    global abclista
    mondat=''
    szavak=s.strip().split('       ')
    for szo in szavak:
        betukodok=szo.split('   ')
        s=''
        for kod in betukodok:
            betu=[k[0] for k in abclista if k[1]==kod][0]
            s+=betu
        mondat+=s+' '
    return mondat.strip()

#morzeabc.txt
# 0     1
#Betű;Morzekód
#2
f=open('morzeabc.txt')
abclista=[sor.strip().split('\t') for sor in f.readlines()[1:]]

#3
print(f'3. feladat: A morze abc {len(abclista)} db karakter kódját tartalmazza')

#4
ch=input('4. feladat: Kérek egy karaktert: ').strip().upper()[0]
kar=[k for k in abclista if k[0]==ch]
if len(kar)==0:
    print('nem található a kódtárbanilyen karakter')
else:
    print(f'\tA {ch} karakter kódja: {kar[0][1]}')

#5
f=open('morze.txt')
idezetek=[sor.strip().split(';') for sor in f]

#7
print(f'7. feladat: Az első idézet szerzője: {Morze2Szöveg(idezetek[0][0])}')

#8
leg=sorted([k for k in idezetek],key=lambda x:len(Morze2Szöveg(x[1])),reverse=True)[0]
print(f'8. feladat: A leghosszabb idézet szerzője és az idézet: {Morze2Szöveg(leg[0])}: {Morze2Szöveg(leg[1])}')

#9
ariszto=[k for k in idezetek if Morze2Szöveg(k[0])=='ARISZTOTELÉSZ']
print('9. feladat: Arisztotelész idézetei:')
[print(f'\t- {Morze2Szöveg(k[1])}') for k in ariszto]

#10
with open('forditas.txt','w',encoding='utf-8') as output:
    [print(f'{Morze2Szöveg(k[0])}: {Morze2Szöveg(k[1])}',file=output) for k in idezetek]
