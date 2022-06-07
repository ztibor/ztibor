class domain:
    def __init__(self,sor):
        self.Name,self.IP=sor.strip().split(';')
    #4
    def Domain(self,szint):
        dom=self.Name.split('.')
        if szint>len(dom):
            return 'nincs'
        else:
            return dom[-szint]

#2
with open('csudh.txt') as f:
    lista=[domain(sor) for sor in f][1:]

#3
print(f'3. feladat: Domainek száma: {len(lista)}')

#5
print('5. feladat: Az első domain felépítése:')
for i in range(1,6):
    print(f'\t{i}. szint: {lista[0].Domain(i)}')

#6
out=[]
out.append('<DOCTYPE html>\n<html>\n<head></head>\n<body>\n<table>\n')
out.append('<tr>\n<th style="text-align: left">Ssz</th>\n')
out.append('<th style="text-align: left">Host domain neve</th>\n')
out.append('<th style="text-align: left">Host IP cime</th>\n')
out.append('<th style="text-align: left">1. szint</th>\n')
out.append('<th style="text-align: left">2. szint</th>\n')
out.append('<th style="text-align: left">3. szint</th>\n')
out.append('<th style="text-align: left">4. szint</th>\n')
out.append('<th style="text-align: left">5. szint</th>\n</tr>')
for i,k in enumerate(lista):
    out.append(f'<tr>\n<th style="text-align: left">{i+1}.</th>\n')
    out.append(f'<th style="text-align: left">{k.Name}</th>\n')
    out.append(f'<th style="text-align: left">{k.IP}</th>\n')
    out.append(f'<th style="text-align: left">{k.Domain(1)}</th>\n')
    out.append(f'<th style="text-align: left">{k.Domain(2)}</th>\n')
    out.append(f'<th style="text-align: left">{k.Domain(3)}</th>\n')
    out.append(f'<th style="text-align: left">{k.Domain(4)}</th>\n')
    out.append(f'<th style="text-align: left">{k.Domain(5)}</th>\n</tr>')
out.append('</table>\n</body>\n</html>')
with open('tabla.html','w') as f:
    f.writelines(out)

