import time 
import os
import sys
import tkinter as tk
from tkinter import messagebox as ms

kayit_edilecek = """
\t\t {} \t {}

Dersler\t\t\tVize\tFinal\tDurum    
{}\t\t\t{}\t{}\t{}\t{}
{}\t\t\t{}\t{}\t{}\t{}
{}\t\t\t{}\t{}\t{}\t{}
{}\t\t\t{}\t{}\t{}\t{}
{}\t\t\t{}\t{}\t{}\t{}
{}\t\t\t{}\t{}\t{}\t{}
{}\t\t\t{}\t{}\t{}\t{}

        Gecme Puani --> {}

"""


def geckal ( baraj , puan) :
    
    baraj= int(baraj) * 10
    puan = int(puan) * 10

    if (puan >= baraj) :
        return  "Gecti" , "green"   

    elif (puan < baraj) :
        return "Kaldi " , "red"

def Hesapla() :
    try :
        def Kaydet () :
            isim = isim11 +" "+ Sisim11
            aaa = kayit_edilecek.format(isim11 , Sisim11,
                                        ders11,vize11, final11, a , geckal(gecmepuani1, a)[0], 
                                        ders12,vize12, final12, b , geckal(gecmepuani1, b)[0],
                                        ders13,vize13, final13, c , geckal(gecmepuani1, c)[0],
                                        ders14,vize14, final14, d , geckal(gecmepuani1, d)[0],
                                        ders15,vize15, final15, e , geckal(gecmepuani1, e)[0],
                                        ders16,vize16, final16, f , geckal(gecmepuani1, f)[0],
                                        ders17,vize17, final17, g , geckal(gecmepuani1, g)[0], gecmepuani1)
            with open(isim , "w+") as dosya :
                dosya.write(aaa)
            ms.showinfo("Kayit Edildi" , "{} olarak kayit edildi".format(isim))

        def kontrol (gelenpuan) :
            if gelenpuan > 100 or gelenpuan < 0 :
                ms.showwarning("Dikkat" , "--> Puan Değeri, Yüzde, Geçme puanı 100 den fazla olamaz")
                return False


        isim11 = isim.get().title()
        Sisim11 = Sisim.get().title()
        ders11 = ders1.get().title()
        ders12 = ders2.get().title()
        ders13 = ders3.get().title()
        ders14 = ders4.get().title()
        ders15 = ders5.get().title()
        ders16 = ders6.get().title()
        ders17 = ders7.get().title()
        fyuzde = int(finalortalama.get())
        vyuzde = int(vizeortalama.get())
        final11= int(final1.get())
        final12= int(final2.get())
        final13=int(final3.get())
        final14=int(final4.get())
        final15=int(final5.get())
        final16=int(final6.get())
        final17=int(final7.get())
        vize11 = int(vize1.get() )
        vize12 = int(vize2.get())
        vize13 = int(vize3.get())
        vize14 = int(vize4.get())
        vize15 = int(vize5.get())
        vize16 = int(vize6.get())
        vize17 = int(vize7.get())
        gecmepuani1 = int(gecmepuani.get())
        lvize1["text"] = (vize11 * vyuzde / 100)
        lvize2["text"] = (vize12 * vyuzde / 100)
        lvize3["text"] = (vize13 * vyuzde / 100)
        lvize4["text"] = (vize14 * vyuzde / 100)
        lvize5["text"] = (vize15 * vyuzde / 100)
        lvize6["text"] = (vize16 * vyuzde / 100)
        lvize7["text"] = (vize17 * vyuzde / 100) 
        lfinal1["text"] = (final11 * fyuzde / 100)
        lfinal2["text"] = (final12 * fyuzde / 100)
        lfinal3["text"] = (final13 * fyuzde / 100)
        lfinal4["text"] = (final14 * fyuzde / 100)
        lfinal5["text"] = (final15 * fyuzde / 100)
        lfinal6["text"] = (final16 * fyuzde / 100)
        lfinal7["text"] = (final17 * fyuzde / 100)
        lgecmepuani["text"] ="Gecme Puani --> {}".format(gecmepuani1)
        lisim.configure(font="Ariel 18 bold" , text= isim11)
        lSisim.configure(font="Ariel 18 bold" , text=Sisim11 )
        #sayıların 100 den fazla olmaması kontrol ediliyor
        ytoplam = fyuzde + vyuzde
        kontrollistesi=[vize11,vize12,vize13,vize14,vize15,vize16,vize17,final11,final12,final13,final14,final15,final16,final17, ytoplam , gecmepuani1]
        for ata in kontrollistesi:
            if kontrol(ata) == False:
                break
                
                
        lders1["text"] = ders11
        lders2["text"] = ders12
        lders3["text"] = ders13
        lders4["text"] = ders14
        lders5["text"] = ders15
        lders6["text"] = ders16
        lders7["text"] = ders17
        a= (vize11 * vyuzde / 100) + (final11 * fyuzde / 100)
        b=(vize12 * vyuzde / 100) + (final12 * fyuzde / 100)
        c=(vize13 * vyuzde / 100) + (final13 * fyuzde / 100)
        d=(vize14 * vyuzde / 100) + (final14 * fyuzde / 100)
        e=(vize15 * vyuzde / 100) + (final15 * fyuzde / 100)
        f=(vize16 * vyuzde / 100) + (final16 * fyuzde / 100)
        g=(vize17 * vyuzde / 100) + (final17 * fyuzde / 100)
        lort1["text"] = a 
        lort2["text"] = b
        lort3["text"] = c
        lort4["text"] = d
        lort5["text"] = e
        lort6["text"] = f
        lort7["text"] = g
        drm1.configure(text=geckal(gecmepuani1, a)[0] , bg=geckal(gecmepuani1, a)[1], fg= "black")
        drm2.configure(text=geckal(gecmepuani1, b)[0] , bg=geckal(gecmepuani1, b)[1], fg= "black")
        drm3.configure(text=geckal(gecmepuani1, c)[0] , bg=geckal(gecmepuani1, c)[1], fg= "black")
        drm4.configure(text=geckal(gecmepuani1, d)[0] , bg=geckal(gecmepuani1, d)[1], fg= "black")
        drm5.configure(text=geckal(gecmepuani1, e)[0] , bg=geckal(gecmepuani1, e)[1], fg= "black")
        drm6.configure(text=geckal(gecmepuani1, f)[0] , bg=geckal(gecmepuani1, f)[1], fg= "black")
        drm7.configure(text=geckal(gecmepuani1, g)[0] , bg=geckal(gecmepuani1, g)[1], fg= "black")
        kaydet = tk.Button(ust , text="Kaydet" , command = Kaydet , bg="white", fg="black" ,font="Ariel").place(x=475, y=350)

    except ValueError:
        ms.showwarning("Dikkat","Sanırım Puan yerine Türkçe karakter girildi !!!")







pen = tk.Tk()
pen.geometry("600x810+200+100")
pen.title("Vize Final Hesaplama")

ust = tk.Frame(pen , width=550 , height=400, bg="white" ).place(x=25 , y=10)
tk.Label(ust , text="ÖGRENCİ BİLGİLERİ", fg="black", bg="white",font="Ariel" ).place(x=200 , y=15)

tk.Label(ust , text="İsim    -->" , fg="black" , bg="white", font="Ariel").place(x=35, y=50)
isim = tk.Entry(ust ,bg="white",fg="black")
isim.place(x=120, y=50)

tk.Label(ust , text="Soyisim->" , fg="black" , bg="white", font="Ariel").place(x=35, y=75)
Sisim = tk.Entry(ust ,bg="white",fg="black")
Sisim.place(x=120, y=75)

tk.Label(ust, text="Geçme Puanı -->" , bg="white" ,fg="black" ).place(x=350,y=50)
gecmepuani = tk.Entry(ust, bg="white", fg="black", width=5 )
gecmepuani.place(x=470 , y=50)


tk.Label(ust , text="Ders İsimleri" , bg="white", fg="black", font="Ariel").place(x=100, y=125)
ders1 = tk.Entry(ust ,bg="white",fg="black")
ders1.place(x=50, y=150)
ders2= tk.Entry(ust ,bg="white",fg="black")
ders2.place(x=50, y=175)
ders3 = tk.Entry(ust ,bg="white",fg="black")
ders3.place(x=50, y=200)
ders4 = tk.Entry(ust ,bg="white",fg="black")
ders4.place(x=50, y=225)
ders5 = tk.Entry(ust ,bg="white",fg="black")
ders5.place(x=50, y=250)
ders6= tk.Entry(ust ,bg="white",fg="black")
ders6.place(x=50, y=275)
ders7= tk.Entry(ust ,bg="white",fg="black")
ders7.place(x=50, y=300)

tk.Label(ust , text="Vize" , fg="black", bg="white" ,font="Ariel" ).place(x=320 , y=125) 
vize1= tk.Entry(ust ,bg="white",fg="black", width=7)
vize1.place(x=300, y=150)
vize2= tk.Entry(ust ,bg="white",fg="black", width=7)
vize2.place(x=300, y=175)
vize3= tk.Entry(ust ,bg="white",fg="black", width=7)
vize3.place(x=300, y=200)
vize4= tk.Entry(ust ,bg="white",fg="black", width=7)
vize4.place(x=300, y=225)
vize5= tk.Entry(ust ,bg="white",fg="black", width=7)
vize5.place(x=300, y=250)
vize6= tk.Entry(ust ,bg="white",fg="black", width=7)
vize6.place(x=300, y=275)
vize7= tk.Entry(ust ,bg="white",fg="black", width=7)
vize7.place(x=300, y=300)

tk.Label(ust , text="Final" , fg="black", bg="white" ,font="Ariel" ).place(x=430 , y=125) 
final1= tk.Entry(ust ,bg="white",fg="black", width=7)
final1.place(x=420, y=150)
final2= tk.Entry(ust ,bg="white",fg="black", width=7)
final2.place(x=420, y=175)
final3= tk.Entry(ust ,bg="white",fg="black", width=7)
final3.place(x=420, y=200)
final4= tk.Entry(ust ,bg="white",fg="black", width=7)
final4.place(x=420, y=225)
final5= tk.Entry(ust ,bg="white",fg="black", width=7)
final5.place(x=420, y=250)
final6= tk.Entry(ust ,bg="white",fg="black", width=7)
final6.place(x=420, y=275)
final7= tk.Entry(ust ,bg="white",fg="black", width=7)
final7.place(x=420, y=300)

tk.Label(ust, text="Vize  %" , bg="white" , fg="black").place(x=50, y=340) 
vizeortalama= tk.Entry(ust , bg="white", fg="black", width=7)
vizeortalama.place(x=101, y=340)

tk.Label(ust, text="Final %" , bg="white" , fg="black").place(x=50, y=365) 
finalortalama = tk.Entry(ust , bg="white", fg="black", width=7)
finalortalama.place(x=101, y=365)

tk.Button(ust , text="Hesapla" , command = Hesapla , bg="white", fg="black" ,font="Ariel").place(x=370, y=350)


#Alt Menu Frame

alt = tk.Frame(pen , width=600 , height=380 , bg="yellow" ).place(x=0, y=420)

lisim = tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lisim.place(x=200, y=420)
lSisim= tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lSisim.place(x=350, y=420)

tk.Label(alt, text="Dersler" , font="Ariel 13 bold" , bg="yellow", fg="red" ).place(x=60, y=470)
lders1 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lders1.place(x=75, y=500)
lders2 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lders2.place(x=75, y=520)
lders3 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lders3.place(x=75, y=540)
lders4 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lders4.place(x=75, y=560)
lders5 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lders5.place(x=75, y=580)
lders6 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lders6.place(x=75, y=600)
lders7 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lders7.place(x=75, y=620)


tk.Label(alt, text="Vize" , font="Ariel 13 bold" , bg="yellow", fg="red" ).place(x=205, y=470)
lvize1 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lvize1.place(x=200, y=500)
lvize2 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lvize2.place(x=200, y=520)
lvize3 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lvize3.place(x=200, y=540)
lvize4 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lvize4.place(x=200, y=560)
lvize5 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lvize5.place(x=200, y=580)
lvize6 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lvize6.place(x=200, y=600)
lvize7 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lvize7.place(x=200, y=620)

tk.Label(alt, text="Final" , font="Ariel 13 bold" , bg="yellow", fg="red" ).place(x=305, y=470)
lfinal1 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lfinal1.place(x=300, y=500)
lfinal2=tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lfinal2.place(x=300, y=520)
lfinal3=tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lfinal3.place(x=300, y=540)
lfinal4=tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lfinal4.place(x=300, y=560)
lfinal5 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lfinal5.place(x=300, y=580)
lfinal6=tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lfinal6.place(x=300, y=600)
lfinal7 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lfinal7.place(x=300, y=620)

tk.Label(alt, text="Toplam" , font="Ariel 13 bold" , bg="yellow", fg="red" ).place(x=380, y=470)
lort1 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lort1.place(x=400, y=500)
lort2=tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lort2.place(x=400, y=520)
lort3=tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lort3.place(x=400, y=540)
lort4=tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lort4.place(x=400, y=560)
lort5 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lort5.place(x=400, y=580)
lort6=tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lort6.place(x=400, y=600)
lort7 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
lort7.place(x=400, y=620)

tk.Label(alt, text="Durum" , font="Ariel 13 bold" , bg="yellow", fg="red" ).place(x=505, y=470)
drm1 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
drm1.place(x=500, y=500)
drm2=tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
drm2.place(x=500, y=520)
drm3=tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
drm3.place(x=500, y=540)
drm4=tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
drm4.place(x=500, y=560)
drm5 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
drm5.place(x=500, y=580)
drm6=tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
drm6.place(x=500, y=600)
drm7 =tk.Label(alt, text="" , font="Ariel" , bg="yellow", fg="Black" )
drm7.place(x=500, y=620)

lgecmepuani = tk.Label(alt, text="Gecme Puani --> ", font="Ariel 15 bold" , bg="yellow", fg="Black")
lgecmepuani.place(x=150, y=750)

pen.mainloop()
