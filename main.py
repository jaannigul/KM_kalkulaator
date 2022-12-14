try:  #proovib kas ttkbootstrap on juba installeeritud, kui mitte, siis installeerib selle
    import ttkbootstrap as ttk #pip install ttkbootstrap
except ImportError:
    import subprocess
    import sys
    def install(package): #vajadusel installeerib puuduolevad moodulid
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    install('ttkbootstrap')
    import ttkbootstrap as ttk #pip install ttkbootstrap
import tkinter as tk
import funktsioonid

#funktsioonid paigutuseks 
def vahetus_vk_raami():
    puhasta_lahtrid()
    detlabel.set("Determinandid")
    pmlabel.set("Pöördmaatriksid")
    vk_tiitel.place(x=300,y=40)
    vk_vektor1_tekst.place(x=300,y=80)
    
    vk_vektor1x.place(x=360,y=80)
    vk_vektor1y.place(x=360+INPUT_MARGIN_X,y=80)
    vk_vektor1z.place(x=360+INPUT_MARGIN_X*2,y=80)
    
    vk_vektor2_tekst.place(x=300,y=80+INPUT_MARGIN_Y)
    
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
    puhasta_lahtrid()
    detlabel.set("Determinandid")
    pmlabel.set("Pöördmaatriksid")
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
    except: kjärkudet_kuva_vastus.configure(text="Vale sisend")
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
    except: njärkudet_kuva_vastus.configure(text="Vale sisend")
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
    except: vjärkudet_kuva_vastus.configure(text="Vale sisend")
def tpm_input():
    try:
        vastus=funktsioonid.pöörd2m(
            float(tpm_a11.get()),
            float(tpm_a12.get()),
            float(tpm_a21.get()),
            float(tpm_a22.get()),
        )
        tpm_kuva_vastus.configure(text=f"{vastus}")
    except: tpm_kuva_vastus.configure(text="Vale sisend")

def kpm_input():
    try:
        vastus=funktsioonid.pöörd3m(
            float(kpm_a11.get()),
            float(kpm_a12.get()),
            float(kpm_a13.get()),
            
            float(kpm_a21.get()),
            float(kpm_a22.get()),
            float(kpm_a23.get()),
            
            float(kpm_a31.get()),
            float(kpm_a32.get()),
            float(kpm_a33.get()),
        )
        kpm_kuva_vastus.configure(text=f"{vastus}")
    except: kpm_kuva_vastus.configure(text="Vale sisend")
def npm_input():
    try:
        vastus=funktsioonid.pöörd4m(
            float(npm_a11.get()), 
            float(npm_a12.get()),
            float(npm_a13.get()),
            float(npm_a14.get()),
            
            float(npm_a21.get()),
            float(npm_a22.get()),
            float(npm_a23.get()),
            float(npm_a24.get()),
            
            float(npm_a31.get()),
            float(npm_a32.get()),
            float(npm_a33.get()),
            float(npm_a34.get()),
            
            float(npm_a41.get()),
            float(npm_a42.get()),
            float(npm_a43.get()),
            float(npm_a44.get())
            
            )
        npm_kuva_vastus.configure(text=f"{vastus}")
    except: npm_kuva_vastus.configure(text="Vale sisend")
def vpm_input():
    try:
        vastus=funktsioonid.pöörd5m(
            float(vpm_a11.get()), 
            float(vpm_a12.get()),
            float(vpm_a13.get()),
            float(vpm_a14.get()),
            float(vpm_a15.get()),
            
            float(vpm_a21.get()),
            float(vpm_a22.get()),
            float(vpm_a23.get()),
            float(vpm_a24.get()),
            float(vpm_a25.get()),
            
            float(vpm_a31.get()),
            float(vpm_a32.get()),
            float(vpm_a33.get()),
            float(vpm_a34.get()),
            float(vpm_a35.get()),
            
            float(vpm_a41.get()),
            float(vpm_a42.get()),
            float(vpm_a43.get()),
            float(vpm_a44.get()),
            float(vpm_a45.get()),
            
            float(vpm_a51.get()),
            float(vpm_a52.get()),
            float(vpm_a53.get()),
            float(vpm_a54.get()),
            float(vpm_a55.get()),
            
            )
        vpm_kuva_vastus.configure(text=f"{vastus}")
    except: vpm_kuva_vastus.configure(text="Vale sisend")    

def vahetus_det2_raami():
    puhasta_lahtrid()
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
    puhasta_lahtrid()
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
    puhasta_lahtrid()
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
    puhasta_lahtrid()
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
    puhasta_lahtrid()
    tpm_tiitel.place(x=300,y=40)
    for i,var in enumerate(muutujad[6][1:5]):
        if i<2:
            var.place(x=360+INPUT_MARGIN_X*i,y=80)
        elif i<4:
            var.place(x=360+INPUT_MARGIN_X*(i-2),y=80+INPUT_MARGIN_Y)
    tpm_arvuta.place(x=360,y=80+INPUT_MARGIN_Y+CALC_MARGIN)
    tpm_kuva_vastus.place(x=360+RESULT_MARGIN,y=INPUT_MARGIN_Y*3+CALC_MARGIN+3) 
    for i in range(len(muutujad)):
        if i !=6:
            for j in muutujad[i]:
                j.place_forget()
def vahetus_pm3_raami():
    puhasta_lahtrid()
    kpm_tiitel.place(x=300,y=40)
    for i,var in enumerate(muutujad[7][1:10]):
        if i<=2:
            var.place(x=360+INPUT_MARGIN_X*i, y=80)
        elif i<=5:
            var.place(x=360+INPUT_MARGIN_X*(i-3), y=80+INPUT_MARGIN_Y)
        elif i<=11:
            var.place(x=360+INPUT_MARGIN_X*(i-6), y=80+INPUT_MARGIN_Y*2)
    kpm_arvuta.place(x=360,y=80+INPUT_MARGIN_Y*2+CALC_MARGIN)
    kpm_kuva_vastus.place(x=360+RESULT_MARGIN,y=80+INPUT_MARGIN_Y*2+CALC_MARGIN+3)

    for i in range(len(muutujad)):
        if i !=7:
            for j in muutujad[i]:
                j.place_forget()
def vahetus_pm4_raami():
    puhasta_lahtrid()
    npm_tiitel.place(x=300,y=40)
    for i,var in enumerate(muutujad[8][1:17],start=0):
        if i<4:
            var.place(x=360+INPUT_MARGIN_X*i, y=80)
        elif i<8:
            var.place(x=360+INPUT_MARGIN_X*(i-4), y=80+INPUT_MARGIN_Y)
        elif i<12:
            var.place(x=360+INPUT_MARGIN_X*(i-8), y=80+INPUT_MARGIN_Y*2)
        elif i<16:
            var.place(x=360+INPUT_MARGIN_X*(i-12), y=80+INPUT_MARGIN_Y*3)
        
    npm_arvuta.place(x=360,y=80+INPUT_MARGIN_Y*3+CALC_MARGIN)
    npm_kuva_vastus.place(x=360+RESULT_MARGIN,y=80+INPUT_MARGIN_Y*3+CALC_MARGIN+3)
    for i in range(len(muutujad)):
        if i !=8:
            for j in muutujad[i]:
                j.place_forget()
def vahetus_pm5_raami():
    puhasta_lahtrid()
    vpm_tiitel.place(x=300,y=40)
    for i,var in enumerate(muutujad[9][1:26],start=0):
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
        
    vpm_arvuta.place(x=360,y=80+INPUT_MARGIN_Y*4+CALC_MARGIN)
    vpm_kuva_vastus.place(x=360+RESULT_MARGIN,y=80+INPUT_MARGIN_Y*4+CALC_MARGIN+3)
    
    for i in range(len(muutujad)):
        if i !=9:
            for j in muutujad[i]:
                j.place_forget()

def det_menu(valik):
    pmlabel.set("Pöördmaatriksid")
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
    detlabel.set("Determinandid")
    valik=pmlabel.get()
    if valik=="2. järku pöördmaatriks":
        vahetus_pm2_raami()
    if valik=="3. järku pöördmaatriks":
        vahetus_pm3_raami()
    if valik=="4. järku pöördmaatriks":
        vahetus_pm4_raami()
    if valik=="5. järku pöördmaatriks":
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

#objektid ja widgetid
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

#segakorrutis
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

#3. järku pöördmaatriks
kpm_tiitel=ttk.Label(root,text="Kolmandat järku pöördmaatriks")
kpm_a11=ttk.Entry(root, width=6)
kpm_a12=ttk.Entry(root, width=6)
kpm_a13=ttk.Entry(root, width=6)

kpm_a21=ttk.Entry(root, width=6)
kpm_a22=ttk.Entry(root, width=6)
kpm_a23=ttk.Entry(root, width=6)

kpm_a31=ttk.Entry(root, width=6)
kpm_a32=ttk.Entry(root, width=6)
kpm_a33=ttk.Entry(root, width=6)

kpm_arvuta=ttk.Button(root,text="Arvuta",command=kpm_input)
kpm_kuva_vastus=tk.Label(root)

#4. järku pöördmaatriks
npm_tiitel=ttk.Label(root,text="Neljandat järku pöördmaatriks")
npm_a11=ttk.Entry(root, width=6)
npm_a12=ttk.Entry(root, width=6)
npm_a13=ttk.Entry(root, width=6)
npm_a14=ttk.Entry(root, width=6)

npm_a21=ttk.Entry(root, width=6)
npm_a22=ttk.Entry(root, width=6)
npm_a23=ttk.Entry(root, width=6)
npm_a24=ttk.Entry(root, width=6)

npm_a31=ttk.Entry(root, width=6)
npm_a32=ttk.Entry(root, width=6)
npm_a33=ttk.Entry(root, width=6)
npm_a34=ttk.Entry(root, width=6)

npm_a41=ttk.Entry(root, width=6)
npm_a42=ttk.Entry(root, width=6)
npm_a43=ttk.Entry(root, width=6)
npm_a44=ttk.Entry(root, width=6)

npm_arvuta=ttk.Button(root,text="Arvuta",command=npm_input)
npm_kuva_vastus=tk.Label(root)

#5. järku pöördmaatriks
vpm_tiitel=ttk.Label(root,text="Viiendat järku pöördmaatriks")
vpm_a11=ttk.Entry(root, width=6)
vpm_a12=ttk.Entry(root, width=6)
vpm_a13=ttk.Entry(root, width=6)
vpm_a14=ttk.Entry(root, width=6)
vpm_a15=ttk.Entry(root, width=6)

vpm_a21=ttk.Entry(root, width=6)
vpm_a22=ttk.Entry(root, width=6)
vpm_a23=ttk.Entry(root, width=6)
vpm_a24=ttk.Entry(root, width=6)
vpm_a25=ttk.Entry(root, width=6)

vpm_a31=ttk.Entry(root, width=6)
vpm_a32=ttk.Entry(root, width=6)
vpm_a33=ttk.Entry(root, width=6)
vpm_a34=ttk.Entry(root, width=6)
vpm_a35=ttk.Entry(root, width=6)

vpm_a41=ttk.Entry(root, width=6)
vpm_a42=ttk.Entry(root, width=6)
vpm_a43=ttk.Entry(root, width=6)
vpm_a44=ttk.Entry(root, width=6)
vpm_a45=ttk.Entry(root, width=6)

vpm_a51=ttk.Entry(root, width=6)
vpm_a52=ttk.Entry(root, width=6)
vpm_a53=ttk.Entry(root, width=6)
vpm_a54=ttk.Entry(root, width=6)
vpm_a55=ttk.Entry(root, width=6)

vpm_arvuta=ttk.Button(root,text="Arvuta",command=vpm_input)
vpm_kuva_vastus=tk.Label(root)

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
            vjärkudet_arvuta,vjärkudet_kuva_vastus],
            #pöördmaatriksid
            [tpm_tiitel,
             tpm_a11,tpm_a12,tpm_a21,tpm_a22, #6
             tpm_arvuta,tpm_kuva_vastus],
          
            [kpm_tiitel,
             kpm_a11,kpm_a12,kpm_a13,kpm_a21,kpm_a22,kpm_a23,kpm_a31,kpm_a32,kpm_a33, #7
             kpm_arvuta,kpm_kuva_vastus],

            [npm_tiitel,
            npm_a11,npm_a12,npm_a13,npm_a14,
            npm_a21,npm_a22,npm_a23,npm_a24,
            npm_a31,npm_a32,npm_a33,npm_a34,
            npm_a41,npm_a42,npm_a43,npm_a44,
            npm_arvuta,npm_kuva_vastus],#8
            
            [vpm_tiitel,
            vpm_a11,vpm_a12,vpm_a13,vpm_a14,vpm_a15,
            vpm_a21,vpm_a22,vpm_a23,vpm_a24,vpm_a25,
            vpm_a31,vpm_a32,vpm_a33,vpm_a34,vpm_a35,
            vpm_a41,vpm_a42,vpm_a43,vpm_a44,vpm_a45,
            vpm_a51,vpm_a52,vpm_a53,vpm_a54,vpm_a55, #9
            vpm_arvuta,vpm_kuva_vastus],
                      ]

def puhasta_lahtrid():
    for i in muutujad:
        for j in i:
            try:
                j.delete(0,tk.END) #tk entry puhastus
            except: #tk labelite puhastus
                if j in [vk_kuva_vastus,sk_kuva_vastus,
                         tjärkudet_kuva_vastus,njärkudet_kuva_vastus,vjärkudet_kuva_vastus,
                         tpm_kuva_vastus,kpm_kuva_vastus,npm_kuva_vastus,vpm_kuva_vastus]:
                    j.configure(text="")
                continue


#menüü nupud
vkcalc = ttk.Button(
    root,
    text="Vektorkorrutise kalkulaator",
    width=BUTTON_WIDTH,
    command=vahetus_vk_raami,)
skcalc = ttk.Button(
    root,
    text="Segakorrutise kalkulaator",
    width=BUTTON_WIDTH,
    command=vahetus_sk_raami,
)
puhastalahtrid = ttk.Button(root,
    text="Puhasta väljad",
    width=BUTTON_WIDTH/2,
    command=puhasta_lahtrid,
)
#menüünupp determinandi jaoks

detlabel=ttk.StringVar(root)
detvalikud=[
    "2. järku determinant",
    "2. järku determinant",#miskipärast vajab see 2 korda seda elementi, et asi töötaks
    "3. järku determinant",
    "4. järku determinant",
    "5. järku determinant"
]
#valikud pöördmaatriksi jaoks
pmvalikud=[
    "2. järku pöördmaatriks",
    "2. järku pöördmaatriks",
    "3. järku pöördmaatriks",
    "4. järku pöördmaatriks",
    "5. järku pöördmaatriks"
]
determinandid=ttk.OptionMenu(root, detlabel,*detvalikud,command=det_menu)
determinandid.config(width=BUTTON_WIDTH-4)
detlabel.set("Determinandid") #algväärtus
#menüünupp pöördmaatriksite jaoks
pmlabel=ttk.StringVar(root)
pöördmaatriksid=ttk.OptionMenu(root, pmlabel,*pmvalikud,command=pm_menu)
pöördmaatriksid.config(width=BUTTON_WIDTH-4)
pmlabel.set("Pöördmaatriksid") #algväärtus
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
puhastalahtrid.place(x=680,y=350)
root.mainloop()