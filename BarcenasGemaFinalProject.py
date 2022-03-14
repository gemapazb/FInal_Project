from tkinter import *

#creating main window 

#window= Tk()
#window.title("Locator V1.0")
#window.configure(background="dark turquoise")
#creating window for BHV & OV Locations

window = Tk()
window.title("Locator V1.0") 
window.geometry("300x300")

def vent1():

  window.config(bg='dark turquoise')
  ventana02.place(width=0, height=0)
  ventana01.pack()

  #return ventana01


def vent2():
    
  window.config(bg='pink')
  ventana01.place(width=0, height=0)  
  ventana02.pack()

def s_stack():
  skids_value=s_var.get()
  Res.set("you need "+str(int(skids_value)/1))

def d_stack():
  skids_value=s_var.get()
  Res.set("you need "+str(int(skids_value)/2))

def t_stack():
  skids_value=s_var.get()
  Res.set("you need "+str(int(skids_value)/3))


#adjusting size of main Window

window.config(bg='dark turquoise',bd=12)

ventana01=Frame(window,bd=0)
ventana01.config(bg='dark turquoise')
ventana01.pack()

#creatring 1st label 
label_1=Label(ventana01,text="Welcome to Locator 2022")
label_1.pack(padx=55, pady=55)
#label_1.pack()

#framing the buttons/menu main window
frame= Frame(window)
frame.pack(side=TOP)
bottom_frame= Frame(ventana01)
bottom_frame.pack(side=TOP)

#creating 1st button /main window
OV_BHVbtn= Button(ventana01, text='Click to Locate OV/BHV', command=vent2)
OV_BHVbtn.pack(side=TOP)

#creating 2nd Button/main window
BNC_btn = Button(ventana01, text='CLick to locate BNC',command=vent2)
BNC_btn.pack(side=TOP)

FondoGen=PhotoImage(file="imagen00.png") 
logo=Label(ventana01, image=FondoGen)
logo.pack() #ipadx=15, ipady=15)

##########################################################################
    
ventana02=Frame(window,bd=0)
ventana02.config(bg='pink')

win2_label = Label(ventana02, text="OV/BHV Available Locations ").pack()
win2_label = Label(ventana02, text=" Enter skids to Locate then select stacking").pack()

s_var=StringVar()
s_var.set('')
skids_e= Entry(ventana02, width=5,textvariable=s_var)
skids_e.pack()

S_S= Button(ventana02,text='Single stack', command=s_stack)
S_S.pack(side=TOP)

D_S= Button(ventana02,text='Double stack', command=d_stack)
D_S.pack(side=TOP)

T_S= Button(ventana02,text='Triple stack', command=t_stack)
T_S.pack(side=TOP)

#Label Results
Res=StringVar()
Res.set(" Skid spaces needed:")
Results= Label(ventana02,textvariable=Res)
Results.pack()
#output Results 
skids= Label(ventana02)
skids.pack()

start_over= Button(ventana02,text='Start Over', command=vent1)
start_over.pack(side=TOP)

FondoGen1=PhotoImage(file="imagen01.png") 
logo1=Label(ventana02, image=FondoGen1)
logo1.pack()

window.mainloop()