#       0           1       2
#Hegycsúcs neve;Hegység;Magasság
with open('HegyekMo.txt',encoding='utf-8-sig') as f:
    lista=[sor.strip().split(';') for sor in f.readlines()[1:]]
print(f'3. feladat: Hegycsúcsok száma: {len(lista)} db')
print(f'4. feladat: Hegycsúcsok átlagos magassága: {sum([int(k[2]) for k in lista])/len(lista):.2f} m')
top=sorted(lista,key=lambda x:int(x[2]),reverse=True)[0]
print(f'5. feladat: A legmagasabb hegycsúcs adatai:\n\tNév: {top[0]}\n\tHegység: {top[1]}\n\tMagasság: {top[2]} m')
mag=int(input('6. feladat: Kérek egy magasságot: ').strip())
van=False
i=0
while i<len(lista) and not van:
    van=int(lista[i][2])>mag
    i+=1
if van:
    print(f'\tVan {mag}m-nél magasabb hegycsúcs a Börzsönyben!')
else:
    print(f'\tNincs {mag}m-nél magasabb hegycsúcs a Börzsönyben!')
print(f'7. feladat: 3000 lábnál magasabb hegycsúcsok száma: {sum([1 for k in lista if int(k[2])*3.280839895>3000])}')
stat=dict()
for k in lista:
    stat[k[1]]=stat.get(k[1],0)+1
print('8. feladat: Hegység statisztika')
[print(f'\t{k} - {stat[k]} db') for k in stat.keys()]
with open('bukk-videk.txt','w') as out:
    out.writelines('Hegycsúcs neve;Magasság láb\n')
    [print(f'{k[0]};{int(k[2])*3.280839895:.1f}',file=out) for k in lista]