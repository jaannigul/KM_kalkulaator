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
nupp= ttk.Button(
    root,
    text="nupp",
    width=BUTTON_WIDTH,
    command=exit,
)

#menüü nuppude asetus
vkcalc.place(
    x=15,
    y=BUTTON_MARGIN,
)
skcalc.place(
    x=15,
    y=BUTTON_MARGIN*2,
)
nupp.place(
    x=15,
    y=BUTTON_MARGIN*3,
)

root.mainloop()