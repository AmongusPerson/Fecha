from tkinter import *
import datetime
import pytz
pg = Tk()
pg.geometry("500x500")
pg.title("Zonas Horarias")
pg.configure(background="#264653")

lb1 = Label(pg, text="Zona Horaria CDMX", bg="#e76f51", fg="white", font=200)
lb1.place(relx=0.5, rely=0.45, anchor=CENTER,)

lb2 = Label(pg, text=".", bg="#e76f51", fg="white", font=200)
lb2.place(relx=0.5, rely=0.55, anchor=CENTER,)

def fn1():
    vr1 = pytz.timezone("America/Mexico_City")
    vr2 = datetime.datetime.now(vr1)
    return vr2.strftime("%d/%m/%Y")
def fn2():
    vr3 = fn1()
    lb2["text"] = vr3
    pg.after(60000,fn2)

fn2()

pg.mainloop()