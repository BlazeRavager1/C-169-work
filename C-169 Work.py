from tkinter import * 
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("GUI ELEMENTS")
root.geometry("600x600")

class GUI :
    def __init__(self):
        print("Function is created")
    def newElement(self):
        if ElementList.get() == "Label" :
            l1 = Label(root, text = "New label and button have been created")
            l1.pack()
        if ElementList.get() == "Button" :
            b1 = Button(root, text = "click me", command = self.alert)
            b1.pack()
        if ElementList.get() == "Dropdown" :
            d1 = ttk.Combobox(root, values = ["You just", "Made a","New Dropdown"])
            d1.pack()
    def alert(self):
        messagebox.showinfo("ALERT!", 'New elements has been created')

object1 = GUI()

ELements = ["Label", "Button", "Dropdown"]
ElementList = ttk.Combobox(root, values = ELements)
ElementList['state'] = 'readonly'

ElementList.pack()

btn = Button(root, text = "Create new elements", command = object1.newElement)
btn.pack()

root.mainloop()