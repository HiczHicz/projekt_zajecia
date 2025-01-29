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
    #okno1.destroy()
    okno_angielski=Tk()
    okno_angielski.geometry("600x200")

    okno_angielski.update_idletasks()
    szerokosc_okna = 600
    wysokosc_okna = 200
    szerokosc_ekranu = okno_angielski.winfo_screenwidth()
    wysokosc_ekranu = okno_angielski.winfo_screenheight()

    # Obliczenie pozycji
    x = (szerokosc_ekranu - szerokosc_okna) // 2
    y = (wysokosc_ekranu - wysokosc_okna) // 2
    okno_angielski.geometry(f"{szerokosc_okna}x{wysokosc_okna}+{x}+{y}")  # Ustawienie pozycji na środku

    # Ustawienie okna na wierzchu
    okno_angielski.attributes("-topmost", True)

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

    zmien_tryb=Button(text='zmien tryb', command=lambda:[okno_angielski.destroy(), otwieranie_polski()])
    zmien_tryb.pack()

    zakoncz=Button(text='zakoncz', command=okno_angielski.destroy)
    zakoncz.pack()

    okno_angielski.mainloop()

#############################################




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
    #okno1.destroy()
    okno_polski=Tk()

    okno_polski.geometry("600x200")

    okno_polski.update_idletasks()
    szerokosc_okna = 600
    wysokosc_okna = 200
    szerokosc_ekranu = okno_polski.winfo_screenwidth()
    wysokosc_ekranu = okno_polski.winfo_screenheight()

    # Obliczenie pozycji
    x = (szerokosc_ekranu - szerokosc_okna) // 2
    y = (wysokosc_ekranu - wysokosc_okna) // 2
    okno_polski.geometry(f"{szerokosc_okna}x{wysokosc_okna}+{x}+{y}")  # Ustawienie pozycji na środku

    # Ustawienie okna na wierzchu
    okno_polski.attributes("-topmost", True)

    okno_polski.title('Tłumaczenie polskich słowek na angielski')
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

    zmien_tryb=Button(text='zmien tryb', command=lambda:[okno_polski.destroy(), otwieranie_angielski()])
    zmien_tryb.pack()

    zakoncz=Button(text='zakoncz', command=okno_polski.destroy)
    zakoncz.pack()


    okno_polski.mainloop()


okno1=Tk()
okno1.title('Wybierz tryb gry')
okno1.geometry("600x200")

okno1.update_idletasks()
szerokosc_okna = 600
wysokosc_okna = 200
szerokosc_ekranu = okno1.winfo_screenwidth()
wysokosc_ekranu = okno1.winfo_screenheight()

# Obliczenie pozycji
x = (szerokosc_ekranu - szerokosc_okna) // 2
y = (wysokosc_ekranu - wysokosc_okna) // 2
okno1.geometry(f"{szerokosc_okna}x{wysokosc_okna}+{x}+{y}")  # Ustawienie pozycji na środku

# Ustawienie okna na wierzchu
okno1.attributes("-topmost", True)

napis=Label(okno1,text='Wybierz tryb gry:', font=('Comic Sans MS', 20), fg='black')
napis.pack()


angpol=Button(okno1,text='Angielski -> Polski',font=('Comic Sans MS', 12), fg = "black", width=25, command=lambda:[okno1.destroy(), otwieranie_angielski()])
angpol.pack(pady=20)


polang=Button(okno1,text='Polski -> Angielski', font=('Comic Sans MS', 12), fg='black', width=25, command=lambda:[okno1.destroy(), otwieranie_polski()])
polang.pack(pady=20)


okno1.mainloop()