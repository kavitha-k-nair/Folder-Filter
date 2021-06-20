'''import os, shutil

initpath = "C:\\Users\\karum\\Downloads\\"

destpath = "C:\\Users\\karum\\OneDrive\\Desktop\\Filtered Files\\"

for path,dirs,files in os.walk(initpath):
    for file in files:
        extn = file.split(".")[1]

        if os.path.exists(destpath + extn):
            shutil.copy(path + "\\" + file, destpath + extn)
        else:
            os.makedirs(destpath + extn)
            shutil.copy(path + "\\" + file, destpath + extn)

print("done")'''

#**********************************************************************************#

def move():
    srcentry = src.get()
    destentry = dest.get()

    if (srcentry == '' or destentry == ''):
        messagebox.showerror('Error', 'Invalid Path')
        root.destroy()
        exit()

    for path,dirs,files in os.walk(srcentry):
        for file in files:
            extn = file.split(".")[1]

            if os.path.exists(destentry + extn):
                shutil.copy(path + "\\" + file, destentry + extn)

            else:
                os.makedirs(destentry + extn)
                shutil.copy(path + "\\" + file, destentry + extn)

    success = Label(root, text = "  SUCCESS  " , font = (30) ).place(x=350,y=230)




    
import tkinter
from tkinter import *
from tkinter import messagebox
import os, shutil, sys

root = tkinter.Tk()
root.geometry("800x300")
root.resizable(0,0)
root.configure(bg= "cyan")


srcpath = Label(root, text = "Source Path: " , font = (15) , bg = "cyan" ).place(x=15,y=50)
destpath = Label(root, text = "Destination Path: " , font = (15) , bg = "cyan" ).place(x=15, y=150)

src = Entry (root, font = (15), width = 50)
src.place(x = 200, y = 50)
dest = Entry (root, font = (15), width = 50)
dest.place(x= 200, y = 150)

movebtn = Button (root, text = "  Move  ", font = (20), bd = 5 , command = move).place(x=380,y=230)

root.mainloop()
