from tkinter import *
from tkinter import ttk
import datetime
import random
import time;
from tkinter import messagebox
from PIL import Image,ImageTk
from lobby import main

class login:
     def __init__(self,root):
          self.root = root
          titlespace = " "
          self.root.title(160 * titlespace + "PEARL HOTEL")
          self.root.geometry("1000x600+0+50")
          self.root.resizable(height = False, width = False)
          self.root.config(bg = "grey6")
          
          self.username = StringVar()
          self.password = StringVar()

          def login():
               if self.username.get() == "admin" and self.password.get() == "admin":
                    self.new_window = Toplevel(self.root)
                    self.app = main(self.new_window)
               else:
                    messagebox.showerror("Error","Invalid User or Password")
                    
          # Background Image
          self.img = Image.open(r"C:\Users\MATEEN MUREED\Desktop\Project 2nd Semester\bg2.jpg")
          new = self.img.resize((1000,600),Image.ANTIALIAS)
          self.img =ImageTk.PhotoImage(new)
          self.img_lbl = Label(self.root, image=self.img,compound=TOP,width=1000,height=600,bg="white")
          self.img_lbl.place(x=0, y=0)

          # Frame
          self.frame1 = Frame(self.root,bg = "black").place(x=80, y= 100 , width=300 , height = 400)

          # Frame 1 Image
          self.i = Image.open(r"img2.jpg")
          n = self.i.resize((300,400),Image.ANTIALIAS)
          self.i =ImageTk.PhotoImage(n)
          self.i_lbl = Label(self.frame1, image=self.i,compound=TOP,width=300,height=400,bg="white")
          self.i_lbl.place(x=80, y=100)

          # Frame 2
          self.frame2  =Frame(self.root,bg = "white").place(x=380, y= 100 , width=600 , height = 405)

                  
          self.heading = Label(self.frame2,text="PEARL HOTEL",bg="white",fg="black",
                             font=("Times New Roman ",40,"italic")).place(x=500, y= 150)
        
          self.user = Label(self.frame2,text="USERNAME",fg="black",bg="white",
                              font=("Times New Roman",20,"italic")).place(x=500,y=230)
        
          self.user_entry=Entry(self.frame2,bg="gray",textvariable=self.username,
                              font=("Times New Roman",15),width=20).place(x=660,y=230)
        
          self.passwaord = Label(self.frame2,text="PASSWORD",fg="black",bg="white",
                               font=("Times New Roman",20,"italic"))
          self.passwaord.place(x=500,y=300)
        
          self.pass_entry=Entry(self.frame2,bg="gray",font=("Times New Roman",15),
                              textvariable=self.password,show="*",width=20).place(x=660,y=300)
        
          login_button=Button(self.frame2,text="Login",fg="#A99C94",bg="#12121A",command=login,
                            bd=4,width = 15,font=("Times New Roman",15,"bold")).place(x=600,y=400)   

if __name__ == "__main__":
    root = Tk()
    obj = login(root)
    root.mainloop()
