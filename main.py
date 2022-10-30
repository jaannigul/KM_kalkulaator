import subprocess
import sys
def install(package): #vajadusel installeerib puuduolevad moodulid
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install('ttkbootstrap') #
import tkinter as tk
import ttkbootstrap as ttk #pip install ttkbootstrap
import funktsioonid


#funktsioonid paigutuseks 
def vahetus_vk_raami():
    vk_tiitel.place(x=300,y=40)
    vk_vektor1_tekst.place(x=300,y=80)
    
    vk_vektor1x.place(x=360,y=80)
    vk_vektor1y.place(x=410,y=80)
    vk_vektor1z.place(x=460,y=80)
    
    vk_vektor2_tekst.place(x=300,y=110)
    
    vk_vektor2x.place(x=360,y=110)
    vk_vektor2y.place(x=410,y=110)
    vk_vektor2z.place(x=460,y=110)
    
    nupp_arvuta.place(x=360,y=140)
    kuva_vastus.place(x=460,y=140)
    #kõik muu paigutus tuleb unustada
    sk_tiitel.place_forget()

def vahetus_sk_raami():
    sk_tiitel.place(x=300,y=40)
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
    nupp_arvuta.place_forget()
    kuva_vastus.place_forget()

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
        kuva_vastus.configure(text=f"{vastus}")
    except:
        kuva_vastus.configure(text="Vale sisend")

BUTTON_WIDTH=30
BUTTON_MARGIN=40

#GUI
root=tk.Tk()
root.geometry("800x400") #akna suurus
#root['background']='grey'
root.title("Kalkulaatorid") #peaakna tiitel
style = ttk.Style("darkly") #stiilid: https://ttkbootstrap.readthedocs.io/en/latest/themes/dark/
root.resizable(False, False)

#current_theme = style.theme_use('awdark')
#muutujad ja widgetid
#vektorkorrutis
vk_tiitel = ttk.Label(root, text="Vektorkorrutis")
sk_tiitel=ttk.Label(root, text="Segakorrutis")

vk_vektor1x=ttk.Entry(root, width=6)
vk_vektor1y=ttk.Entry(root, width=6)
vk_vektor1z=ttk.Entry(root, width=6)

vk_vektor1_tekst=tk.Label(root,text="Vektor 1:")

vk_vektor2x=ttk.Entry(root, width=6)
vk_vektor2y=ttk.Entry(root, width=6)
vk_vektor2z=ttk.Entry(root, width=6)

vk_vektor2_tekst=tk.Label(root,text="Vektor 2:")
nupp_arvuta=ttk.Button(root,text="Arvuta",command=vk_input)
kuva_vastus=tk.Label(root)
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
#menüü nuppude paigutus https://www.pythontutorial.net/tkinter/tkinter-grid/

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