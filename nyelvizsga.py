#nyelv;2009;2010;2011;2012;2013;2014;2015;2016;2017;2018
# 0     1    2     3    4    5    6    7    8   9    10
class Nyelv:
    def __init__(self,siker,slen):
        s1=siker.strip().split(';')
        s2=slen.strip().split(';')
        self.nyelv=s1[0]
        self.sikeres=[]
        self.sikertelen=[]
        self.osszes=[]
        for i in range(1,11):
            self.sikeres.append(int(s1[i]))
            self.sikertelen.append(int(s2[i]))
            self.osszes.append(self.sikeres[i-1]+self.sikertelen[i-1])

#1
with open('sikeres.csv') as f:
    siklista=[k for k in f.readlines()[1:]]
with open('sikertelen.csv') as g:
    slenlista = [k for k in g.readlines()[1:]]
vizsga=[]
for i in range(len(siklista)):
    vizsga.append(Nyelv(siklista[i],slenlista[i]))

#2
sor=sorted(vizsga,key=lambda x:sum(x.osszes),reverse=True)[:3]
print('2. feladat: A legnépszerűbb nyelvek:')
[print(f'\t{k.nyelv}') for k in sor]

#3
print('3. feladat')
while True:
    ev=int(input('\tVizsgálandó év: ').strip())
    if (2009<=ev<=2017):
        break

#4
arany=sorted([(k.nyelv,k.sikeres[ev-2009]/k.osszes[ev-2009]) for k in vizsga if k.osszes[ev-2009]!=0],key=lambda x:x[1],reverse=True)
print(f'4. feladat:\n\t{ev}-ben {arany[0][0]} nyelvből a sikeres vizsgák aránya {arany[0][1]*100:.2f}%')

#5
nemvolt=[k.nyelv for k in vizsga if k.osszes[ev-2009]==0]
print('5. feladat')
[print(f'\t{k}') for k in nemvolt]

#6
stat=[(k.nyelv,sum(k.osszes),sum(k.sikeres)/sum(k.osszes)*100)for k in vizsga]
with open('osszesites.csv','w',encoding='utf-8') as output:
    [print(f'{k[0]};{k[1]};{k[2]:.2f}%',file=output) for k in stat]

