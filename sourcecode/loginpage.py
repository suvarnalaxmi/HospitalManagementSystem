from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk

def loginpage():
    uname=e1.get()
    password=e2.get()

    if(uname=="" and password==""):
        messagebox.showinfo("Login","Blank not allowed")
    
    elif(uname=="Admin" and password=="Admin@123"):
        messagebox.showinfo("Login","Login Successful")
        root.destroy()

    else:
        messagebox.showinfo("","Invalid login credentials")

root=Tk()
root.title("Login")

# Setting icon of root window
img=PhotoImage(file='icon2.png')
root.iconphoto(False, img)
 


             
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()

#setting tkinter window size
root.geometry("%dx%d" %(width,height))
root.configure(background="Light blue")

load=Image.open('LOGINBG.png')
img=ImageTk.PhotoImage(load)
panel = Label (root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
global e1
global e2
global load1
global render
global img1
global render1
global load2
global load3
global render2
global imgap1
global bap1

load1=Image.open('Loginlbl.png')
render=ImageTk.PhotoImage(load1)
img1= Label (root, image = render,bd=0,bg="lightblue")
img1.place (x = 300, y = 200)




##load2=Image.open('User.png')
##render1=ImageTk.PhotoImage(load2)
##Label(root,image=render1,bd=0).place(x=606,y=300)
##
##load3=Image.open('passbtn.png')
##render2=ImageTk.PhotoImage(load3)
##Label(root,image=render2,bd=0).place(x=606,y=370)
##

e1=Entry(root,font=("Arial", 15),bd=0)
e1.place(x=850,y=299)

e2=Entry(root,font=("Arial", 15),bd=0)
e2.place(x=850,y=450)
e2.config(show="*")


imgap1= PhotoImage(file ='loginbtn.png')
bap1 =Button (root, image=imgap1, bd=0,bg="green",command=loginpage)
bap1.place (x = 860, y = 550)



#Button(root,text="Login",command=loginpage,height=2,width=10,font=("Arial", 15),bg="lightblue",bd=0).place(x=720,y=450)

root.mainloop()
