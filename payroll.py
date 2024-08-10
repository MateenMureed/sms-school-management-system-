from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from datetime import date
import mysql.connector
from fpdf import FPDF
import os

class FrontEnd:
    def __init__(self,mm):
        self.mm = mm
        self.mm.title("Payroll Management System")
        self.mm.geometry("810x603+200+85")
        self.mm.resizable("False","False")

        self.search_by = StringVar()
        self.search = StringVar()
        self.search_by2 = StringVar()
        self.search2 = StringVar()
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.basic = StringVar()
        self.medical = StringVar()
        self.house = StringVar()
        self.conveyance = StringVar()
        self.gross = StringVar()
        self.tax = StringVar()
        self.loan = StringVar()
        self.advance = StringVar()
        self.net = StringVar()
        self.date = StringVar()
        self.month = StringVar()
        self.receipt = StringVar()
        self.id = StringVar()
        self.name = StringVar()
        self.account = StringVar()
        self.join = StringVar()
        self.role = StringVar()
        self.today = date.today()
        self.getadvance = StringVar()
        self.getloan = StringVar()

        style = ttk.Style()
        style.theme_use("clam")

        # Title Frame
        title_frame = Frame(self.mm, width=810, height=50 ,bg="lightgreen")
        title_frame.place(x=0,y=0)

        title = Label(title_frame, text="STAFF PAYROLL MANAGEMENT SYSTEM", bg="lightgreen",
        font=("Times",23,"bold","italic"),fg="black")
        title.place(x=0,y=3)

        self.btn_view_all = Button(title_frame, relief=GROOVE, bd=4, width=10, font=("Arial",10,"bold"),
        bg="cyan", text="View_All", command=self.view_all)
        self.btn_view_all.place(x=620, y=10)

        self.btn_back = Button(title_frame, relief=GROOVE, bd=4, width=8, font=("Arial",10,"bold"),
        bg="cyan", text="Back", command=self.back)
        self.btn_back.place(x=720, y=10)

        # Search Frame
        search_frame = LabelFrame(self.mm, text="Search Staff", font=("Times",12,"bold"),
        width=405, height=60, bg="seashell")
        search_frame.place(x=0,y=50)

        combo_search_by = ttk.Combobox(search_frame, state="readonly", font=("Times",12,"bold"),
        textvariable=self.search_by)
        combo_search_by["values"] = ("Search By","ID","Staff_Name","CNIC","Phone")
        combo_search_by.current("0")
        combo_search_by.place(x=10,y=5)

        ent_search = Entry(search_frame, textvariable=self.search, font=("Times",12,"bold"))
        ent_search.place(x=200, y=5)
        ent_search.bind("<Return>",self.search_staff)

        # Receipt Frame
        self.receipt_frame = LabelFrame(self.mm, text="Receipt", font=("Times",12,"bold"),
        width=404, height=473, bg="#ffffcc")
        self.receipt_frame.place(x=405,y=50)

        self.txt_receipt = Text(self.receipt_frame,relief=RIDGE,font=("Times",12,"bold"),
        bd=2, bg="seashell")
        self.txt_receipt.place(x=5,y=0,width=390,height=445)

        # Button Frame
        Button_frame = LabelFrame(self.mm, text="Button", font=("Times",12,"bold"),
        width=404, height=80, bg="#ffffcc")
        Button_frame.place(x=405,y=523)

        btn_calculate = Button(Button_frame, relief=GROOVE, bd=2, width=8, font=("Arial",10,"bold"),
        bg="cyan", text="Calculate", command=self.net_calculate)
        btn_calculate.place(x=10, y=10)

        btn_save = Button(Button_frame, command=self.save, relief=GROOVE, bd=2, width=8, font=("Arial",10,"bold"),
        bg="cyan", text="Submit")
        btn_save.place(x=84, y=10)

        btn_reset = Button(Button_frame, relief=GROOVE, bd=2, width=8, font=("Arial",10,"bold"),
        bg="cyan", text="Reset", command=self.reset)
        btn_reset.place(x=158, y=10)

        btn_update = Button(Button_frame, relief=GROOVE, bd=2, width=8, font=("Arial",10,"bold"),
        bg="cyan", text="Update", command=self.update)
        btn_update.place(x=232, y=10)

        btn_exit = Button(Button_frame, relief=GROOVE, bd=2, width=8, font=("Arial",10,"bold"),
        bg="cyan", text="Exit", command=self.exit)
        btn_exit.place(x=306, y=10)


        # Staff Frame
        staff_frame = LabelFrame(self.mm,text="Staff Information", font=("Times",12,"bold"),
        width=405, height=120, bg="seashell")
        staff_frame.place(x=0,y=113)

        lbl_id = Label(staff_frame, text="Staff ID", font=("Arial",10,"bold"), bg="seashell")
        lbl_id.place(x=0,y=5)

        ent_id = Entry(staff_frame, textvariable=self.id, font=("Arial",10,"bold"),width=15)
        ent_id.place(x=70,y=5)

        lbl_name = Label(staff_frame, text="Staff Name", font=("Arial",10,"bold"), bg="seashell")
        lbl_name.place(x=190,y=5)

        ent_name = Entry(staff_frame, textvariable=self.name, font=("Arial",10,"bold"),width=15)
        ent_name.place(x=280,y=5)

        lbl_role = Label(staff_frame, text="Staff Role", font=("Arial",10,"bold"), bg="seashell")
        lbl_role.place(x=0,y=30)

        ent_role = Entry(staff_frame, textvariable=self.role, font=("Arial",10,"bold"),width=15)
        ent_role.place(x=70,y=30)

        lbl_join = Label(staff_frame, text="Joining Date", font=("Arial",10,"bold"), bg="seashell")
        lbl_join.place(x=190,y=30)

        ent_join = Entry(staff_frame, textvariable=self.join, font=("Arial",10,"bold"),width=15)
        ent_join.place(x=280,y=30)

        lbl_account = Label(staff_frame, text="Account", font=("Arial",10,"bold"), bg="seashell")
        lbl_account.place(x=0,y=60)

        ent_account = Entry(staff_frame, textvariable=self.account, font=("Arial",10,"bold"),width=15)
        ent_account.place(x=70,y=60)

        lbl_date = Label(staff_frame, text="Current Date", font=("Arial",10,"bold"), bg="seashell")
        lbl_date.place(x=190,y=60)

        ent_date = Entry(staff_frame, textvariable=self.date, font=("Arial",10,"bold"),width=15)
        ent_date.place(x=280,y=60)
        ent_date.insert(0,self.today)

        # Payroll Frame
        pay_frame = LabelFrame(self.mm,text="Payroll Frame", font=("Times",12,"bold"),
        width=405, height=370, bg="seashell")
        pay_frame.place(x=0,y=233)

        # Basic Salary Frame
        basic_salary = LabelFrame(pay_frame,text="Basic Salary", font=("Times",12,"bold"),
        width=380, height=80, bg="seashell",fg="red")
        basic_salary.place(x=10,y=0)

        lbl_basic_salary = Label(basic_salary, text="Basic Salary", font=("Arial",10,"bold"), bg="seashell")
        lbl_basic_salary.place(x=0,y=5)

        ent_basic_salary = Entry(basic_salary, textvariable=self.basic, width=15, font=("Arial",10,"bold"))
        ent_basic_salary.place(x=90,y=5)
        ent_basic_salary.bind("<KeyRelease>",self.calculate)

        self.combo_select_month = ttk.Combobox(basic_salary,state="readonly",textvariable=self.month,
        font=("Times",10,"bold"),width=8)
        self.combo_select_month["value"]=("Month","January","February","March","April",
        "May","June","July","August","September","October","November","December")
        self.combo_select_month.current(0)
        self.combo_select_month.place(x=210,y=5)

        ent_receipt = Entry(basic_salary, textvariable=self.receipt, width=6, font=("Arial",12,"bold"))
        ent_receipt.place(x=300,y=4)

        lbl_get_loan = Label(basic_salary, text="Get Loan", font=("Arial",10,"bold"), bg="seashell")
        lbl_get_loan.place(x=0,y=30)

        ent_get_loan = Entry(basic_salary, textvariable=self.getloan, width=15, font=("Arial",10,"bold"))
        ent_get_loan.place(x=90,y=30)


        lbl_get_loan = Label(basic_salary, text="Adv. Salary" , font=("Arial",10,"bold"), bg="seashell")
        lbl_get_loan.place(x=205,y=30)

        ent_get_advance = Entry(basic_salary, textvariable=self.getadvance, width=6, font=("Arial",12,"bold"))
        ent_get_advance.place(x=300,y=30)



        # Allowance Frame
        allowance = LabelFrame(pay_frame,text="Allowances", font=("Times",12,"bold"),
        width=380, height=90, bg="seashell",fg="red")
        allowance.place(x=10,y=80)

        lbl_medical = Label(allowance, text="Medical 10%", font=("Arial",10,"bold"), bg="seashell")
        lbl_medical.place(x=0,y=10)

        self.ent_medical = Entry(allowance, textvariable=self.medical, font=("Arial",10,"bold"),width=10)
        self.ent_medical.place(x=90,y=10)

        lbl_house = Label(allowance, text="House Rent 20%", font=("Arial",10,"bold"), bg="seashell")
        lbl_house.place(x=170,y=10)

        self.ent_house = Entry(allowance, textvariable=self.house, font=("Arial",10,"bold"),width=10)
        self.ent_house.place(x=290,y=10)

        lbl_conveyance = Label(allowance, text="Conveyance 15%", font=("Arial",10,"bold"), bg="seashell")
        lbl_conveyance.place(x=100,y=40)

        self.ent_conveyance = Entry(allowance, textvariable=self.conveyance, font=("Arial",10,"bold"),width=10)
        self.ent_conveyance.place(x=220,y=40)

        # Deduction Frame
        deduction = LabelFrame(pay_frame,text="Deduction", font=("Times",12,"bold"),
        width=380, height=100, bg="seashell",fg="red")
        deduction .place(x=10,y=170)


        lbl_tax = Label(deduction, text="Govt. Tax", font=("Arial",10,"bold"), bg="seashell")
        lbl_tax.place(x=0,y=10)

        ent_tax = Entry(deduction, textvariable=self.tax, font=("Arial",10,"bold"),width=15)
        ent_tax.place(x=70,y=10)


        radio_loan = Checkbutton(deduction,command=self.loan_check,onvalue=1,offvalue=0,
        variable = self.var2, text="Loan", font=("Arial",10,"bold"), bg="seashell")
        radio_loan.place(x=180,y=8)

        self.ent_loan = Entry(deduction, textvariable=self.loan, font=("Arial",10,"bold"),width=15)
        self.ent_loan.place(x=250,y=10)
        self.ent_loan.configure(state=DISABLED)
        self.ent_loan.bind("<Return>",self.loan_calculate)


        radio_addvance = Checkbutton(deduction,command=self.advance_check,onvalue=1,offvalue=0,
        variable=self.var1, text="Advance Salary", font=("Arial",10,"bold"), bg="seashell")
        radio_addvance.place(x=60,y=40)

        self.ent_addvance = Entry(deduction, textvariable=self.advance, font=("Arial",10,"bold"),width=15)
        self.ent_addvance.place(x=200,y=42)
        self.ent_addvance.configure(state=DISABLED)
        self.ent_addvance.bind("<Return>",self.advance_calculate)

        # Total Frame
        total = LabelFrame(pay_frame,text="Gross & Net Payment", font=("Times",12,"bold"),
        width=380, height=70, bg="seashell",fg="red")
        total .place(x=10,y=270)

        lbl_gross = Label(total, text="Gross Payment", font=("Arial",10,"bold"), bg="seashell")
        lbl_gross.place(x=0,y=10)

        ent_gross = Entry(total, textvariable=self.gross, font=("Arial",10,"bold"),width=10)
        ent_gross.place(x=110,y=10)

        lbl_net = Label(total, text="Net Payment", font=("Arial",10,"bold"), bg="seashell")
        lbl_net.place(x=190,y=10)

        ent_net = Entry(total, textvariable=self.net, font=("Arial",10,"bold"),width=10)
        ent_net.place(x=280,y=10)


    def calculate(self, event=""):
        if self.getloan.get() == "" or self.getadvance.get() == "":
            try:
                m = (int(float(self.basic.get()) * 0.1))
                h = (int(float(self.basic.get()) * 0.2))
                c = (int(float(self.basic.get()) * 0.15))
                t = (int(float(self.basic.get()) * 0.05))

                self.medical.set(m)
                self.house.set(h)
                self.conveyance.set(c)
                self.tax.set(t)
                total = (int(float(self.basic.get())) + int(float(self.medical.get())) + int(float(self.house.get())) + int(float(self.conveyance.get())))
                self.gross.set(total)
            except Exception as e:
                print(e)
        else:
            try:
                m = (int(float(self.basic.get()) * 0.1))
                h = (int(float(self.basic.get()) * 0.2))
                c = (int(float(self.basic.get()) * 0.15))
                t = (int(float(self.basic.get()) * 0.05))

                self.medical.set(m)
                self.house.set(h)
                self.conveyance.set(c)
                self.tax.set(t)
                total = (int(float(self.basic.get())) + int(float(self.medical.get())) + int(float(self.house.get())) + int(float(self.conveyance.get())+int(float(self.getadvance.get()))+int(float(self.getloan.get()))))
                self.gross.set(total)
            except Exception as e:
                pass

    def loan_calculate(self,event=""):
        l = (int(float(self.getloan.get()))-int(float(self.loan.get())))
        self.getloan.set(l)
    def advance_calculate(self,event=""):
        a = (int(float(self.getadvance.get()))-int(float(self.advance.get())))
        self.getadvance.set(a)

    def net_calculate(self):
        if self.month.get() == "Select Month":
            messagebox.showinfo("Info","Select Month")
        elif self.loan.get() == "" and self.advance.get() == "":
            deduction_total = (int(float(float(self.tax.get()))))
            net_total = (int(float(self.gross.get()) - deduction_total))
            self.net.set(net_total)
            self.salary_receipt()
        else:
            deduction_total = (int(float(float(self.tax.get())) + int(float(self.loan.get())) + int(float(self.advance.get()))))
            net_total = (int(float(self.gross.get()) - deduction_total))
            self.net.set(net_total)
            self.salary_receipt()

    def salary_receipt(self):
        if self.name.get() == "" or self.id.get() == "" or self.join.get() == "" or self.month.get() == "":
            messagebox.showerror("Error","Fill All The Fields")
            self.mm.deiconify()
        else:
            self.txt_receipt.delete("1.0",END)
            self.txt_receipt.insert(END, '\t\t    Employee Payroll Receipt \t\t\t' "\n")
            self.txt_receipt.insert(END, '-----------------------------------------------------------------------\t\t\t'+"\n")
            self.txt_receipt.insert(END, 'Staff ID:\t\t\t' + self.id.get() + "\n")
            self.txt_receipt.insert(END, 'Staff Name:\t\t\t' + self.name.get() + "\n")
            self.txt_receipt.insert(END, 'Staff Role:\t\t\t' + self.role.get() + "\n")
            self.txt_receipt.insert(END, 'Joining Date:\t\t\t' + self.join.get() + "\n")
            self.txt_receipt.insert(END, 'Account No:\t\t\t' + self.account.get() + "\n")
            self.txt_receipt.insert(END, 'Date:\t\t\t' + self.date.get() + "\n")
            self.txt_receipt.insert(END, 'Month:\t\t\t' + self.month.get() + "\n")
            self.txt_receipt.insert(END, '------------------------------------------------------------------------\t\t\t'+"\n")
            self.txt_receipt.insert(END, 'Loan :\t\t\t' + self.getloan.get()+ "\n")
            self.txt_receipt.insert(END, 'Advance Salary:\t\t\t' + self.getadvance.get() + "\n")
            self.txt_receipt.insert(END, '------------------------------------------------------------------------\t\t\t'+"\n")
            self.txt_receipt.insert(END, 'Medical Allowance:\t\t\t' + self.medical.get() + "\n")
            self.txt_receipt.insert(END, 'House Rent Allowance:\t\t\t' + self.house.get() + "\n")
            self.txt_receipt.insert(END, 'Conveyance Allowance:\t\t\t' + self.conveyance.get() + "\n")
            self.txt_receipt.insert(END, '------------------------------------------------------------------------\t\t\t'+"\n")
            self.txt_receipt.insert(END, 'Govt. tax:\t\t\t' + self.tax.get() + "\n")
            self.txt_receipt.insert(END, 'Loan Deduction:\t\t\t' + self.loan.get() + "\n")
            self.txt_receipt.insert(END, 'Advance Salary Deduction:\t\t\t' + self.advance.get() + "\n")
            self.txt_receipt.insert(END, '------------------------------------------------------------------------\t\t\t'+"\n")
            self.txt_receipt.insert(END, 'Gross Payment:\t\t\t' + self.gross.get() + "\n")
            self.txt_receipt.insert(END, 'Net Payment:\t\t\t' + self.net.get() + "\n")
            self.savereceipt = self.txt_receipt.get("1.0",END)
            f1 = open("Salary Receipt/"+str(self.receipt.get())+".txt","w")
            f1.write(self.savereceipt)
            f1.close()
            self.saveaspdf()
            if os.path.exists("Salary Receipt/"+str(self.receipt.get())+".txt"):
                os.remove("Salary Receipt/"+str(self.receipt.get())+".txt")
            else:
                print("The file does not exist")

    def view_all(self):
        self.btn_view_all.configure(state = DISABLED)
        self.record_frame =Frame(self.mm,width=404, height=473, bg="#ffffcc")
        self.record_frame.place(x=405,y=50)
        # Search Frame
        search_pay = LabelFrame(self.record_frame, text="Search Record", font=("Times",12,"bold"),
        width=403, height=60, bg="seashell")
        search_pay.place(x=0,y=0)

        combo_search_by = ttk.Combobox(search_pay, state="readonly", font=("Times",12,"bold"),
        textvariable=self.search_by2)
        combo_search_by["values"] = ("Search By","ID","Staff_Name","CNIC","Phone")
        combo_search_by.current("0")
        combo_search_by.place(x=10,y=5)

        ent_search2 = Entry(search_pay, textvariable=self.search2, font=("Times",12,"bold"))
        ent_search2.place(x=200, y=5)
        ent_search2.bind("<Return>",self.search_payroll)

        # Treeview Frame
        self.tv_frame = LabelFrame(self.record_frame, text="Payroll Record", font=("Times",12,"bold"),
        width=403, height=410, bg="seashell")
        self.tv_frame.place(x=0,y=61,height=410,width=403)

        scroll_x = ttk.Scrollbar(self.tv_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.tv_frame,orient=VERTICAL)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",background="lightyellow",forebackground="lightyellow",
                            fieldbackground="lightyellow")

        style.map("Treeview",background=[('selected','#074463')])
        self.tv = ttk.Treeview(self.tv_frame,columns=("Receipt","ID","Name","R","J","A","D","Month","B","M","H","C","T","L","Advance","G","N","getloan","getadvance"),
                                      xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.tv.xview)
        scroll_y.config(command=self.tv.yview)
        self.tv.heading("Receipt",text="Receipt_No")
        self.tv.heading("ID",text="ID")
        self.tv.heading("Name",text="Name")
        self.tv.heading("R",text="Role")
        self.tv.heading("J",text="Joining Date")
        self.tv.heading("A",text="Account No")
        self.tv.heading("D",text="Date")
        self.tv.heading("Month",text="Basic")
        self.tv.heading("B",text="Month")
        self.tv.heading("M",text="Medical")
        self.tv.heading("H",text="House")
        self.tv.heading("C",text="Conveyance")
        self.tv.heading("T",text="Tax")
        self.tv.heading("L",text="Loan")
        self.tv.heading("Advance",text="Advance")
        self.tv.heading("G",text="Gross")
        self.tv.heading("N",text="Net")
        self.tv.heading("getloan",text="Loan Get")
        self.tv.heading("getadvance",text="Advance Salary")
        self.tv["show"]= "headings"
        self.tv.pack(fill=BOTH,expand=1)
        self.tv.bind("<ButtonRelease>",self.get_cursor)
        self.show_data()

    def createfolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print("Error: Creating directory. "+ directory)
    createfolder("./Salary Receipt/")


    def saveaspdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", size=14)
        f = open("Salary Receipt/"+str(self.receipt.get())+".txt","r")
        for x in f:
            pdf.cell(200, 10, txt=x, ln=1)
        pdf.output("Salary Receipt/"+str(self.receipt.get())+".pdf")

    def back(self):
        self.btn_view_all.configure(state="normal")
        self.record_frame.destroy()

    def advance_check(self):
        if self.var1.get() == 0:
            self.ent_addvance.delete(0,END)
            self.ent_addvance.configure(state = DISABLED)
        else:
            self.ent_addvance.configure(state = "normal")
            self.ent_addvance.delete(0,END)

    def loan_check(self):
        if self.var2.get() == 0:
            self.ent_loan.delete(0,END)
            self.ent_loan.configure(state = DISABLED)
        else:
            self.ent_loan.configure(state = "normal")
            self.ent_loan.delete(0,END)
    
    def reset(self):
        try:
            self.basic.set("")
            self.medical.set("")
            self.house.set("")
            self.conveyance.set("")
            self.gross.set("")
            self.tax.set("")
            self.loan.set("")
            self.advance.set("")
            self.net.set("")
            self.date.set("")
            self.month.set("Month")
            self.date.set("")
            self.id.set("")
            self.name.set("")
            self.account.set("")
            self.join.set("")
            self.role.set("")
            self.receipt.set("")
            self.txt_receipt.delete("1.0",END)
            self.today = date.today()
            self.date.set(self.today)
            self.back()
        except Exception as e:
            pass

    def search_staff(self,event=""):
        try:
            conn =mysql.connector.connect(host="localhost", user = "root", password = "12345", database = "sms")
            cursor = conn.cursor()
            cursor.execute("select * from staff_registration where "+str(self.search_by.get())+" LIKE '%"+str(self.search.get())+"%'")
            data = cursor.fetchone()
            if len(data)!=0:
                print(data[1])
                self.id.set(data[0])
                self.name.set(data[1])
                self.role.set(data[2])
                self.join.set(data[4])
                self.account.set(data[10])
                conn.commit()
            else:
                messagebox.showinfo("Info","Staff Record Not Found")
                self.mm.deiconify()
            conn.close()

        except Exception as e:
            messagebox.showerror("Error",f"Due To: {e}")
            self.mm.deiconify()

    def save(self):
        try:
            conn =mysql.connector.connect(host="localhost", user = "root", password = "12345", database = "sms")
            cursor = conn.cursor()
            cursor.execute("select exists (select * from payroll where ID LIKE '%"+str(self.id.get())+"%'"+" and "+" Month LIKE '%"+str(self.month.get())+"%')")
            data = cursor.fetchone()
            if (data[0]) == 1:
                messagebox.showinfo("Info",f"Month {self.month.get()} Record Already Exist")
                self.mm.deiconify()
            else:
                conn =mysql.connector.connect(host="localhost", user = "root", password = "M@ateen0786", database = "sms")
                cursor = conn.cursor()
                cursor.execute("insert into payroll (ID,Staff_Name,Role,Joinig_Date,Account_No,Cur_Date,Basic,Month,Medical,House,Conveyance,Tax,Loan,Add_Salary,Gross,Net,getloan,getadvance) values(%s ,%s ,%s ,%s ,%s ,%s, %s, %s, %s,%s ,%s ,%s ,%s, %s, %s, %s, %s, %s)",(
                                                                                                                        self.id.get(),
                                                                                                                        self.name.get(),
                                                                                                                        self.role.get(),
                                                                                                                        self.join.get(),
                                                                                                                        self.account.get(),
                                                                                                                        self.date.get(),
                                                                                                                        self.basic.get(),
                                                                                                                        self.month.get(),
                                                                                                                        self.medical.get(),
                                                                                                                        self.house.get(),
                                                                                                                        self.conveyance.get(),
                                                                                                                        self.tax.get(),
                                                                                                                        self.loan.get(),
                                                                                                                        self.advance.get(),
                                                                                                                        self.gross.get(),
                                                                                                                        self.net.get(),
                                                                                                                        self.getloan.get(),
                                                                                                                        self.getadvance.get(),
                ))
                conn.commit()
                self.salary_receipt()
                conn.close()
                messagebox.showinfo("Success", f"Reocrd added successfully")
                self.mm.deiconify()
        except Exception as e:
            messagebox.showerror("Error",f"Due To {e}")
            self.mm.deiconify()

    def update(self):
        try:
            update=messagebox.askyesno("Update","Are You Sure Update this Student data",parent=self.mm)
            if update>0:
                conn =mysql.connector.connect(host="localhost", user = "root", password = "12345", database = "sms")
                cursor = conn.cursor()
                cursor.execute("update payroll set ID=%s,Staff_Name=%s,Role=%s,Joinig_Date=%s,Account_No=%s,Cur_Date=%s,Basic=%s,Month=%s,Medical=%s,\
                    House=%s,Conveyance=%s,Tax=%s,Loan=%s,Add_Salary=%s,Gross=%s,Net=%s,getloan=%s,getadvance=%s where Receipt_no=%s",(
                                                                                            self.id.get(),
                                                                                            self.name.get(),
                                                                                            self.role.get(),
                                                                                            self.join.get(),
                                                                                            self.account.get(),
                                                                                            self.date.get(),
                                                                                            self.basic.get(),
                                                                                            self.month.get(),
                                                                                            self.medical.get(),
                                                                                            self.house.get(),
                                                                                            self.conveyance.get(),
                                                                                            self.tax.get(),
                                                                                            self.loan.get(),
                                                                                            self.advance.get(),
                                                                                            self.gross.get(),
                                                                                            self.net.get(),
                                                                                            self.getloan.get(),
                                                                                            self.getadvance.get(),
                                                                                            self.receipt.get(),

                                                                                            
                                                                                            
                ))
                conn.commit()
                messagebox.showinfo("Info","Record Updated Successfully")
                self.show_data()
            else:
                if not update:
                    return
        except Exception as e:
            messagebox.showinfo("Info",f"Due to {e}")

    def show_data(self):
        conn =mysql.connector.connect(host="localhost", user = "root", password = "12345", database = "sms")
        cursor = conn.cursor()
        cursor.execute("select * from payroll")
        data = cursor.fetchall()
        if len(data)!=0:
            self.tv.delete(*self.tv.get_children())
            for i in data:
                self.tv.insert("",END,values=i)
                conn.commit()
            conn.close()

    def search_payroll(self,event=""):
        if self.search_by2.get() == "Search By":
            messagebox.showerror("Error","Select Search By")
        else:
            try:
                conn =mysql.connector.connect(host="localhost", user = "root", password = "12345", database = "sms")
                cursor = conn.cursor()
                cursor.execute("select * from payroll where "+str(self.search_by2.get())+" LIKE '%"+str(self.search2.get())+"%'")
                data = cursor.fetchall()
                if len(data)!=0:
                    self.tv.delete(*self.tv.get_children())
                for i in data:
                    self.tv.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as e:
                pass

    def get_cursor(self,event=""):
        try:
            row_1 = self.tv.focus()
            content = self.tv.item(row_1)
            data = content["values"]
            self.receipt.set(data[0])
            self.id.set(data[1])
            self.name.set(data[2])
            self.role.set(data[3])
            self.join.set(data[4])
            self.account.set(data[5])
            self.date.set(data[6])
            self.month.set(data[8])
            self.basic.set(data[7])
            self.medical.set(data[9])
            self.house.set(data[10])
            self.conveyance.set(data[11])
            self.tax.set(data[12])
            self.loan.set(data[13])
            self.advance.set(data[14])
            self.gross.set(data[15])
            self.net.set(data[16])
            self.getloan.set(data[17])
            self.getadvance.set(data[18])
        except Exception as e:
            print(e)

    def exit(self):
        self.mm.destroy()

if __name__ == "__main__":
    mm = Tk()
    obj = FrontEnd(mm)
    mm.mainloop()
