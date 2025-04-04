from tkinter import *
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Base")
root.geometry("400x400")


    



EntryNumber = Entry(root,width=23)
EntryNumber.place(x=125, y=20)

innerFrame = tk.Frame(root, bg="blue",width= 400, height=200)
innerFrame.place(x=0,y=200)

BaseFrom = ttk.Combobox(root,width=20,height=20,values=[str(i) for i in range(2,17)])
BaseFrom.place(x=125,y=50)

canvas =Canvas(innerFrame,width=360, height=180)
scrollbar= Scrollbar(innerFrame, orient=VERTICAL, command=canvas.yview)
scrollableFrame = Frame(canvas)
canvas.create_window((0, 0), window=scrollableFrame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

def updateRegion():
    scrollableFrame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


BaseTo = ttk.Combobox(root,width=20,height=20,values=[str(i) for i in range(2,17)])
BaseTo.place(x=125,y=80)

def ConvertBase():

    for widget in scrollableFrame.winfo_children():
        widget.destroy()

    baseF = BaseFrom.get()
    baseT = BaseTo.get()
    number = EntryNumber.get()
    
    for i in number:
        if i not in "0123456789ABCDEF":
            print("Invalid Number")
            return
        
    y_offset = 10
    s=0
    Label(scrollableFrame, text=f"Converting {number} from base {baseF} to base 10:" ).pack(anchor="w", padx=50)
    for i in range(len(number)):# transforma in baza 10
        digi = int(number[i],base=int(baseF))
        term =digi *pow(int(baseF), len(number)-i-1)
        s += int(number[i], base=int(baseF)) * pow(int(baseF), len(number) - i - 1)
        Label(scrollableFrame, text=f"{digi} × {baseF}^{len(number) - i - 1} = {term}",  ).pack(anchor="w", padx=50)

    Label(scrollableFrame, text=f"Base 10 equivalent: {s}").pack(anchor="w", padx=50)
    convert = []
    module = 0

    Label(scrollableFrame, text=f"Converting {s} from base 10 to base {baseT}:").pack(anchor="w", padx=50)
    while s > 0 :
        module = s % int(baseT)
        s = s // int(baseT)
        convert.append(module)#descompune numarul in baza 10 in baza T
        Label(scrollableFrame, text=f"Divide by {baseT}: Rest = {module}, Cat = {s}").pack(anchor="w", padx=50)

    finalNumber = 0
    p=1

    for i in range(len(convert)):
        finalNumber += p * convert[i]# afiseaza corect numarul in ordine inversa 
        p = p * 10
    Label(scrollableFrame, text=f"Final result in base {baseT}: {finalNumber}").pack(anchor="w", padx=50)
    updateRegion()

    print (finalNumber)
     
        
    






Label(root,text="Number").place(x=30,y=20)
Label(root,text="From Base").place(x=30,y=50)
Label(root,text="To Base").place(x=30,y=80)

Button(root,text = "Convert",command=ConvertBase, width=19,height=5).place(x=125,y=110)

root.mainloop()