#  0    1     2     3
#varos;nev1;nev2;ferohely
#2
with open('vb2018.txt') as f:
    lista=[sor.strip().split(';') for sor in f.readlines()[1:]]
#3
print(f'3. feladat: Stadionok száma: {len(lista)}')
#4
kis=sorted(lista,key=lambda x:x[3])[0]
print(f'4. fegladat: A legkevesebb férőhely:\n\tVáros: {kis[0]}\n\tStadion neve: {kis[1]}\n\tFérőhely: {kis[3]}')
#5
print(f'5. feladat: Átlagos férőhelyszám: {sum([int(k[3]) for k in lista])/len(lista):.1f}')
#6
print(f'6. feladat: Két néven is ismert stadionok száma: {sum([1 for k in lista if k[2]!="n.a."])}')
#7
while True:
    city=input('7. feladat: Kérem a város nevét: ').strip()
    if len(city)>=3:
        break
#8
i=0
van=False
while i<len(lista) and not van:
    van=lista[i][0].upper()==city.upper()
    i+=1
if van:
    print('8. feladat: A megadott város VB helyszín.')
else:
    print('8. feladat: A megadott város nem VB helyszín.')
#9
h=set()
for k in lista:
    h.add(k[0])
print(f'9. feladat: {len(h)} különböző városban voltak mérkőzések.')