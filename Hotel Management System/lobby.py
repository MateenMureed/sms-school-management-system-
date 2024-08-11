from tkinter import*
from tkinter import ttk
import datetime
import random
import time;
import tkinter.messagebox
from PIL import Image,ImageTk
from customer import manage_customer
from resturent import manage_resturent

class main:
    def __init__(self,master):
        self.master = master
        titlespace = " "
        self.master.title(160 * titlespace + "PEARL HOTEL")
        self.master.geometry("1050x600+0+50")
        self.master.resizable(height = False, width = False)
        self.master.config(bg = "black")
                
        #===============second window mainframe================
        
        self.frame = Frame(self.master, bd= 20,relief = RIDGE ,
                           bg = "grey54").place(x=230, y= 100 , width=600 , height = 405) 
        self.heading2 = Label(self.master,text="PEARL HOTEL",bg="grey54",fg="white",
                              font=("Times New Roman ",45,"italic")).place(x=320, y= 150)
        
        
        self.button_retaurent = Button(self.master,text = 'Manage Restaurent!',command =self.func_restuarent_billing,
                                fg="white",bg="#12121A",bd=4,width = 35,font=("Times",15,"bold")).place(x=320, y= 260)
        self.button_customer = Button(self.master, text = 'Manage customers',command =self.func_manage_customers ,
                                fg="white",bg="#12121A",bd=4,width = 35,font=("Times",15,"bold")).place(x=320, y= 360)


    def func_manage_customers(self):
        manage_customers_window = Toplevel(self.master)
        obj_manage_customer= manage_customer(manage_customers_window)
    
    def func_restuarent_billing(self):
        restuarent_billing_window = Toplevel(self.master)
        obj_restuarent_billing=manage_resturent(restuarent_billing_window)


if __name__ == "__main__":
    root = Tk()
    obj = main(root)
    root.mainloop()
