from tkinter import *
from tkinter import ttk
import datetime
import random
import time
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector

class manage_customer:
    def __init__(self,window3):
        self.window3 = window3
        titlespace = " "
        self.window3.title(160 * titlespace + "PEARL HOTEL")
        self.window3.geometry("1050x600+100+50")
        self.window3.resizable(height = False, width = False)
        self.window3.config(bg = "black")
        #===================frames============
        self.frame3 = Frame(self.window3, bd= 10,relief = RIDGE ,bg = "grey54").place(x=10, y= 5 , width=1030 , height = 100)
        self.heading_2 = Label(self.window3,text="PEARL HOTEL(Customer)",bg="grey54",fg="black",font=("Times New Roman ",45,"italic")).place(x=200, y= 20)
        self.frame4 = Frame(self.window3, bd= 10,relief = RIDGE ,bg = "grey54").place(x=10, y= 110 , width=200 , height = 480)
        self.frame5 = Frame(self.window3, bd= 10,relief = RIDGE ,bg = "grey54").place(x=215, y= 110 , width=826 , height = 250)
        frame6 = Frame(self.window3, bd= 10,relief = RIDGE ,bg = "grey54")
        frame6.place(x=215, y= 365 , width=826 , height = 225)
        
        #=================textvariables=================
        self.sd = StringVar()
        self.credit = StringVar()
        self.amount = StringVar()
        self.dos = StringVar()
        self.rn = StringVar()
        self.pm = StringVar()

        self.name = StringVar()
        self.gender = StringVar()
        self.address = StringVar()
        self.age = StringVar()
        self.cnic = StringVar()
        self.phone = StringVar()


        #============buttons=====================
        self.button_Ad_cust = Button(self.window3,text = 'Add Customer!',command=self.save_pi,
                                     fg="#12121A",bg="white",bd=4,width = 13,height = 2,font=("Times New Roman",14,"bold")).place(x=30, y= 130)
        self.button_del_cust = Button(self.window3, text = 'Delete Customer!',command=self.delete,
        fg="#12121A",bg="white",bd=4,width = 13,height = 2,font=("Times New Roman",14,"bold")).place(x=30, y= 200)
        self.button_UP_cust = Button(self.window3, text = 'Update Customer!',command=self.Update,
        fg="#12121A",bg="white",bd=4,width = 13,height = 2,font=("Times New Roman",14,"bold")).place(x=30, y= 270)
        self.button_view_cust = Button(self.window3, text = 'View Customer!',command=self.show_data,
        fg="#12121A",bg="white",bd=4,width = 13,height = 2,font=("Times New Roman",14,"bold")).place(x=30, y= 340)
        self.button_reset = Button(self.window3, text = 'Reset!',command=self.reset,
        fg="#12121A",bg="white",bd=4,width = 13,height = 2,font=("Times New Roman",14,"bold")).place(x=30, y= 410)
        self.button_exit = Button(self.window3, command = exit, text = 'Exit!',fg="#12121A",bg="white",bd=4,width = 13,height = 2,font=("Times New Roman",14,"bold")).place(x=30, y= 480)
        
        
        #===================label frame==============
        self.labelframe =LabelFrame(self.window3, bd= 5,text = "Personal Information",font=("Times New Roman",15,"italic"),relief = RIDGE ,bg = "grey54")
        self.labelframe.place(x=230, y= 120 , width=350 , height = 220)
        self.labelframe2=LabelFrame(self.window3, bd= 5,text = "Reservation Information",font=("Times New Roman",15,"italic"),relief = RIDGE ,bg = "grey54")
        self.labelframe2.place(x=600, y= 120 , width=420 , height = 220)
        
        
        #===============labels=================
        
        self.N = Label(self.window3,text="Name",fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=240,y=140)
        self.G = Label(self.window3,text="Gender",fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=240,y=170)
        self.a = Label(self.window3,text="Address",fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=240,y=200)
        self.A = Label(self.window3,text="Age",fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=240,y=230)
        self.C = Label(self.window3,text="CNIC",fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=240,y=260)
        self.p = Label(self.window3,text="Phone No.",fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=240,y=290)
         #==================entries==================

        self.NameEnt = Entry(self.window3,bd = 5,textvariable=self.name,
        fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=350,y=140,width=200)

        self.GenderEnt = Entry(self.window3,bd = 5,textvariable=self.gender,
        fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=350,y=170,width=200)

        self.addressEnt = Entry(self.window3,bd = 5,textvariable=self.address,
        fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=350,y=200,width=200)

        self.AgeEnt = Entry(self.window3,bd = 5,textvariable=self.age,
        fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=350,y=230, width=200)

        self.CNICEnt = Entry(self.window3,bd = 5,textvariable=self.cnic,
        fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=350,y=260, width=200)

        self.phoneNoEnt = Entry(self.window3,bd = 5,textvariable=self.phone,
        fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=350,y=290, width=200)

        #===============label in 2nd labelframe===================
        
        self.room_no = Label(self.window3,text="Room No",
        fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=610,y=140)

        self.dateOfReserv = Label(self.window3,text="Reservation Date",
        fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=610,y=170)

        self.stayDays = Label(self.window3,text="How Many Days?",
        fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=610,y=200)

        self.Amount = Label(self.window3,text="Amount",
        fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=610,y=230)

        self.Pay_method = Label(self.window3,text="Payment Method",
        fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=610,y=260)

        self.credit_card = Label(self.window3,text="Credit Card No.",
        fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=610,y=290)
        
        #=====================entries in 2nd Frame====================

        self.room_noEnt = Entry(self.window3,bd = 5,textvariable=self.rn,
        fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=800,y=140,width=200)

        self.sdateOfReservEnt = Entry(self.window3,bd = 5,textvariable=self.dos,
        fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=800,y=170,width=200)

        self.stayDaysEnt = Entry(self.window3,bd = 5,textvariable=self.sd,
        fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=800,y=200,width=200)

        self.AmountEnt = Entry(self.window3,bd = 5,textvariable=self.amount,
        fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=800,y=230, width=200)

        self.Pay_methodEnt = Entry(self.window3,bd = 5,textvariable=self.pm,
        fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=800,y=260, width=200)

        self.credit_cardEnt = Entry(self.window3,bd = 5,textvariable=self.credit,
        fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=800,y=290, width=200)
        
        
        #==================treeview and scroll bar========================
        scroll_bar1 = Scrollbar(frame6, orient = VERTICAL)
        scroll_bar1.pack(side = RIGHT , fill = Y )
        scroll_bar2 = Scrollbar(frame6, orient = HORIZONTAL)
        scroll_bar2.pack(side = BOTTOM , fill = X )
        self.tv = ttk.Treeview(frame6, columns=(1, 2, 3,4,5,6,7,8,9,10,11,12), show='headings', height=8 , yscrollcommand =scroll_bar1.set ,xscrollcommand =scroll_bar2.set )
        scroll_bar2.config(command=self.tv.xview)
        scroll_bar1.config(command=self.tv.yview)
        self.tv.pack(side=LEFT , fill = BOTH , expand = 1)

        self.tv.heading(1, text="Name")
        self.tv.heading(2, text="Gender")
        self.tv.heading(3, text="Address")
        self.tv.heading(4, text="Age")
        self.tv.heading(5, text="CNIC")
        self.tv.heading(6, text="Phone No")
        self.tv.heading(7, text="Room No")
        self.tv.heading(8, text="Reservation Date")
        self.tv.heading(9, text="Days")
        self.tv.heading(10, text="Amount")
        self.tv.heading(11, text="Payment Mathod")
        self.tv.heading(12, text="Credit No")

        
        self.tv.column(1 , width = 70)
        self.tv.column(2 , width = 200)
        self.tv.column(3 , width = 200)
        self.tv.column(4 , width = 200)
        self.tv.column(5 , width = 200)
        self.tv.column(6 , width = 200)
        self.tv.column(7 , width = 100)
        self.tv.column(8 , width = 100)
        self.tv.bind("<ButtonRelease>",self.get)

    def save_pi(self):
        conn = mysql.connector.connect(host="localhost", user = "root", password = "razeen", database = "HOTEL")
        cursor = conn.cursor()
        cursor.execute("insert into PI values(%s ,%s ,%s ,%s ,%s, %s,%s ,%s ,%s ,%s ,%s, %s)",(
                                                                        self.name.get(),
                                                                        self.gender.get(),
                                                                        self.address.get(),
                                                                        self.age.get(),
                                                                        self.cnic.get(),
                                                                        self.phone.get(),
                                                                        self.rn.get(),
                                                                        self.dos.get(),
                                                                        self.sd.get(),
                                                                        self.amount.get(),
                                                                        self.pm.get(),
                                                                        self.credit.get()

        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data Added Successfully")

    def Update(self):
        conn = mysql.connector.connect(host="localhost", user = "root", password = "razeen", database = "HOTEL")
        cursor = conn.cursor()
        cursor.execute("update PI set NAME= %s, GENDER= %s, ADDRESS= %s, AGE= %s, PHONE= %s, ROOM_NO = %s, RESERVATION_DATE = %s, HOW = %s, AMOUNT = %s,P_METHOD = %s, CARD_NO = %s where CNIC= %s ",(
                                                                                                                                                                        self.name.get(),
                                                                                                                                                                        self.gender.get(),
                                                                                                                                                                        self.address.get(),
                                                                                                                                                                        self.age.get(),
                                                                                                                                                                        self.phone.get(),
                                                                                                                                                                        self.rn.get(),
                                                                                                                                                                        self.dos.get(),
                                                                                                                                                                        self.sd.get(),
                                                                                                                                                                        self.amount.get(),
                                                                                                                                                                        self.pm.get(),
                                                                                                                                                                        self.credit.get(),
                                                                                                                                                                        self.cnic.get()
        ))
        conn.commit()
        self.show_data()
        conn.close()
        messagebox.showinfo("Success", "Data Updated Successfully")
    
    def show_data(self):
        conn = mysql.connector.connect(host="localhost", user = "root", password = "razeen", database = "HOTEL")
        cursor = conn.cursor()
        cursor.execute("select * from PI")
        data = cursor.fetchall()
        if len(data)!=0:
            self.tv.delete(*self.tv.get_children())
            for i in data:
                self.tv.insert("",END,values=i)
                conn.commit()
            conn.close()

    def delete(self):
        conn = mysql.connector.connect(host="localhost", user = "root", password = "razeen", database = "HOTEL")
        cursor = conn.cursor()
        query=("delete from PI where CNIC=%s")
        value=(self.cnic.get(),)
        cursor.execute(query,value)
        conn.commit()
        self.show_data()
        conn.close()
        messagebox.showinfo("Success", "Data deleted Successfully")
    
    def get(self,event=""):
        row = self.tv.focus()
        content = self.tv.item(row)
        data = content["values"]
        self.name.set(data[0])
        self.gender.set(data[1])
        self.address.set(data[2])
        self.age.set(data[3])
        self.cnic.set(data[4])
        self.phone.set(data[5])
        self.rn.set(data[6])
        self.dos.set(data[7])
        self.sd.set(data[8])
        self.amount.set(data[9])
        self.pm.set(data[10])
        self.credit.set(data[11])

    def reset(self):
        self.name.set("")
        self.gender.set("")
        self.address.set("")
        self.age.set("")
        self.cnic.set("")
        self.phone.set("")
        self.rn.set("")
        self.dos.set("")
        self.sd.set("")
        self.amount.set("")
        self.pm.set("")
        self.credit.set("")



if __name__ == '__main__':
    root = Tk()
    obj = manage_customer(root)
    root.mainloop()

          
