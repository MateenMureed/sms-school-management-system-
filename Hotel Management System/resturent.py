from tkinter import *
from tkinter import ttk
import datetime
import random
import time;
from tkinter import messagebox
from PIL import Image,ImageTk

class manage_resturent:
    def __init__(self,window1):
        self.window1 = window1
        #Giving main window a title
        self.window1.title("Restaurant Billing System")
        #Giving window a default size.
        self.window1.geometry('1500x1200')

        #===========================Frames=========================
        #making a frame for heading.
        top= Frame(window1,relief=RIDGE)
        top.pack(side=TOP)
        R_name= Label(top,text='Pearl Restaurant Billing System', font=('aerolite',36,'italic'),fg='#2ECC71')
        R_name.pack(side=TOP)
        Greeting=Label(top,text='"Courteous treatment will make a customer a walking advertisement" - JAMES CASH PENNY',font=('Courier',14,'italic'))
        Greeting.pack(side=BOTTOM)
        #for menu
        Item= Frame(window1,relief=RIDGE)
        Item.pack(side=TOP)
        food = Frame(Item,relief=GROOVE) 
        food.pack(side=LEFT)
        drinks = Frame(Item,relief=GROOVE)
        drinks.pack(side=RIGHT)
        total= Frame(Item,relief=GROOVE)
        total.pack(side=BOTTOM)
        #for billing
        billing= Frame(window1,relief=RIDGE)
        billing.pack(side=RIGHT)
        recipt= Frame(billing,relief=GROOVE)
        recipt.pack(side=TOP)
        recipt_button= Frame(billing,relief=GROOVE)
        recipt_button.pack(side=BOTTOM)
        #=============================Variable=============================

        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        self.var4=IntVar()
        self.var5=IntVar()
        self.var6=IntVar()
        self.var7=IntVar()
        self.var8=IntVar()
        self.var9=IntVar()
        self.var10=IntVar()
        self.var11=IntVar()
        self.var12=IntVar()
        self.var13=IntVar()
        self.var14=IntVar()
        self.var15=IntVar()
        self.var16=IntVar()


        self.DateofOrder= StringVar()
        self.Recipt_ref= StringVar()
        self.TaxPaid= StringVar()
        self.Subtotal=StringVar()
        self.Totalcost= StringVar()
        self.Costofdishes = StringVar()
        self.Costofdrinks= StringVar()
        self.Servicetax= StringVar()

        text_input = StringVar()
        operator=""

        self.C_Pepsi = StringVar()
        self.C_Coke_cola = StringVar()
        self.C_Marinda = StringVar()
        self.C_Dew = StringVar()
        self.C_7up = StringVar()
        self.C_String = StringVar()
        self.C_Fanta = StringVar()
        self.C_Sprite = StringVar()

        self.D_Chickenbiryani = StringVar()
        self.D_Chickenkarahi = StringVar()
        self.D_Muttonkarahi = StringVar()
        self.D_Beefkarahi = StringVar()
        self.D_Qeema= StringVar()
        self.D_Sajji = StringVar()
        self.D_Chargha = StringVar()
        self.D_Paratha = StringVar()

        self.C_Pepsi.set("0")
        self.C_Coke_cola.set("0")
        self.C_Marinda.set("0")
        self.C_Dew.set("0")
        self.C_7up.set("0")
        self.C_String.set("0")
        self.C_Fanta.set("0")
        self.C_Sprite.set("0")

        self.D_Chickenbiryani.set("0")
        self.D_Chickenkarahi.set("0")
        self.D_Muttonkarahi.set("0")
        self.D_Beefkarahi.set("0")
        self.D_Qeema.set("0")
        self.D_Sajji.set("0")
        self.D_Chargha.set("0")
        self.D_Paratha.set("0")

        self.DateofOrder.set(time.strftime("%d/%m/%y"))



        
        #===========================Checkbox for drinks==========================

        Pepsi=Checkbutton(drinks, text="Pepsi",variable=self.var1, onvalue=1, offvalue=0,font=('aerolite',16,'italic')
                  ,command=self.chkPepsi)
        Pepsi.grid(row=0,sticky=W)
        
        Coke_cola=Checkbutton(drinks, text="Coka Cola", variable=self.var2, onvalue=1, offvalue=0,font=('aerolite',16,'italic')
                    ,command=self.chkCoke_cola).grid(row=1,sticky=W)
        Marinda=Checkbutton(drinks, text="Marinda",variable=self.var3, onvalue=1, offvalue=0,font=('aerolite',16,'italic')
                    ,command=self.chkMarinda).grid(row=2,sticky=W)
        Dew=Checkbutton(drinks, text="Dew",variable=self.var4, onvalue=1, offvalue=0,font=('aerolite',16,'italic')
                ,command=self.chkDew).grid(row=3,sticky=W)
        up7=Checkbutton(drinks, text="7up",variable=self.var5, onvalue=1, offvalue=0,font=('aerolite',16,'italic')
                ,command=self.chk7up).grid(row=4,sticky=W)
        String=Checkbutton(drinks, text="String",variable=self.var6, onvalue=1, offvalue=0,font=('aerolite',16,'italic')
                   ,command=self.chkString).grid(row=5,sticky=W)
        Fanta=Checkbutton(drinks, text="Fanta",variable=self.var7, onvalue=1, offvalue=0,font=('aerolite',16,'italic')
                  ,command=self.chkFanta).grid(row=6,sticky=W)
        Sprite=Checkbutton(drinks, text="Sprite",variable=self.var8, onvalue=1, offvalue=0,font=('aerolite',16,'italic')
                   ,command=self.chkSprite).grid(row=7,sticky=W)

        #===========================Entry box for drinks=========================

        self.txtPepsi= Entry(drinks,font=('aerolite',16,'italic'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=self.C_Pepsi)
        self.txtPepsi.grid(row=0,column=1)
        self.txtCoke_cola= Entry(drinks,font=('aerolite',16,'italic'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=self.C_Coke_cola)
        self.txtCoke_cola.grid(row=1,column=1)
        self.txtMarinda= Entry(drinks,font=('aerolite',16,'italic'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=self.C_Marinda)
        self.txtMarinda.grid(row=2,column=1)
        self.txtDew= Entry(drinks,font=('aerolite',16,'italic'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=self.C_Dew)
        self.txtDew.grid(row=3,column=1)
        self.txt7up= Entry(drinks,font=('aerolite',16,'italic'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=self.C_7up)
        self.txt7up.grid(row=4,column=1)
        self.txtString= Entry(drinks,font=('aerolite',16,'italic'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=self.C_String)
        self.txtString.grid(row=5,column=1)
        self.txtFanta= Entry(drinks,font=('aerolite',16,'italic'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=self.C_Fanta)
        self.txtFanta.grid(row=6,column=1)
        self.txtSprite= Entry(drinks,font=('aerolite',16,'italic'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=self.C_Sprite)
        self.txtSprite.grid(row=7,column=1)
        
        #=============================Checkbox for dishes===============================

        Chickenbiryani=Checkbutton(food, text='Chicken Biryani', variable=self.var9, onvalue=1, offvalue=0, font=('aerolite',16,'italic')
                , command=self.chkChickenbiryani).grid(row=0,sticky=W)
        Chickenkarahi=Checkbutton(food, text='Chicken Karahi', variable=self.var10, onvalue=1, offvalue=0, font=('aerolite',16,'italic')
                  , command=self.chkChickenkarahi).grid(row=1,sticky=W)
        Muttonkarahi=Checkbutton(food, text='Mutton Karahi', variable=self.var11, onvalue=1, offvalue=0, font=('aerolite',16,'italic')
                  ,command=self.chkMuttonkarahi).grid(row=2,sticky=W)
        Beefkarahi=Checkbutton(food, text='Beef Karahi', variable=self.var12, onvalue=1, offvalue=0, font=('aerolite',16,'italic')
                  , command=self.chkBeefkarahi).grid(row=3,sticky=W)
        Qeema=Checkbutton(food, text='Qeema', variable=self.var13, onvalue=1, offvalue=0, font=('aerolite',16,'italic')
                  , command=self.chkQeema).grid(row=4,sticky=W)
        Sajji=Checkbutton(food, text='Sajji', variable=self.var14, onvalue=1, offvalue=0, font=('aerolite',16,'italic')
                  , command=self.chkSajji).grid(row=5,sticky=W)
        Chargha=Checkbutton(food, text='Chargha', variable=self.var15, onvalue=1, offvalue=0, font=('aerolite',16,'italic')
                  , command=self.chkChargha).grid(row=6,sticky=W)
        Paratha=Checkbutton(food, text='Paratha', variable=self.var16, onvalue=1, offvalue=0, font=('aerolite',16,'italic')
                  , command=self.chkParatha).grid(row=7,sticky=W)
        
        #====================================Entrybox for chicken============================

        self.txtChickenbiryani= Entry(food,font=('aerolite',16,'italic'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=self.D_Chickenbiryani)
        self.txtChickenbiryani.grid(row=0,column=1)
        self.txtChickenkarahi= Entry(food,font=('aerolite',16,'italic'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=self.D_Chickenkarahi)
        self.txtChickenkarahi.grid(row=1,column=1)
        self.txtMuttonkarahi= Entry(food,font=('aerolite',16,'italic'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=self.D_Muttonkarahi)
        self.txtMuttonkarahi.grid(row=2,column=1)
        self.txtBeefkarahi= Entry(food,font=('aerolite',16,'italic'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=self.D_Beefkarahi)
        self.txtBeefkarahi.grid(row=3,column=1)
        self.txtQeema= Entry(food,font=('aerolite',16,'italic'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=self.D_Qeema)
        self.txtQeema.grid(row=4,column=1)
        self.txtSajji= Entry(food,font=('aerolite',16,'italic'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=self.D_Sajji)
        self.txtSajji.grid(row=5,column=1)
        self.txtChargha= Entry(food,font=('aerolite',16,'italic'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=self.D_Chargha)
        self.txtChargha.grid(row=6,column=1)
        self.txtParatha= Entry(food,font=('aerolite',16,'italic'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=self.D_Paratha)
        self.txtParatha.grid(row=7,column=1)
        
        #================================ TOTAL COST OF FOOD =================================       

        LCDrink =Label(total, font=('arial',14,'bold'),text='Cost of Drinks\t',fg='black')
        LCDrink.grid(row=0,column=0, sticky=W)
        TCDrink= Entry(total, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=self.Costofdrinks)
        TCDrink.grid(row=0, column=1)

        LCDishes =Label(total, font=('arial',14,'bold'),text='Cost of Dishes\t',fg='black')
        LCDishes.grid(row=1,column=0, sticky=W)
        TCDishes= Entry(total, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=self.Costofdishes)
        TCDishes.grid(row=1, column=1)

        LSC =Label(total, font=('arial',14,'bold'),text='Service Charge\t',fg='black')
        LSC.grid(row=2,column=0, sticky=W)
        TSC= Entry(total, bg='white',width=40, bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=self.Servicetax)
        TSC.grid(row=2, column=1)
        
        #============================== Amount Payed =============================

        LPT =Label(total, font=('arial',14,'bold'),text='\tPaid Tax',fg='black')
        LPT.grid(row=0,column=2, sticky=W)
        TPT = Entry(total, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=self.TaxPaid)
        TPT.grid(row=0, column=3)

        LST =Label(total, font=('arial',14,'bold'),text='\tSub Total',fg='black')
        LST.grid(row=1,column=2, sticky=W)
        TST= Entry(total, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=self.Subtotal)
        TST.grid(row=1, column=3)

        LTC =Label(total, font=('arial',14,'bold'),text='\tTotal Cost',fg='black')
        LTC.grid(row=2,column=2, sticky=W)
        TTC= Entry(total, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=self.Totalcost)
        TTC.grid(row=2, column=3)


        #======================================= RECEIPT =============================

        self.txtReceipt= Text(recipt, width=46, height=12, bg='white', bd=4, font=('arial',12,'bold'))
        self.txtReceipt.grid(row=0, column=0)

        #====================================== RECEIPT BUTTONS ===========================

        btnTotal=Button(recipt_button, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                        width=4, text="Total", bg="Powder Blue", command=self.CostofItem).grid(row=0,column=0)
        btnReceipt=Button(recipt_button, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                        width=4, text="Receipt", bg="Powder Blue", command=self.Receipt).grid(row=0,column=1)
        btnReset=Button(recipt_button, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                        width=4, text="Reset", bg="Powder Blue", command=self.p_reset).grid(row=0,column=2)
        btnExit=Button(recipt_button, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                        width=4, text="Exit", bg="Powder Blue", command=self.p_Exit).grid(row=0,column=3)
    def Receipt(self):
        self.txtReceipt.delete("1.0",END)
        a= random.randint(1,1000)
        r_ref= str(a)
        self.Recipt_ref.set("BILL" + r_ref)
        
        self.txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + self.Recipt_ref.get() + "\t" + self.DateofOrder.get() + "\n")
        self.txtReceipt.insert(END, 'Item:\t\t\t' + "No of Items\n")
        self.txtReceipt.insert(END, 'Pepsi: \t\t\t\t' + self.C_Pepsi.get() + "\n")
        self.txtReceipt.insert(END, 'Coka Cola: \t\t\t\t' + self.C_Coke_cola.get() + "\n")
        self.txtReceipt.insert(END, 'Marinda: \t\t\t\t' + self.C_Marinda.get() + "\n")
        self.txtReceipt.insert(END, 'Dew: \t\t\t\t' + self.C_Dew.get() + "\n")
        self.txtReceipt.insert(END, '7up: \t\t\t\t' + self.C_7up.get() + "\n")
        self.txtReceipt.insert(END, 'String: \t\t\t\t' + self.C_String.get() + "\n")
        self.txtReceipt.insert(END, 'Fanta: \t\t\t\t' + self.C_Fanta.get() + "\n")
        self.txtReceipt.insert(END, 'Sprite: \t\t\t\t' + self.C_Sprite.get() + "\n")
        self.txtReceipt.insert(END, 'Chicken Biryani: \t\t\t\t' + self.D_Chickenbiryani.get() + "\n")
        self.txtReceipt.insert(END, 'Chicken Karahi: \t\t\t\t' + self.D_Chickenkarahi.get() + "\n")
        self.txtReceipt.insert(END, 'Mutton Karahi: \t\t\t\t' + self.D_Muttonkarahi.get() + "\n")
        self.txtReceipt.insert(END, 'Beef Karahi: \t\t\t\t' + self.D_Beefkarahi.get() + "\n")
        self.txtReceipt.insert(END, 'Qeema: \t\t\t\t' + self.D_Qeema.get() + "\n")
        self.txtReceipt.insert(END, 'Sajji: \t\t\t\t' + self.D_Sajji.get() + "\n")
        self.txtReceipt.insert(END, 'Chargha: \t\t\t\t' + self.D_Chargha.get() + "\n")
        self.txtReceipt.insert(END, 'Paratha: \t\t\t\t' +self. D_Paratha.get() + "\n")


    def chkPepsi(self):
        if(self.var1.get()==1):
            self.txtPepsi.configure(state= NORMAL)
            self.txtPepsi.focus()
            self.txtPepsi.delete('0', END)
            self.C_Pepsi.set("")
        elif(self.var1.get()==0):
            self.txtPepsi.configure(state= DISABLED)
            self.C_Pepsi.set("0")
    def chkCoke_cola(self):
        if(self.var2.get()==1):
            self.txtCoke_cola.configure(state= NORMAL)
            self.txtCoke_cola.focus()
            self.txtCoke_cola.delete('0', END)
            self.C_Coke_cola.set("")
        elif(self.var2.get()==0):
            self.txtCoke_cola.configure(state= DISABLED)
            self.C_Coke_cola.set("0")
    def chkMarinda(self):
        if(self.var3.get()==1):
            self.txtMarinda.configure(state= NORMAL)
            self.txtMarinda.focus()
            self.txtMarinda.delete('0', END)
            self.C_Marinda.set("")
        elif(self.var3.get()==0):
            self.txtMarinda.configure(state= DISABLED)
            self.C_Marinda.set("0")
    def chkDew(self):
        if(self.var4.get()==1):
            self.txtDew.configure(state= NORMAL)
            self.txtDew.focus()
            self.txtDew.delete('0', END)
            self.C_Dew.set("")
        elif(self.var4.get()==0):
            self.txtDew.configure(state= DISABLED)
            self.C_Dew.set("0")
    def chk7up(self):
        if(self.var5.get()==1):
            self.txt7up.configure(state= NORMAL)
            self.txt7up.focus()
            self.txt7up.delete('0', END)
            self.C_7up.set("")
        elif(self.var5.get()==0):
            self.txt7up.configure(state= DISABLED)
            self.C_7up.set("0")
    def chkString(self):
        if(self.var6.get()==1):
            self.txtString.configure(state= NORMAL)
            self.txtString.focus()
            self.txtString.delete('0', END)
            self.C_String.set("")
        elif(self.var6.get()==0):
            self.txtString.configure(state= DISABLED)
            self.C_String.set("0")
    def chkFanta(self):
        if(self.var7.get()==1):
            self.txtFanta.configure(state= NORMAL)
            self.txtFanta.focus()
            self.txtFanta.delete('0', END)
            self.C_Fanta.set("")
        elif(self.var7.get()==0):
            self.txtFanta.configure(state= DISABLED)
            self.C_Fanta.set("0")
    def chkSprite(self):
        if(self.var8.get()==1):
            self.txtSprite.configure(state= NORMAL)
            self.txtSprite.focus()
            self.txtSprite.delete('0', END)
            self.C_Sprite.set("")
        elif(self.var8.get()==0):
            self.txtSprite.configure(state= DISABLED)
            self.C_Sprite.set("0")
    def chkChickenbiryani(self):
        if(self.var9.get()==1):
            self.txtChickenbiryani.configure(state= NORMAL)
            self.txtChickenbiryani.focus()
            self.txtChickenbiryani.delete('0', END)
            self.D_Chickenbiryani.set("")
        elif(self.var9.get()==0):
            self.txtChickenbiryani.configure(state= DISABLED)
            self.D_Chickenbiryani.set("0")
    def chkChickenkarahi(self):
        if(self.var10.get()==1):
            self.txtChickenkarahi.configure(state= NORMAL)
            self.txtChickenkarahi.focus()
            self.txtChickenkarahi.delete('0', END)
            self.D_Chickenkarahi.set("")
        elif(self.var10.get()==0):
            self.txtChickenkarahi.configure(state= DISABLED)
            self.D_Chickenkarahi.set("0")
    def chkMuttonkarahi(self):
        if(self.var11.get()==1):
            self.txtMuttonkarahi.configure(state= NORMAL)
            self.txtMuttonkarahi.focus()
            self.txtMuttonkarahi.delete('0', END)
            self.D_Muttonkarahi.set("")
        elif(self.var11.get()==0):
            self.txtMuttonkarahi.configure(state= DISABLED)
            self.D_Muttonkarahi.set("0")
    def chkBeefkarahi(self):
        if(self.var12.get()==1):
            self.txtBeefkarahi.configure(state= NORMAL)
            self.txtBeefkarahi.focus()
            self.txtBeefkarahi.delete('0', END)
            self.D_Beefkarahi.set("")
        elif(self.var12.get()==0):
            self.txtBeefkarahi.configure(state= DISABLED)
            self.D_Beefkarahi.set("0")
    def chkQeema(self):
        if(self.var13.get()==1):
            self.txtQeema.configure(state= NORMAL)
            self.txtQeema.focus()
            self.txtQeema.delete('0', END)
            self.D_Qeema.set("")
        elif(self.var13.get()==0):
            self.txtQeema.configure(state= DISABLED)
            self.D_Qeema.set("0")
    def chkSajji(self):
        if(self.var14.get()==1):
            self.txtSajji.configure(state= NORMAL)
            self.txtSajji.focus()
            self.txtSajji.delete('0', END)
            self.D_Sajji.set("")
        elif(self.var14.get()==0):
            self.txtSajji.configure(state= DISABLED)
            self.D_Sajji.set("0")
    def chkChargha(self):
        if(self.var15.get()==1):
            self.txtChargha.configure(state= NORMAL)
            self.txtChargha.focus()
            self.txtChargha.delete('0', END)
            self.D_Chargha.set("")
        elif(self.var15.get()==0):
            self.txtChargha.configure(state= DISABLED)
            self.D_Chargha.set("0")
    def chkParatha(self):
        if(self.var16.get()==1):
            self.txtParatha.configure(state= NORMAL)
            self.txtParatha.focus()
            self.txtParatha.delete('0', END)
            self.D_Paratha.set("")
        elif(self.var16.get()==0):
            self.txtParatha.configure(state= DISABLED)
            self.D_Paratha.set("0")

    def p_reset(self):
        self.C_Pepsi.set("0")
        self.C_Coke_cola.set("0")
        self.C_Marinda.set("0")
        self.C_Dew.set("0")
        self.C_7up.set("0")
        self.C_String.set("0")
        self.C_Fanta.set("0")
        self.C_Sprite.set("0")
        
        self.D_Chickenbiryani.set("0")
        self.D_Chickenkarahi.set("0")
        self.D_Muttonkarahi.set("0")
        self.D_Beefkarahi.set("0")
        self.D_Qeema.set("0")
        self.D_Sajji.set("0")
        self.D_Chargha.set("0")
        self.D_Paratha.set("0")
        
        self.TaxPaid.set("0")
        self.Subtotal.set("0")
        self.Totalcost.set("0")
        self.Costofdishes.set("0")
        self.Costofdrinks.set("0")
        self.Servicetax.set('0')
       
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)
        self.var8.set(0)
        self.var9.set(0)
        self.var10.set(0)
        self.var11.set(0)
        self.var12.set(0)
        self.var13.set(0)
        self.var14.set(0)
        self.var15.set(0)
        self.var16.set(0)
       
        self.txtPepsi.configure(state=DISABLED)
        self.txtCoke_cola.configure(state=DISABLED)
        self.txtMarinda.configure(state=DISABLED)
        self.txtDew.configure(state=DISABLED)
        self.txt7up.configure(state=DISABLED)
        self.txtString.configure(state=DISABLED)
        self.txtFanta.configure(state=DISABLED)
        self.txtSprite.configure(state=DISABLED)
        self.txtChickenbiryani.configure(state=DISABLED)
        self.txtChickenkarahi.configure(state=DISABLED)
        self.txtMuttonkarahi.configure(state=DISABLED)
        self.txtBeefkarahi.configure(state=DISABLED)
        self.txtQeema.configure(state=DISABLED)
        self.txtSajji.configure(state=DISABLED)
        self.txtChargha.configure(state=DISABLED)
        self.txtParatha.configure(state=DISABLED)
        
    def CostofItem(self):
        Item1=float(self.C_Pepsi.get())
        Item2=float(self.C_Coke_cola.get())
        Item3=float(self.C_Marinda.get())
        Item4=float(self.C_Dew.get())
        Item5=float(self.C_7up.get())
        Item6=float(self.C_String.get())
        Item7=float(self.C_Fanta.get())
        Item8=float(self.C_Sprite.get())
        
        Item9=float(self.D_Chickenbiryani.get())
        Item10=float(self.D_Chickenkarahi.get())
        Item11=float(self.D_Muttonkarahi.get())
        Item12=float(self.D_Beefkarahi.get())
        Item13=float(self.D_Qeema.get())
        Item14=float(self.D_Sajji.get())
        Item15=float(self.D_Chargha.get())
        Item16=float(self.D_Paratha.get())
        
        PriceofDrinks=((Item1 * 35 ) + (Item2 * 35) + (Item3 * 35) + (Item4 * 35)
                       + (Item5 * 35) + (Item6 * 40) + (Item7 * 35) + (Item8 * 35))
        PriceofDishes=((Item9 * 120) + (Item10 * 300) + (Item11 * 500) + (Item12 * 400)
                       + (Item13 * 250) + (Item14 * 650) + (Item15 * 350) + (Item16 * 30))

        DrinksPrice="Rs", str('%.2f'%(PriceofDrinks))
        DishesPrice="Rs", str('%.2f'%(PriceofDishes))
        self.Costofdishes.set(DishesPrice)
        self.Costofdrinks.set(DrinksPrice)
        SC="Rs", str('%.2f'%(2.5))
        self.Servicetax.set(SC)

        SubTotalofITEMS="Rs", str('%.2f'%(PriceofDrinks + PriceofDishes + 2.5))
        self.Subtotal.set(SubTotalofITEMS)

        Tax="Rs", str('%.2f'%((PriceofDrinks + PriceofDishes + 2.5)*0.17))
        self.TaxPaid.set(Tax)
        TT=((PriceofDrinks + PriceofDishes + 2.5) *0.17)
        TC="Rs", str('%.2f'%(PriceofDishes + PriceofDrinks + 2.5 + TT))
        self.Totalcost.set(TC)
        
    def p_Exit(self):
        p_Exit = messagebox.askyesno("Exit","Are you sure to exit? ")
        if p_Exit > 0:
            self.restuarent_billing_window.destory()
            return

if __name__ == '__main__':
    root = Tk()
    obj = manage_resturent(root)
    root.mainloop()
