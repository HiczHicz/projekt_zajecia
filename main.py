from tkinter import *
from tkinter import font
import random

l = []
with open('slowka.txt', 'r', encoding='utf-8') as slowka:
    for s in slowka:
        d = s.strip()
        r = d.split('\t')
        l.append(r)
# polski-angielski
pol_ang = {}
for i in l:
    pol_ang[i[1]] = i[0]
ang_pol = {}
for i in l:
    ang_pol[i[0]] = i[1]

def otwieranie_angielski():
    def slowko_ang_pol():
        global angielski
        angielski = random.choice(list(ang_pol.keys()))
        slowko.configure(text=angielski)
        wpisz.delete(0,END)
    def sprawdz():
        odpowiedz=wpisz.get()
        if odpowiedz.lower() == ang_pol[angielski].lower():
            wynik.configure(text='Dobrze!')
            del ang_pol[angielski]
            wpisz.delete(0, END)
            slowko.configure(text=angielski)
            slowko_ang_pol()
        else:
            wynik.configure(text='nie ok! Poprawna odpowiedź to:'+ang_pol[angielski])
            slowko_ang_pol()
            wpisz.delete(0, END)
    okno1.destroy()
    okno_angielski=Tk()
    okno_angielski.geometry("600x300")



    okno_angielski.title('Tłumaczenie angielskich słowek na polski')
    slowko = Label(okno_angielski, text='', font=('Comic Sans MS', 20), fg='black')
    slowko.pack()
    wynik=Label(okno_angielski, text='')
    wynik.pack()
    wpisz=Entry()
    wpisz.pack()

    losuj=Button(text='losuj', command=slowko_ang_pol)
    losuj.pack()

    ok=Button(text='ok', command=sprawdz)
    ok.pack()

    okno_angielski.mainloop()


def otwieranie_polski():
    def slowko_pol_ang():
        global polski
        polski = random.choice(list(pol_ang.keys()))
        slowko.configure(text=polski)
        wpisz.delete(0,END)
    def sprawdz():
        odpowiedz=wpisz.get()
        if odpowiedz.lower() == pol_ang[polski].lower():
            wynik.configure(text='Dobrze!')
            del pol_ang[polski]
            wpisz.delete(0, END)
            slowko.configure(text=polski)
            slowko_pol_ang()
        else:
            wynik.configure(text='nie ok! Poprawna odpowiedź to:' + pol_ang[polski])
            slowko_pol_ang()
            wpisz.delete(0, END)
    okno1.destroy()
    okno_polski=Tk()
    okno_polski.title('Tłumaczenie angielskich słowek na polski')
    slowko = Label(okno_polski, text='', font=('Comic Sans MS', 20), fg='black')
    slowko.pack()
    wynik=Label(okno_polski, text='')
    wynik.pack()
    wpisz=Entry()
    wpisz.pack()

    losuj=Button(text='losuj', command=slowko_pol_ang)
    losuj.pack()

    ok=Button(text='ok', command=sprawdz)
    ok.pack()

    okno_polski.mainloop()


okno1=Tk()
okno1.title('Wybierz tryb gry')
okno1.geometry('750x250')
okno1.attributes("-topmost", True)

napis=Label(okno1,text='Wybierz tryb gry:', font=('Comic Sans MS', 20), fg='black')
napis.pack()


angpol=Button(okno1,text='Angielski -> Polski',font=('Comic Sans MS', 12), fg = "black", width=25, command=otwieranie_angielski)
angpol.pack(pady=20)


polang=Button(okno1,text='Polski -> Angielski', font=('Comic Sans MS', 12), fg='black', width=25, command=otwieranie_polski)
polang.pack(pady=20)


okno1.mainloop()