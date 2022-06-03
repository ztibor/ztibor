#év;típus;keresztnév;vezetéknév
# 0   1       2         3
class Dijas:
    def __init__(self,sor):
        s=sor.strip().split(';')
        self.ev=int(s[0])
        self.tipus=s[1]
        self.knev=s[2]
        self.vnev=s[3]

#2
f=open('nobel.csv',encoding='utf-8')
lista=[Dijas(k) for k in f.readlines()[1:]]

#3
dijtipus=[k for k in lista if k.knev=='Arthur B.' and k.vnev=='McDonald'][0].tipus
print(f'3. feladat: {dijtipus}')

#4
irodalmi_2017=[k for k in lista if k.ev==2017 and k.tipus=='irodalmi'][0]
print(f'4. feladat: {irodalmi_2017.knev} {irodalmi_2017.vnev}')

#5
szervek=[k for k in lista if k.vnev=='']
print('5. feladat')
[print(f'\t{k.ev}: {k.knev}') for k in szervek]

#6
curie=[k for k in lista if 'Curie' in k.vnev]
print('6. feladat')
[print(f'\t{k.ev}: {k.knev} {k.vnev} ({k.tipus})') for k in curie]

#7. feladat
tipdb=dict()
for k in lista:
    tipdb[k.tipus]=tipdb.get(k.tipus,0)+1
print('7. feladat')
[print(f'\t{k:15} {tipdb[k]:-15} db') for k in tipdb.keys()]

#8
orvosi=sorted([k for k in lista if k.tipus=='orvosi'],key=lambda x:x.ev)
with open('orvosi.txt','w',encoding='utf-8') as output:
    [print(f'{k.ev}: {k.knev} {k.vnev}',file=output) for k in orvosi]
