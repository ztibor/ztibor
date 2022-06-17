#     0       1 2 3
#2018.03.06. 11 3 0
#2
with open('lift.txt') as f:
    lista=[sor.strip().split() for sor in f]
#3
print(f'3. feladat: Összes lifthasználat: {len(lista)}')
#4
print(f'4. feladat: Időszak: {min([k[0] for k in lista])} - {max([k[0] for k in lista])}')
#5
print(f'5. feladat: Célszint max: {max([k[3] for k in lista])}')
#6
try:
    num=int(input('6. feladat:\n\tKártya száma: ').strip())
    cel=int(input('\tCélszint száma: ').strip())
except:
    print('Konvertálái hiba')
#7
if sum([1 for k in lista if int(k[1])==num and int(k[3])==cel])>0:
    print(f'7. feladat: A(z) {num}. kártyával utaztak a(z) {cel}. emeletre')
else:
    print(f'7. feladat: A(z) {num}. kártyával nem utaztak a(z) {cel}. emeletre')
#8
stat=dict()
for k in lista:
    stat[k[0]]=stat.get(k[0],0)+1
print('8. feladat: Statisztika')
[print(f'\t{k} - {stat[k]}x') for k in sorted(stat.keys())]