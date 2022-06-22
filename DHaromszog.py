from tkinter import *
from tkinter import filedialog

lista=[]

class DHaromszog:
    __aOldal,__bOldal, __cOldal=0,0,0

    def __init__(self,num,sor):
        s=sor.strip().replace(',','.').split(' ')
        self.a=float(s[0])
        self.b=float(s[1])
        self.c=float(s[2])
        self._Kerulet=self.Kerulet
        self._Terulet=self.Terulet
        self.SorSzama=num
        if self.a > 0 and self.b > 0 and self.c > 0:
            if not self.EllNovekvoSorrend:
                raise Exception(str(self.SorSzama) + '.sor: Az adatok nincsenek növekvő sorrendben')
            if not self.EllMegszerkesztheto:
                raise Exception(str(self.SorSzama) + '. sor: A háromszöget nem lehet megszerkeszteni')
            if not self.EllDerekszogu:
                raise Exception(str(self.SorSzama) + '. sor: A háromszög nem derékszögű')
        else:
            if self.a <= 0:
                raise Exception(str(self.SorSzama)+". sor: Az 'a' oldal nem lehet nulla vegy negatív")
            if self.b <= 0:
                raise Exception(str(self.SorSzama)+". sor: A 'b' oldal nem lehet nulla vegy negatív")
            if self.c <= 0:
                raise Exception(str(self.SorSzama)+". sor: A 'c' oldal nem lehet nulla vegy negatív")
        self.__aOldal = self.a
        self.__bOldal = self.b
        self.__cOldal = self.c

    @property
    def EllDerekszogu(self):
        if self.a*self.a+self.b*self.b==self.c*self.c:
            return True
        else:
            return False

    @property
    def EllMegszerkesztheto(self):
        if self.a+self.b>self.c:
            return True
        else:
            return False

    @property
    def EllNovekvoSorrend(self):
        if self.a<=self.b and self.b<=self.c:
            return True
        else:
            return False

    @property
    def Kerulet(self):
        return self.__aOldal+self.__bOldal+self.__cOldal

    @property
    def Terulet(self):
        return self.__aOldal*self.__bOldal/2

def passfv():
    global lista
    listb1.delete(0,END)
    listb2.delete(0,END)
    f_path=filedialog.askopenfilename()
    i=1
    f=open(f_path)
    for sor in f.readlines():
        try:
            dh=DHaromszog(i,sor)
            s=str(dh.SorSzama)+'. sor: a='+str(dh.a)+' b='+str(dh.b)+' c='+str(dh.c)
            listb2.insert(END,s)
            lista.append(dh)
            i+=1
        except Exception as e:
            listb1.insert(END,e)
            i+=1

def clickEvent(event):
    listb3.delete(0,END)
    w=event.widget
    index=w.curselection()[0]
    listb3.insert(END,' ')
    listb3.insert(END,'Kerület = '+str(lista[index].Kerulet))
    listb3.insert(END,' ' )
    listb3.insert(END,'Terület = '+str(lista[index].Terulet))

top=Tk()
top.geometry('700x500')
top.configure(bg='white')
top.title('Derékszögű háromszögek')
lfr1=LabelFrame(top,text='Hibák a kiválasztott állományban',width=660,height=160,bg='white')
lfr2=LabelFrame(top,text='Derékszögű háromszögek',width=250,height=230, bg='white')
lfr3=LabelFrame(top,text='Kiválasztott derékszögű háromszög adatai',width=390,height=150,bg='white')
lfr1.place(x=20,y=80)
lfr2.place(x=20,y=250)
lfr3.place(x=290,y=250)
btn=Button(top,text='  Adatok betöltése  ',height=2,width=20,command=passfv)
btn.place(x=20,y=20)
listb1=Listbox(top,width=105,height=8,relief=FLAT,bd=0)
listb1.place(x=35,y=100)
listb2=Listbox(top,width=35,height=12,relief=FLAT,bd=0)
listb2.bind('<<ListboxSelect>>',clickEvent)
listb2.place(x=35,y=270)
listb3=Listbox(top,width=60,height=6,relief=FLAT,bd=0)
listb3.place(x=300,y=275)
top.mainloop()