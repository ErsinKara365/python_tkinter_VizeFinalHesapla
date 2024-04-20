import time 
import os
import sys
import tkinter as tk
from tkinter import messagebox as ms

global ders1, ders2, ders3 , ders4, ders5, ders6, ders7, ders8, ders9, ders10 , ders11 , ders12
global pen, vizeortalama, finalortalama
global vize1, vize2, vize3, vize4, vize5, vize6, vize7, vize8, vize9, vize10, vize11, vize12
global final1 ,final2 , final3 ,final4 , final5, final6, final7, final8, final9, final10, final11, final12


def hesapla(sinav ):
    global vpuan1,vpuan2,vpuan3,vpuan4,vpuan5,vpuan6,vpuan7,vpuan8,vpuan9,vpuan10,vpuan11,vpuan12


    try :

        if(sinav == "vize1"):
            puanv1 = int(vize1.get())
            oranv1 = int(voran1.get())
            vpuan1 = ((puanv1*oranv1)/100)
            tk.Label(sonucFrame, text=vpuan1, bg="yellow").place(x=590, y=75)
        if(sinav == "vize2"):
            puanv2 = int(vize2.get())
            oranv2 = int(voran2.get())
            vpuan2 = ((puanv2*oranv2)/100)
            tk.Label(sonucFrame, text=vpuan2, bg="yellow").place(x=590, y=100)
        if(sinav == "vize3"):
            puanv3 = int(vize3.get())
            oranv3 = int(voran3.get())
            vpuan3 =((puanv3*oranv3)/100)
            tk.Label(sonucFrame, text=vpuan3, bg="yellow").place(x=590, y=125)
        if(sinav == "vize4"):
            puanv4 = int(vize4.get())
            oranv4 = int(voran4.get())
            vpuan4 =((puanv4*oranv4)/100)
            tk.Label(sonucFrame, text=vpuan4, bg="yellow").place(x=590, y=150)
        if(sinav == "vize5"):
            puanv5 = int(vize5.get())
            oranv5 = int(voran5.get())
            vpuan5 =((puanv5*oranv5)/100)
            tk.Label(sonucFrame, text=vpuan5, bg="yellow").place(x=590, y=175)
        if(sinav == "vize6"):
            puanv6 = int(vize6.get())
            oranv6 = int(voran6.get())
            vpuan6 =((puanv6*oranv6)/100)
            tk.Label(sonucFrame, text=vpuan6, bg="yellow").place(x=590, y=200)
        if(sinav == "vize7"):
            puanv7= int(vize7.get())
            oranv7 = int(voran7.get())
            vpuan7=((puanv7*oranv7)/100)
            tk.Label(sonucFrame, text=vpuan7, bg="yellow").place(x=590, y=225)
        if(sinav == "vize8"):
            puanv8 = int(vize8.get())
            oranv8 = int(voran8.get())
            vpuan8=((puanv8*oranv8)/100)
            tk.Label(sonucFrame, text=vpuan8, bg="yellow").place(x=590, y=250)
        if(sinav == "vize9"):
            puanv9 = int(vize9.get())
            oranv9 = int(voran9.get())
            vpuan9=((puanv9*oranv9)/100)
            tk.Label(sonucFrame, text=vpuan9, bg="yellow").place(x=590, y=275)
        if(sinav == "vize10"):
            puanv10 = int(vize10.get())
            oranv10 = int(voran10.get())
            vpuan10=((puanv10*oranv10)/100)
            tk.Label(sonucFrame, text=vpuan10, bg="yellow").place(x=590, y=300)
        if(sinav == "vize11"):
            puanv11 = int(vize11.get())
            oranv11 = int(voran11.get())
            vpuan11=((puanv11*oranv11)/100)
            tk.Label(sonucFrame, text=vpuan11, bg="yellow").place(x=590, y=325)
        if(sinav == "vize12"):
            puanv12 = int(vize12.get())
            oranv12 = int(voran12.get())
            vpuan12 =((puanv12*oranv12)/100)
            tk.Label(sonucFrame, text=vpuan12, bg="yellow").place(x=590, y=350)
    except ValueError :
        pass

    
    try:
        if (sinav == "final1") :
            puanf1 = int(final1.get())
            oranf1 = int(foran1.get())
            fpuan1 = ((puanf1*oranf1)/100)
            tk.Label(sonucFrame, text=fpuan1, bg="yellow").place(x=660, y=75)
            tk.Label(sonucFrame, text=(fpuan1 + vpuan1), bg="yellow").place(x=750, y=75)
        if (sinav == "final2") :
            puanf2 = int(final2.get())
            oranf2 = int(foran2.get())
            fpuan2 = ((puanf2*oranf2)/100)
            tk.Label(sonucFrame, text=fpuan2, bg="yellow").place(x=660, y=100)
            tk.Label(sonucFrame, text=(fpuan2 + vpuan2), bg="yellow").place(x=750, y=100)
        if (sinav == "final3") :
            puanf3 = int(final3.get())
            oranf3 = int(foran3.get())
            fpuan3 = ((puanf3*oranf3)/100)
            tk.Label(sonucFrame, text=fpuan3, bg="yellow").place(x=660, y=125)
            tk.Label(sonucFrame, text=(fpuan3 + vpuan3), bg="yellow").place(x=750, y=125)
        if (sinav == "final4") :
            puanf4 = int(final4.get())
            oranf4 = int(foran4.get())
            fpuan4 = ((puanf4*oranf4)/100)
            tk.Label(sonucFrame, text=fpuan4, bg="yellow").place(x=660, y=150)
            tk.Label(sonucFrame, text=(fpuan4 + vpuan4), bg="yellow").place(x=750, y=150)
        if (sinav == "final5") :
            puanf5 = int(final5.get())
            oranf5 = int(foran5.get())
            fpuan5 = ((puanf5*oranf5)/100)
            tk.Label(sonucFrame, text=fpuan5, bg="yellow").place(x=660, y=175)
            tk.Label(sonucFrame, text=(fpuan5 + vpuan5), bg="yellow").place(x=750, y=175)
        if (sinav == "final6") :
            puanf6 = int(final6.get())
            oranf6 = int(foran6.get())
            fpuan6 = ((puanf6*oranf6)/100)
            tk.Label(sonucFrame, text=fpuan6, bg="yellow").place(x=660, y=200)
            tk.Label(sonucFrame, text=(fpuan6 + vpuan6), bg="yellow").place(x=750, y=200)
        if (sinav == "final7") :
            puanf7 = int(final7.get())
            oranf7 = int(foran7.get())
            fpuan7 = ((puanf7*oranf7)/100)
            tk.Label(sonucFrame, text=fpuan7, bg="yellow").place(x=660, y=225)
            tk.Label(sonucFrame, text=(fpuan7 + vpuan7), bg="yellow").place(x=750, y=225)
        if (sinav == "final8") :
            puanf8 = int(final8.get())
            oranf8 = int(foran8.get())
            fpuan8 = ((puanf8*oranf8)/100)
            tk.Label(sonucFrame, text=fpuan8, bg="yellow").place(x=660, y=250)
            tk.Label(sonucFrame, text=(fpuan8 + vpuan8), bg="yellow").place(x=750, y=250)
        if (sinav == "final9") :
            puanf9 = int(final9.get())
            oranf9 = int(foran9.get())
            fpuan9 = ((puanf9*oranf9)/100)
            tk.Label(sonucFrame, text=fpuan9, bg="yellow").place(x=660, y=275)
            tk.Label(sonucFrame, text=(fpuan9 + vpuan9), bg="yellow").place(x=750, y=275)
        if (sinav == "final10") :
            puanf10 = int(final10.get())
            oranf10 = int(foran10.get())
            fpuan10 = ((puanf10*oranf10)/100)
            tk.Label(sonucFrame, text=fpuan10, bg="yellow").place(x=660, y=300)
            tk.Label(sonucFrame, text=(fpuan10 + vpuan10), bg="yellow").place(x=750, y=300)
        if (sinav == "final11") :
            puanf11 = int(final11.get())
            oranf11 = int(foran11.get())
            fpuan11 = ((puanf11*oranf11)/100)
            tk.Label(sonucFrame, text=fpuan11, bg="yellow").place(x=660, y=325)
            tk.Label(sonucFrame, text=(fpuan11 + vpuan11), bg="yellow").place(x=750, y=325)
        if (sinav == "final12") :
            puanf12 = int(final12.get())
            oranf12 = int(foran12.get())
            fpuan12 = ((puanf12*oranf12)/100)
            tk.Label(sonucFrame, text=fpuan12, bg="yellow").place(x=660, y=350)
            tk.Label(sonucFrame, text=(fpuan12 + vpuan12), bg="yellow").place(x=750, y=350)
    except ValueError :
        pass

pen = tk.Tk()
pen.geometry("900x500+200+100")
pen.resizable(width="FALSE", height="FALSE")
pen.title("Vize Final Hesaplama")

dersFrame = tk.Frame(pen, width=290, height=500, bg="yellow").place(x=0, y=0)
tk.Label(pen , text="Ders İsimleri" , font="Ariel", bg="yellow" ).place(x=75, y=25)
ders1 = tk.Entry(pen)
ders1.place(x=50, y=75)
ders2= tk.Entry(pen)
ders2.place(x=50, y=100)
ders3 = tk.Entry(pen)
ders3.place(x=50, y=125)
ders4 = tk.Entry(pen)
ders4.place(x=50, y=150)
ders5 = tk.Entry(pen)
ders5.place(x=50, y=175)
ders6= tk.Entry(pen)
ders6.place(x=50, y=200)
ders7= tk.Entry(pen)
ders7.place(x=50, y=225)
ders8 = tk.Entry(pen)
ders8.place(x=50, y=250)
ders9= tk.Entry(pen)
ders9.place(x=50, y=275)
ders10= tk.Entry(pen)
ders10.place(x=50, y=300)
ders11= tk.Entry(pen)
ders11.place(x=50, y=325)
ders12= tk.Entry(pen)
ders12.place(x=50, y=350)

vizeFrame = tk.Frame(pen, width=155, height=500, bg="blue").place(x=260, y=0)

tk.Label(pen , text="Vize" ,font="Ariel" ,bg="blue", fg="white" ).place(x=275 , y=25) 
tk.Label(pen , text="(Oran)" , font="Ariel" , bg="blue", fg="white").place(x=271 , y=47)

voran1= tk.Entry(vizeFrame ,width=7)
voran1.place(x=270, y=75)
voran2= tk.Entry(vizeFrame ,width=7)
voran2.place(x=270, y=100)
voran3= tk.Entry(vizeFrame ,width=7)
voran3.place(x=270, y=125)
voran4= tk.Entry(vizeFrame ,width=7)
voran4.place(x=270, y=150)
voran5= tk.Entry(vizeFrame ,width=7)
voran5.place(x=270, y=175)
voran6= tk.Entry(vizeFrame ,width=7)
voran6.place(x=270, y=200)
voran7= tk.Entry(vizeFrame ,width=7)
voran7.place(x=270, y=225)
voran8= tk.Entry(vizeFrame ,width=7)
voran8.place(x=270, y=250)
voran9= tk.Entry(vizeFrame ,width=7)
voran9.place(x=270, y=275)
voran10= tk.Entry(vizeFrame ,width=7)
voran10.place(x=270, y=300)
voran11= tk.Entry(vizeFrame ,width=7)
voran11.place(x=270, y=325)
voran12= tk.Entry(vizeFrame ,width=7)
voran12.place(x=270, y=350)


tk.Label(vizeFrame , text="Vize" ,font="Ariel" , bg="blue" ,fg="white").place(x=350 , y=25) 
tk.Label(vizeFrame , text="(Puan)" , font="Ariel" ,bg="blue", fg="white").place(x=345 , y=47)

vize1= tk.Entry(vizeFrame ,width=7)
vize1.bind("<FocusOut>", lambda event: hesapla("vize1") )
vize1.place(x=345, y=75)
vize2= tk.Entry(vizeFrame ,width=7)
vize2.bind("<FocusOut>", lambda event: hesapla("vize2") )
vize2.place(x=345, y=100)
vize3= tk.Entry(vizeFrame ,width=7)
vize3.bind("<FocusOut>", lambda event: hesapla("vize3") )
vize3.place(x=345, y=125)
vize4= tk.Entry(vizeFrame ,width=7)
vize4.bind("<FocusOut>", lambda event: hesapla("vize4") )
vize4.place(x=345, y=150)
vize5= tk.Entry(vizeFrame ,width=7)
vize5.bind("<FocusOut>", lambda event: hesapla("vize5") )
vize5.place(x=345, y=175)
vize6= tk.Entry(vizeFrame ,width=7)
vize6.bind("<FocusOut>", lambda event: hesapla("vize6") )
vize6.place(x=345, y=200)
vize7= tk.Entry(vizeFrame ,width=7)
vize7.bind("<FocusOut>", lambda event: hesapla("vize7") )
vize7.place(x=345, y=225)
vize8= tk.Entry(vizeFrame ,width=7)
vize8.bind("<FocusOut>", lambda event: hesapla("vize8") )
vize8.place(x=345, y=250)
vize9= tk.Entry(vizeFrame ,width=7)
vize9.bind("<FocusOut>", lambda event: hesapla("vize9") )
vize9.place(x=345, y=275)
vize10= tk.Entry(vizeFrame ,width=7)
vize10.bind("<FocusOut>", lambda event: hesapla("vize10") )
vize10.place(x=345, y=300)
vize11= tk.Entry(vizeFrame ,width=7)
vize11.bind("<FocusOut>", lambda event: hesapla("vize11") )
vize11.place(x=345, y=325)
vize12= tk.Entry(vizeFrame ,width=7)
vize12.bind("<FocusOut>", lambda event: hesapla("vize12") )
vize12.place(x=345, y=350)



finalFrame = tk.Frame(pen, width=150, height=500, bg="purple").place(x=415, y=0)

tk.Label(finalFrame , text="Final" , font="Ariel" , bg="purple" , fg="white").place(x=432 , y=25) 
tk.Label(finalFrame , text="(Oran)" , font="Ariel" , bg="purple" , fg="white").place(x=428 , y=47) 

foran1= tk.Entry(finalFrame ,width=7)
foran1.place(x=420, y=75)
foran2= tk.Entry(finalFrame ,width=7)
foran2.place(x=420, y=100)
foran3= tk.Entry(finalFrame ,width=7)
foran3.place(x=420, y=125)
foran4= tk.Entry(finalFrame ,width=7)
foran4.place(x=420, y=150)
foran5= tk.Entry(finalFrame ,width=7)
foran5.place(x=420, y=175)
foran6= tk.Entry(finalFrame ,width=7)
foran6.place(x=420, y=200)
foran7= tk.Entry(finalFrame ,width=7)
foran7.place(x=420, y=225)
foran8= tk.Entry(finalFrame ,width=7)
foran8.place(x=420, y=250)
foran9= tk.Entry(finalFrame ,width=7)
foran9.place(x=420, y=275)
foran10= tk.Entry(finalFrame ,width=7)
foran10.place(x=420, y=300)
foran11= tk.Entry(finalFrame ,width=7)
foran11.place(x=420, y=325)
foran12= tk.Entry(finalFrame ,width=7)
foran12.place(x=420, y=350)


tk.Label(finalFrame , text="Final" , font="Ariel" , bg="purple" , fg="white") .place(x=500 , y=25) 
tk.Label(finalFrame , text="(Puan)" , font="Ariel" , bg="purple" , fg="white").place(x=495 , y=47) 

final1= tk.Entry(finalFrame ,width=7)
final1.bind("<FocusOut>", lambda event: hesapla ("final1"))
final1.place(x=490, y=75)
final2= tk.Entry(finalFrame ,width=7)
final2.bind("<FocusOut>", lambda event: hesapla ("final2"))
final2.place(x=490, y=100)
final3= tk.Entry(finalFrame ,width=7)
final3.bind("<FocusOut>", lambda event: hesapla ("final3"))
final3.place(x=490, y=125)
final4= tk.Entry(finalFrame ,width=7)
final4.bind("<FocusOut>", lambda event: hesapla ("final4"))
final4.place(x=490, y=150)
final5= tk.Entry(finalFrame ,width=7)
final5.bind("<FocusOut>", lambda event: hesapla ("final5"))
final5.place(x=490, y=175)
final6= tk.Entry(finalFrame ,width=7)
final6.bind("<FocusOut>", lambda event: hesapla ("final6"))
final6.place(x=490, y=200)
final7= tk.Entry(finalFrame ,width=7)
final7.bind("<FocusOut>", lambda event: hesapla ("final7"))
final7.place(x=490, y=225)
final8= tk.Entry(finalFrame ,width=7)
final8.bind("<FocusOut>", lambda event: hesapla ("final8"))
final8.place(x=490, y=250)
final9= tk.Entry(finalFrame ,width=7)
final9.bind("<FocusOut>", lambda event: hesapla ("final9"))
final9.place(x=490, y=275)
final10= tk.Entry(finalFrame ,width=7)
final10.bind("<FocusOut>", lambda event: hesapla ("final10"))
final10.place(x=490, y=300)
final11= tk.Entry(finalFrame ,width=7)
final11.bind("<FocusOut>", lambda event: hesapla ("final11"))
final11.place(x=490, y=325)
final12= tk.Entry(finalFrame ,width=7)
final12.bind("<FocusOut>", lambda event: hesapla ("final12"))
final12.place(x=490, y=350)

sonucFrame = tk.Frame(pen, width=350, height=500, bg="yellow").place(x=560, y=0)
tk.Label(sonucFrame, text="Vize", bg="yellow", font=("Arial",15)).place(x=585, y=30)

tk.Label(sonucFrame, text="Final", bg="yellow", font=("Arial",15)).place(x=655, y=30)
tk.Label(sonucFrame, text="Toplam", bg="yellow", font=("Arial",15)).place(x=750, y=30)


pen.mainloop()


