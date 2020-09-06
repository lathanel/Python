import tkinter as tk
from tkinter import ttk
import csv

class Header():
    def __init__(self, master):

        self.canvas = tk.Canvas(app, width = 300, height = 100)
        self.img = tk.PhotoImage(file="title.PNG")
        
        self.imgArea = self.canvas.create_image(0, 0, anchor=tk.NW, image = self.img)
        self.canvas.grid(row=0, column=0)
        


imenu={}#dictionary of item menu
ilist=[]#list of item list
with open('books2.csv', mode='r') as infile:
    reader = csv.reader(infile)
##    with open('coors_new.csv', mode='w') as outfile:
##        writer = csv.writer(outfile)
    imenu = {rows[0]:rows[1] for rows in reader}
    
for k in imenu.keys():
    ilist.append(k)
app = tk.Tk() 
app.geometry('500x500')
total=0

def add_item():
    global total
    co=comb.get()
    qu=quan.get()
    isvalue=(imenu[co])#istring value comes from dictionary
    ivalue=float(isvalue)
    tup=(co,isvalue,qu)
    iqu=int(qu)
    total= total+ ivalue *iqu
    tree.insert("", tk.END, values=tup)
    ltotal.set(str(total))

labelTop = tk.Label(app,text = "Choose item")
labelTop.grid(row=1,column=0)
comb=tk.StringVar()
comboExample = ttk.Combobox(app, textvariable=comb , values=ilist)
quan= tk.StringVar(value=1)
comboExample.grid(row=2,column=0)
comboExample.current(1)

customer_entry = tk.Entry(app,textvariable=quan, width=10)
customer_entry.grid(row=2, column=1, pady=20)

add_btn = tk.Button(app, text="Add item", width=12, command=add_item)
add_btn.grid(row=2, column=2, pady=20)
##print(dict(comboExample))

tree= ttk.Treeview(app, column=("column1", "column2", "column3"), show='headings')
tree.heading("#1", text="ITEM")
tree.heading("#2", text="PRICE")
tree.heading("#3", text="QTY")
tree.grid(row=3, column=0, columnspan=1)
tree.column("#2",minwidth=40,width=40)
tree.column("#3",minwidth=40,width=40)
##listbox1 = tk.Listbox(app, height=8, width=50, border=0)
##listbox1.grid(row=2, column=0, columnspan=3)
label1 = tk.Label(app, text = "Total Bill",font='Helvetica 18 bold' )
label1.grid(column=2, row=3)
ltotal=tk.StringVar()
label2 = tk.Label(app,font='Helvetica 18 bold',textvariable=ltotal)
label2.grid(column=2, row=4)
##print(comboExample.current(), comboExample.get())
##gui = Header(app)
h=Header(app)
app.mainloop()
