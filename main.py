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
    
    vk_nupp_arvuta.place(x=360,y=80+INPUT_MARGIN_Y+CALC_MARGIN)
    vk_kuva_vastus.place(x=445,y=80+INPUT_MARGIN_Y+CALC_MARGIN+3)
    #kõik muu paigutus tuleb unustada
    for i in range(len(muutujad)):
        if i !=0:
            for j in muutujad[i]:
                j.place_forget()
    
    

def vahetus_sk_raami():
    sk_tiitel.place(x=300,y=40)
    
    sk_x1.place(x=360,y=80)
    sk_y1.place(x=360+INPUT_MARGIN_X, y=80)
    sk_z1.place(x=360+INPUT_MARGIN_X*2, y=80)
    sk_vektor1_tekst.place(x=300,y=80)
    sk_x2.place(x=360,y=80+INPUT_MARGIN_Y)
    sk_y2.place(x=360+INPUT_MARGIN_X, y=80+INPUT_MARGIN_Y)
    sk_z2.place(x=360+INPUT_MARGIN_X*2, y=80+INPUT_MARGIN_Y)
    sk_vektor2_tekst.place(x=300,y=80+INPUT_MARGIN_Y)
    sk_x3.place(x=360, y=80+INPUT_MARGIN_Y*2)
    sk_y3.place(x=360+INPUT_MARGIN_X, y=80+INPUT_MARGIN_Y*2)
    sk_z3.place(x=360+INPUT_MARGIN_X*2, y=80+INPUT_MARGIN_Y*2)
    sk_vektor3_tekst.place(x=300,y=80+INPUT_MARGIN_Y*2)
    sk_nupp_arvuta.place(x=360, y=80+INPUT_MARGIN_Y*2+CALC_MARGIN) 
    sk_kuva_vastus.place(x=460, y=80+INPUT_MARGIN_Y*2+CALC_MARGIN)
    #kõik muu paigutus tuleb unustada

    for i in range(len(muutujad)):
        if i !=1:
            for j in muutujad[i]:
                j.place_forget()

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
        print(vastus)
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
        vastus=funktsioonid.det4(
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
        vastus=funktsioonid.det5(
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
            
            float(vdet_a51.get()),
            float(vdet_a52.get()),
            float(vdet_a53.get()),
            float(vdet_a54.get()),
            float(vdet_a55.get()),
            
            )
        vjärkudet_kuva_vastus.configure(text=f"{vastus}")
    except: vjärkudet_kuva_vastus.configure(text="Vale Sisend")
def tpm_input():
    try:
        vastus=funktsioonid.pöörd2m(
            float(tpm_a11.get()),
            float(tpm_a12.get()),
            float(tpm_a21.get()),
            float(tpm_a22.get()),
        )
    except: pass
def vahetus_det2_raami():
    tjärkudet_tiitel.place(x=300,y=40)
    
    tdet_a11.place(x=360,y=80)
    tdet_a12.place(x=360+INPUT_MARGIN_X, y=80)
    tdet_a21.place(x=360,y=80+INPUT_MARGIN_Y)
    tdet_a22.place(x=360+INPUT_MARGIN_X,y=80+INPUT_MARGIN_Y)
    
    tjärkudet_arvuta.place(x=360,y=80+INPUT_MARGIN_Y+CALC_MARGIN)
    tjärkudet_kuva_vastus.place(x=360+RESULT_MARGIN,y=80+INPUT_MARGIN_Y+CALC_MARGIN+3)
    for i in range(len(muutujad)):
        if i !=2:
            for j in muutujad[i]:
                j.place_forget()
def vahetus_det3_raami(): 
    kjärkudet_tiitel.place(x=300,y=40)
    
    for i,var in enumerate(muutujad[3][1:10]):
        if i<=2:
            var.place(x=360+INPUT_MARGIN_X*i, y=80)
        elif i<=5:
            var.place(x=360+INPUT_MARGIN_X*(i-3), y=80+INPUT_MARGIN_Y)
        elif i<=11:
            var.place(x=360+INPUT_MARGIN_X*(i-6), y=80+INPUT_MARGIN_Y*2)
    
    kjärkudet_arvuta.place(x=360,y=80+INPUT_MARGIN_Y*2+CALC_MARGIN)
    kjärkudet_kuva_vastus.place(x=360+RESULT_MARGIN,y=80+INPUT_MARGIN_Y*2+CALC_MARGIN+3)
    
    for i in range(len(muutujad)):
        if i !=3:
            for j in muutujad[i]:
                j.place_forget()
def vahetus_det4_raami():
    njärkudet_tiitel.place(x=300,y=40)
    for i,var in enumerate(muutujad[4][1:17],start=0):
        if i<4:
            var.place(x=360+INPUT_MARGIN_X*i, y=80)
        elif i<8:
            var.place(x=360+INPUT_MARGIN_X*(i-4), y=80+INPUT_MARGIN_Y)
        elif i<12:
            var.place(x=360+INPUT_MARGIN_X*(i-8), y=80+INPUT_MARGIN_Y*2)
        elif i<16:
            var.place(x=360+INPUT_MARGIN_X*(i-12), y=80+INPUT_MARGIN_Y*3)
        
    njärkudet_arvuta.place(x=360,y=80+INPUT_MARGIN_Y*3+CALC_MARGIN)
    njärkudet_kuva_vastus.place(x=360+RESULT_MARGIN,y=80+INPUT_MARGIN_Y*3+CALC_MARGIN+3)
    for i in range(len(muutujad)):
        if i !=4:
            for j in muutujad[i]:
                j.place_forget()
def vahetus_det5_raami():
    vjärkudet_tiitel.place(x=300,y=40)
    for i,var in enumerate(muutujad[5][1:26],start=0):
        if i<5:
            var.place(x=360+INPUT_MARGIN_X*i, y=80)
        elif i<10:
            var.place(x=360+INPUT_MARGIN_X*(i-5), y=80+INPUT_MARGIN_Y)
        elif i<15:
            var.place(x=360+INPUT_MARGIN_X*(i-10), y=80+INPUT_MARGIN_Y*2)
        elif i<20:
            var.place(x=360+INPUT_MARGIN_X*(i-15), y=80+INPUT_MARGIN_Y*3)
        elif i<25:
            var.place(x=360+INPUT_MARGIN_X*(i-20), y=80+INPUT_MARGIN_Y*4)
        
    vjärkudet_arvuta.place(x=360,y=80+INPUT_MARGIN_Y*4+CALC_MARGIN)
    vjärkudet_kuva_vastus.place(x=360+RESULT_MARGIN,y=80+INPUT_MARGIN_Y*4+CALC_MARGIN+3)
    
    for i in range(len(muutujad)):
        if i !=5:
            for j in muutujad[i]:
                j.place_forget()
def vahetus_pm2_raami():
    pass
def vahetus_pm3_raami():
    pass
def vahetus_pm4_raami():
    pass
def vahetus_pm5_raami():
    pass

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
def pm_menu(valik):
    valik=pmlabel.get()
    if valik=="2. järku determinant":
        vahetus_pm2_raami()
    if valik=="3. järku determinant":
        vahetus_pm3_raami()
    if valik=="4. järku determinant":
        vahetus_pm4_raami()
    if valik=="5. järku determinant":
        vahetus_pm5_raami()
        
#konstandid
BUTTON_WIDTH=30
BUTTON_MARGIN=40
INPUT_MARGIN_X=55
INPUT_MARGIN_Y=35
CALC_MARGIN=45
RESULT_MARGIN=85
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

#segakorrutis TODO: lahtrite puhastus
sk_tiitel=ttk.Label(root, text="Segakorrutis")
sk_x1=ttk.Entry(root, width=6)
sk_y1=ttk.Entry(root, width=6)
sk_z1=ttk.Entry(root, width=6)
sk_vektor1_tekst=tk.Label(root,text="Vektor 1:")
sk_x2=ttk.Entry(root, width=6)
sk_y2=ttk.Entry(root, width=6)
sk_z2=ttk.Entry(root, width=6)
sk_vektor2_tekst=tk.Label(root,text="Vektor 2:")
sk_x3=ttk.Entry(root, width=6)
sk_y3=ttk.Entry(root, width=6)
sk_z3=ttk.Entry(root, width=6)
sk_vektor3_tekst=tk.Label(root,text="Vektor 3:")

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

#2. järku pöördmaatriks
tpm_tiitel=ttk.Label(root,text="Teist järku pöördmaatriks")
tpm_a11=ttk.Entry(root, width=6)
tpm_a12=ttk.Entry(root, width=6)
tpm_a21=ttk.Entry(root, width=6)
tpm_a22=ttk.Entry(root, width=6)

tpm_arvuta=ttk.Button(root,text="Arvuta",command=tpm_input)
tpm_kuva_vastus=tk.Label(root)
#muutujad listis sega ja vektorkorrutis (tegelikult objektid)
muutujad=[[vk_tiitel,
           vk_vektor1x,vk_vektor1y,vk_vektor1z,
           vk_vektor1_tekst,
           vk_vektor2x,vk_vektor2y,vk_vektor2z,
           vk_vektor2_tekst,vk_nupp_arvuta,vk_kuva_vastus], #0
          
          [sk_tiitel,
           sk_x1,sk_y1,sk_z1,
           sk_x2,sk_y2,sk_z2,
           sk_x3,sk_y3,sk_z3,
           sk_nupp_arvuta,sk_kuva_vastus,sk_vektor1_tekst,sk_vektor2_tekst,sk_vektor3_tekst], #1
          
            [tjärkudet_tiitel,
            tdet_a11,tdet_a12,tdet_a21,tdet_a22,
            tjärkudet_arvuta,tjärkudet_kuva_vastus],#2
            
            [kjärkudet_tiitel,
            kdet_a11,kdet_a12,kdet_a13,
            kdet_a21,kdet_a22,kdet_a23,
            kdet_a31,kdet_a32,kdet_a33,
            kjärkudet_arvuta,kjärkudet_kuva_vastus],#3
            
            [njärkudet_tiitel,
            ndet_a11,ndet_a12,ndet_a13,ndet_a14,
            ndet_a21,ndet_a22,ndet_a23,ndet_a24,
            ndet_a31,ndet_a32,ndet_a33,ndet_a34,
            ndet_a41,ndet_a42,ndet_a43,ndet_a44,
            njärkudet_arvuta,njärkudet_kuva_vastus],#4
            
            [vjärkudet_tiitel,
            vdet_a11,vdet_a12,vdet_a13,vdet_a14,vdet_a15,
            vdet_a21,vdet_a22,vdet_a23,vdet_a24,vdet_a25,
            vdet_a31,vdet_a32,vdet_a33,vdet_a34,vdet_a35,
            vdet_a41,vdet_a42,vdet_a43,vdet_a44,vdet_a45,
            vdet_a51,vdet_a52,vdet_a53,vdet_a54,vdet_a55, #5
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

#menüünupp determinandi jaoks

detlabel=ttk.StringVar(root)
valikud=[
    "2. järku determinant",
    "2. järku determinant",#miskipärast vajab see 2 korda seda elementi
    "3. järku determinant",
    "4. järku determinant",
    "5. järku determinant"
]
determinandid=ttk.OptionMenu(root, detlabel,*valikud,command=det_menu)
determinandid.config(width=BUTTON_WIDTH-4)
detlabel.set("Determinandid")
#menüünupp pöördmaatriksite jaoks
pmlabel=ttk.StringVar(root)
pöördmaatriksid=ttk.OptionMenu(root, pmlabel,*valikud,command=pm_menu)
pöördmaatriksid.config(width=BUTTON_WIDTH-4)
pmlabel.set("Pöördmaatriksid")
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
pöördmaatriksid.place(
    x=15,
    y=BUTTON_MARGIN*4
)
root.mainloop()