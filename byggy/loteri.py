from tkinter import *
from tkinter import messagebox
import lotteri 

root = Tk()
root.title("Lotteri")

listbox = Listbox (root, height = 4,
                  width = 30,
                  bg = "white",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "blue")

root.geometry("380x300")

lotteri = lotteri.Lotteri()

label_antal = Label(root, text="Antal Lotter, Max 3st :")
label_antal.grid(row=0, column=0, sticky=E, padx=5, pady=5)

textbox_antal = Entry(root, width=2)
textbox_antal.grid(row=0, column=1, sticky=W, padx=5, pady=5)
textbox_antal.focus_set()

def update_listBox(antal_lotter):
    listbox.delete(0, END)
    listbox.insert(1,"Gratis du van det här!")
    
    try:
        int_antal_lotter = int(antal_lotter)
        i = 0
        if (int_antal_lotter <4):
             while i < int_antal_lotter:
                 Vinst = lotteri.get_vinst()
                 listbox.insert((i+2), Vinst)
                 i += 1
                
                
        elif (int_antal_lotter > 3):
            messagebox.showinfo("Du har valt för många lotter")
            
    except ValueError:
        messagebox.showinfo("Endast siffror tillåtet!")
        
def clickSlumpaButton():
    antal_lott = textbox_antal.get()
    textbox_antal.delete(0, END)
    textbox_antal.focus_set()
    update_listBox(antal_lott)
    
button_slumpa = Button(text="Tur knapp", command = clickSlumpaButton)
button_slumpa.grid(row=1, column=0, sticky=E, padx=15, pady=15)
    
listbox.grid(row=2, column=0, columnspan=2, padx=15, pady=15)
    
    #pack the widgates
    #label.pack()
    #listbox.pack()
    
    #display until User
    #exits themselves
root.mainloop()