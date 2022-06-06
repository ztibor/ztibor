class Keszlet:
    def __init__(self,sor):
        s=sor.strip().split(';')
        self.tkod=s[0]
        self.nev=s[1]
        self.ar=int(s[2])
        self.kdb=int(s[3])
class Rendeles:
    def __init__(self,sor):
        s=sor.strip().split(';')
        self.datum=s[1]
        self.rsz=int(s[2])
        self.email=s[3]
        self.statusz=''
        self.osszeg=0
class Tetel:
    def __init__(self,sor):
        s=sor.strip().split(';')
        self.rsz=int(s[1])
        self.tkod=s[2]
        self.rdb=int(s[3])
        self.kiad=False
#1
with open('rendeles.csv',encoding='latin2') as f:
    inp=f.readlines()
    rendlist=[Rendeles(sor) for sor in inp if sor[0]=='M']
    tetellist=[Tetel(sor) for sor in inp if sor[0]=='T']
with open('raktar.csv',encoding='latin2') as g:
    keszletlist=[Keszlet(sor) for sor in g]

#2
menny=dict()
arak=dict()
for k in keszletlist:
    menny[k.tkod]=menny.get(k.tkod,k.kdb)
    arak[k.tkod] = arak.get(k.tkod,k.ar)
for k in rendlist:
    aktrend=[p for p in tetellist if p.rsz==k.rsz]
    dbjo=sum([1 for p in aktrend if p.rdb<=menny[p.tkod]])
    if dbjo==len(aktrend):
        k.statusz='T'
        for p in aktrend:
            menny[p.tkod]-=p.rdb
            k.osszeg+=p.rdb*arak[p.tkod]
            index=[i for i,t in enumerate(tetellist) if t.rsz==p.rsz and t.tkod==p.tkod][0]
            tetellist[index].kiad=True
    else:
        k.statusz='V'

#3
out=list()
for k in rendlist:
    if k.statusz=='T':
        out.append(k.email+';A rendelését két napon belül szállítjuk. A rendelés értéke: '+str(k.osszeg)+'Ft\n')
    else:
        out.append(k.email+';A rendelése függő állapotba került. Hamarosan értesítjük a szállítás időpontjáról\n')
f=open('levelek.csv','w',encoding='utf-8')
f.writelines(out)

#4
besz=dict()
for k in tetellist:
    if not k.kiad:
        besz[k.tkod]=besz.get(k.tkod,0)+k.rdb
with open('beszerzes.csv','w',encoding='utf-8') as output:
    for k in besz.keys():
        if besz[k]>menny[k]:
            [print(f'{k};{besz[k]-menny[k]}',file=output)]
