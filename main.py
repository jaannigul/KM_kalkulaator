try:  #proovib kas ttkbootstrap on juba installeeritud, kui mitte, siis installeerib selle
    import ttkbootstrap as ttk #pip install ttkbootstrap
except ImportError:
    import subprocess
    import sys
    def install(package): #vajadusel installeerib puuduolevad moodulid
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    install('ttkbootstrap') #
    import ttkbootstrap as ttk #pip install ttkbootstrap
import tkinter as tk

import funktsioonid

#funktsioonid paigutuseks 
def vahetus_vk_raami():
    vk_tiitel.place(x=300,y=40)
    vk_vektor1_tekst.place(x=300,y=80)
    
    vk_vektor1x.place(x=360,y=80)
    vk_vektor1y.place(x=360+INPUT_MARGIN_X,y=80)
    vk_vektor1z.place(x=360+INPUT_MARGIN_X*2,y=80)
    
    vk_vektor2_tekst.place(x=300,y=110)
    
    vk_vektor2x.place(x=360,y=80+INPUT_MARGIN_Y)
    vk_vektor2y.place(x=360+INPUT_MARGIN_X,y=80+INPUT_MARGIN_Y)
    vk_vektor2z.place(x=360+INPUT_MARGIN_X*2,y=80+INPUT_MARGIN_Y)
    
    vk_nupp_arvuta.place(x=360,y=160)
    vk_kuva_vastus.place(x=460,y=160)
    #kõik muu paigutus tuleb unustada
    sk_tiitel.place_forget()
    sk_x1.place_forget()
    sk_y1.place_forget()
    sk_z1.place_forget()
    sk_x2.place_forget()
    sk_y2.place_forget()
    sk_z2.place_forget()
    sk_x3.place_forget()
    sk_y3.place_forget()
    sk_z3.place_forget()
    sk_kuva_vastus.place_forget()
    sk_nupp_arvuta.place_forget()
    
    

def vahetus_sk_raami():
    sk_tiitel.place(x=300,y=40)
    
    sk_x1.place(x=360,y=80)
    sk_y1.place(x=360+INPUT_MARGIN_X, y=80)
    sk_z1.place(x=360+INPUT_MARGIN_X*2, y=80)

    sk_x2.place(x=360,y=80+INPUT_MARGIN_Y)
    sk_y2.place(x=360+INPUT_MARGIN_X, y=80+INPUT_MARGIN_Y)
    sk_z2.place(x=360+INPUT_MARGIN_X*2, y=80+INPUT_MARGIN_Y)

    sk_x3.place(x=360, y=80+INPUT_MARGIN_Y*2)
    sk_y3.place(x=360+INPUT_MARGIN_X, y=80+INPUT_MARGIN_Y*2)
    sk_z3.place(x=360+INPUT_MARGIN_X*2, y=80+INPUT_MARGIN_Y*2)
    sk_nupp_arvuta.place(x=360, y=200) #muuda millalgi 
    sk_kuva_vastus.place(x=460, y=200)
    #kõik muu paigutus tuleb unustada
    vk_tiitel.place_forget()
    vk_vektor1x.place_forget()
    vk_vektor1y.place_forget()
    vk_vektor1z.place_forget()
    vk_vektor1_tekst.place_forget()
    vk_vektor2x.place_forget()
    vk_vektor2y.place_forget()
    vk_vektor2z.place_forget()
    vk_vektor2_tekst.place_forget()
    vk_nupp_arvuta.place_forget()
    vk_kuva_vastus.place_forget()

def vk_input(): #võtab inputi lahtritest
    try:
        vastus=funktsioonid.vektorkorrutis(
            float(vk_vektor1x.get()),
            float(vk_vektor1y.get()),
            float(vk_vektor1z.get()),
            float(vk_vektor2x.get()),
            float(vk_vektor2y.get()),
            float(vk_vektor2z.get()),
        )
        vk_kuva_vastus.configure(text=f"{vastus}")
    except:
        vk_kuva_vastus.configure(text="Vale sisend")
def sk_input():
    try:
        vastus=funktsioonid.segakorrutis(
            float(sk_x1.get()),
            float(sk_y1.get()),
            float(sk_z1.get()),
            
            float(sk_x2.get()),
            float(sk_y2.get()),
            float(sk_z2.get()),
            
            float(sk_x3.get()),
            float(sk_y3.get()),
            float(sk_z3.get()),
            )
        sk_kuva_vastus.configure(text=f"{vastus}")
    except:
        sk_kuva_vastus.configure(text="Vale sisend")
def tjärkudet_input():
    try:
        vastus=funktsioonid.det2(
            float(tdet_a11.get()), 
            float(tdet_a12.get()),
            float(tdet_a21.get()),
            float(tdet_a22.get())
            )
        tjärkudet_kuva_vastus.configure(text=f"{vastus}")
    except: tjärkudet_kuva_vastus.configure(text="Vale Sisend")
def kjärkudet_input():
    try:
        vastus=funktsioonid.det3(
            float(kdet_a11.get()), 
            float(kdet_a12.get()),
            float(kdet_a13.get()),
            
            float(kdet_a21.get()),
            float(kdet_a22.get()),
            float(kdet_a23.get()),
            
            float(kdet_a31.get()),
            float(kdet_a32.get()),
            float(kdet_a33.get())
            )
        kjärkudet_kuva_vastus.configure(text=f"{vastus}")
    except: kjärkudet_kuva_vastus.configure(text="Vale Sisend")
def njärkudet_input():
    try:
        vastus=funktsioonid.det3(
            float(ndet_a11.get()), 
            float(ndet_a12.get()),
            float(ndet_a13.get()),
            float(ndet_a14.get()),
            
            float(ndet_a21.get()),
            float(ndet_a22.get()),
            float(ndet_a23.get()),
            float(ndet_a24.get()),
            
            float(ndet_a31.get()),
            float(ndet_a32.get()),
            float(ndet_a33.get()),
            float(ndet_a34.get()),
            
            float(ndet_a41.get()),
            float(ndet_a42.get()),
            float(ndet_a43.get()),
            float(ndet_a44.get())
            
            )
        njärkudet_kuva_vastus.configure(text=f"{vastus}")
    except: njärkudet_kuva_vastus.configure(text="Vale Sisend")
def vjärkudet_input():
    try:
        vastus=funktsioonid.det3(
            float(vdet_a11.get()), 
            float(vdet_a12.get()),
            float(vdet_a13.get()),
            float(vdet_a14.get()),
            float(vdet_a15.get()),
            
            float(vdet_a21.get()),
            float(vdet_a22.get()),
            float(vdet_a23.get()),
            float(vdet_a24.get()),
            float(vdet_a25.get()),
            
            float(vdet_a31.get()),
            float(vdet_a32.get()),
            float(vdet_a33.get()),
            float(vdet_a34.get()),
            float(vdet_a35.get()),
            
            float(vdet_a41.get()),
            float(vdet_a42.get()),
            float(vdet_a43.get()),
            float(vdet_a44.get()),
            float(vdet_a45.get()),
            
            )
        vjärkudet_kuva_vastus.configure(text=f"{vastus}")
    except: vjärkudet_kuva_vastus.configure(text="Vale Sisend")
def vahetus_det2_raami():
    tjärkudet_tiitel.place(x=300,y=40)
def vahetus_det3_raami():
    kjärkudet_tiitel.place(x=300,y=40)
def vahetus_det4_raami():
    njärkudet_tiitel.place(x=300,y=40)
def vahetus_det5_raami():
    vjärkudet_tiitel.place(x=300,y=40)
def det_menu(valik):
    valik=detlabel.get()
    if valik=="2. järku determinant":
        vahetus_det2_raami()
    if valik=="3. järku determinant":
        vahetus_det3_raami()
    if valik=="4. järku determinant":
        vahetus_det4_raami()
    if valik=="5. järku determinant":
        vahetus_det5_raami()
BUTTON_WIDTH=30
BUTTON_MARGIN=40
INPUT_MARGIN_X=55
INPUT_MARGIN_Y=35
#GUI
root=tk.Tk()
root.geometry("800x400") #akna suurus
root.title("Kalkulaatorid") #peaakna tiitel
style = ttk.Style("darkly") #stiilid: https://ttkbootstrap.readthedocs.io/en/latest/themes/dark/
root.resizable(False, False)

#muutujad ja widgetid
#vektorkorrutis
vk_tiitel = ttk.Label(root, text="Vektorkorrutis")

vk_vektor1x=ttk.Entry(root, width=6)
vk_vektor1y=ttk.Entry(root, width=6)
vk_vektor1z=ttk.Entry(root, width=6)

vk_vektor1_tekst=tk.Label(root,text="Vektor 1:")

vk_vektor2x=ttk.Entry(root, width=6)
vk_vektor2y=ttk.Entry(root, width=6)
vk_vektor2z=ttk.Entry(root, width=6)

vk_vektor2_tekst=tk.Label(root,text="Vektor 2:")
vk_nupp_arvuta=ttk.Button(root,text="Arvuta",command=vk_input)
vk_kuva_vastus=tk.Label(root)

#segakorrutis TODO: label igale koordinaadile (x y z), vektor 1-3 label, lahtrite puhastus
sk_tiitel=ttk.Label(root, text="Segakorrutis")
sk_x1=ttk.Entry(root, width=6)
sk_y1=ttk.Entry(root, width=6)
sk_z1=ttk.Entry(root, width=6)

sk_x2=ttk.Entry(root, width=6)
sk_y2=ttk.Entry(root, width=6)
sk_z2=ttk.Entry(root, width=6)

sk_x3=ttk.Entry(root, width=6)
sk_y3=ttk.Entry(root, width=6)
sk_z3=ttk.Entry(root, width=6)

sk_nupp_arvuta=ttk.Button(root,text="Arvuta",command=sk_input)
sk_kuva_vastus=tk.Label(root)

#2. järku determinant

tjärkudet_tiitel=ttk.Label(root,text="Teist järku determinant")
tdet_a11=ttk.Entry(root, width=6)
tdet_a12=ttk.Entry(root, width=6)
tdet_a21=ttk.Entry(root, width=6)
tdet_a22=ttk.Entry(root, width=6)

tjärkudet_arvuta=ttk.Button(root,text="Arvuta",command=tjärkudet_input)
tjärkudet_kuva_vastus=tk.Label(root)

#3. järku determinant
kjärkudet_tiitel=ttk.Label(root,text="Kolmandat järku determinant")
kdet_a11=ttk.Entry(root, width=6)
kdet_a12=ttk.Entry(root, width=6)
kdet_a13=ttk.Entry(root, width=6)

kdet_a21=ttk.Entry(root, width=6)
kdet_a22=ttk.Entry(root, width=6)
kdet_a23=ttk.Entry(root, width=6)

kdet_a31=ttk.Entry(root, width=6)
kdet_a32=ttk.Entry(root, width=6)
kdet_a33=ttk.Entry(root, width=6)

kjärkudet_arvuta=ttk.Button(root,text="Arvuta",command=kjärkudet_input)
kjärkudet_kuva_vastus=tk.Label(root)

#4. järku determinant
njärkudet_tiitel=ttk.Label(root,text="Neljandat järku determinant")
ndet_a11=ttk.Entry(root, width=6)
ndet_a12=ttk.Entry(root, width=6)
ndet_a13=ttk.Entry(root, width=6)
ndet_a14=ttk.Entry(root, width=6)

ndet_a21=ttk.Entry(root, width=6)
ndet_a22=ttk.Entry(root, width=6)
ndet_a23=ttk.Entry(root, width=6)
ndet_a24=ttk.Entry(root, width=6)

ndet_a31=ttk.Entry(root, width=6)
ndet_a32=ttk.Entry(root, width=6)
ndet_a33=ttk.Entry(root, width=6)
ndet_a34=ttk.Entry(root, width=6)

ndet_a41=ttk.Entry(root, width=6)
ndet_a42=ttk.Entry(root, width=6)
ndet_a43=ttk.Entry(root, width=6)
ndet_a44=ttk.Entry(root, width=6)

njärkudet_arvuta=ttk.Button(root,text="Arvuta",command=njärkudet_input)
njärkudet_kuva_vastus=tk.Label(root)

#5. järku determinant
vjärkudet_tiitel=ttk.Label(root,text="Viiendat järku determinant")
vdet_a11=ttk.Entry(root, width=6)
vdet_a12=ttk.Entry(root, width=6)
vdet_a13=ttk.Entry(root, width=6)
vdet_a14=ttk.Entry(root, width=6)
vdet_a15=ttk.Entry(root, width=6)

vdet_a21=ttk.Entry(root, width=6)
vdet_a22=ttk.Entry(root, width=6)
vdet_a23=ttk.Entry(root, width=6)
vdet_a24=ttk.Entry(root, width=6)
vdet_a25=ttk.Entry(root, width=6)

vdet_a31=ttk.Entry(root, width=6)
vdet_a32=ttk.Entry(root, width=6)
vdet_a33=ttk.Entry(root, width=6)
vdet_a34=ttk.Entry(root, width=6)
vdet_a35=ttk.Entry(root, width=6)

vdet_a41=ttk.Entry(root, width=6)
vdet_a42=ttk.Entry(root, width=6)
vdet_a43=ttk.Entry(root, width=6)
vdet_a44=ttk.Entry(root, width=6)
vdet_a45=ttk.Entry(root, width=6)

vdet_a51=ttk.Entry(root, width=6)
vdet_a52=ttk.Entry(root, width=6)
vdet_a53=ttk.Entry(root, width=6)
vdet_a54=ttk.Entry(root, width=6)
vdet_a55=ttk.Entry(root, width=6)

vjärkudet_arvuta=ttk.Button(root,text="Arvuta",command=vjärkudet_input)
vjärkudet_kuva_vastus=tk.Label(root)

#muutujad listis sega ja vektorkorrutis
muutujad=[[vk_tiitel,
           vk_vektor1x,vk_vektor1y,vk_vektor1z,
           vk_vektor1_tekst,
           vk_vektor2x,vk_vektor2y,vk_vektor2z,
           vk_vektor2_tekst,vk_nupp_arvuta,vk_kuva_vastus], #0
          
          [sk_tiitel,
           sk_x1,sk_y1,sk_z1,
           sk_x2,sk_y2,sk_z2,
           sk_x3,sk_y3,sk_z3,
           sk_nupp_arvuta,sk_kuva_vastus], #1
          ]

#muutujad 2-5 determinant
muutujad2=[[tjärkudet_tiitel,
        tdet_a11,tdet_a12,tdet_a21,tdet_a22,
        tjärkudet_arvuta,tjärkudet_kuva_vastus],#2x2
           
        [kjärkudet_tiitel,
         kdet_a11,kdet_a12,kdet_a13,
         kdet_a21,kdet_a22,kdet_a23,
         kdet_a31,kdet_a32,kdet_a33,
         kjärkudet_arvuta,kjärkudet_kuva_vastus],#3x3
           
        [njärkudet_tiitel,
         ndet_a11,ndet_a12,ndet_a13,ndet_a14,
         ndet_a21,ndet_a22,ndet_a23,ndet_a24,
         ndet_a31,ndet_a32,ndet_a33,ndet_a34,
         ndet_a41,ndet_a42,ndet_a43,ndet_a44,
         njärkudet_arvuta,njärkudet_kuva_vastus],#4x4
           
        [vjärkudet_tiitel,
         vdet_a11,vdet_a12,vdet_a13,vdet_a14,vdet_a15,
         vdet_a21,vdet_a22,vdet_a23,vdet_a24,vdet_a25,
         vdet_a31,vdet_a32,vdet_a33,vdet_a34,vdet_a35,
         vdet_a41,vdet_a42,vdet_a43,vdet_a44,vdet_a45,
         vdet_a51,vdet_a52,vdet_a53,vdet_a54,vdet_a55, #5x5
         vjärkudet_arvuta,vjärkudet_kuva_vastus
         ]]



#menüü nupud
vkcalc = ttk.Button(
    root,
    text="Vektorkorrutise kalkulaator",
    width=BUTTON_WIDTH,
    command=vahetus_vk_raami,
)
skcalc = ttk.Button(
    root,
    text="Segakorrutise kalkulaator",
    width=BUTTON_WIDTH,
    command=vahetus_sk_raami,
)


#menubutton determinandi jaoks

# determinandid=ttk.Menubutton(root,
#                            text="                 Determinandid", #sobib ajutiseks lahenduseks kah
#                            width=26,
#                            )

# determinandid.menu=ttk.Menu(determinandid,tearoff=0)
# determinandid["menu"]=determinandid.menu

detlabel=ttk.StringVar(root)
#detlabel.trace('w',det_menu)
valikud=[
    "2. järku determinant",
    "2. järku determinant",
    "3. järku determinant",
    "4. järku determinant",
    "5. järku determinant"
]
determinandid=ttk.OptionMenu(root, detlabel,*valikud,command=det_menu)
determinandid.config(width=BUTTON_WIDTH-4)
detlabel.set("Determinandid")
# for i in valikud:
#     determinandid.menu.add_radiobutton(label=i,variable=detlabel)


#menüü nuppude asetus
vkcalc.place(
    x=15,
    y=BUTTON_MARGIN,
)
skcalc.place(
    x=15,
    y=BUTTON_MARGIN*2,
)

determinandid.place(
    x=15,
    y=BUTTON_MARGIN*3
)
root.mainloop()