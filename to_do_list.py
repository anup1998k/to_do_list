from tkinter import *
import tkinter


from tkinter import messagebox

root = Tk()

# def to_display():
#     global entry
#     string = entry.get()
#     # label.configure(text= string)
#     filename = 'names.txt'
#     f = open(filename,'a') 
#     f.write(string)
#     f.close()




# entry = Entry(root)
# entry.focus_set()
# entry.grid()


# # label = tkinter.Label(root,text='name')
# # label.grid()

# btn = tkinter.Button(root,text='OK',command=to_display)
# btn.grid()


def add():
    global entry
    string = entry.get()
    lstbox.insert(END,string)
    entry.delete(0,'end')
    

def dele():
    lstbox.delete(ANCHOR) # lstboard has a inbuilt 'ANCHOR' which selects when hover on an item in listbox.
  
    


root.geometry()
root.config(background='black',border='10')
root.title('to_do_list')
root.resizable(width=False,height=False)

frame = Frame(root)
frame.pack(pady=10)

lstbox = Listbox(frame,width=25,height=8,font=('Times New Roman',14),bd= 0,fg='black')
lstbox.pack(side = LEFT,fill=BOTH)

list_items = []

for item in list_items:
    lstbox.insert(END,item) 

scrol = Scrollbar(frame)
scrol.pack(padx=10,side=RIGHT,fill=BOTH)
lstbox.config(yscrollcommand=scrol.set)  # to configuer the scroll bar , used y scrolle command to move up and down , else x scroll command left /right
scrol.config(command=lstbox.yview) # this command sets to help movment of lstbox when ever the scroller os scrolled.


entry = Entry(frame,font=('Times New Roman',14))
entry.pack(pady=20,padx=20)  # any number 


btn = Button(frame,text='ADD TEXT',font='times',command=add)
btn.pack(pady=20)

btn1 = Button(frame,text='DEL TEXT',font='times',command=dele)
btn1.pack(pady=20)


root.mainloop()



