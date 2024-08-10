from tkinter import *
from tkinter import Tk
from tkinter import ttk
from ttkthemes import themed_tk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import filedialog
import os
#import docx
#from docx.shared import Pt
#from docx.shared import Inches

class staff_registration:
    def __init__(self,mm):
        self.mm = mm
        self.mm.geometry('810x603+200+85')
        self.mm.title("Fee Management GUI")
        self.mm.resizable('false', 'false')
        self.mm.configure(bg="black")
        self.mm.deiconify()

        # String Variables for Database
        self.id = StringVar()
        self.sname = StringVar()
        self.sgender = StringVar()
        self.sdob = StringVar()
        self.semail = StringVar()
        self.scnic = StringVar()
        self.srole = StringVar()
        self.saddress = StringVar()
        self.join = StringVar()
        self.image = StringVar()
        self.phone = StringVar()
        self.account = StringVar()

        #String Variables For Search Frame
        self.search_by = StringVar()
        self.search_info = StringVar()
        self.saveas = StringVar()

        # ======= Title========
        self.title = Label(self.mm,width=38,text="STAFF REGISTRATION FORM",relief=RAISED,bg="#FFF0F5",
        font=("Times",27,"bold"),bd=6).pack(fill=X)

        # ======= Main Frame ========
        self.main = Frame(self.mm, width=810, height=547, relief=RAISED, bd=2, bg="seashell3")
        self.main.place(x=0, y=54)

        # ======= Staff Information Label Frame =======
        self.s = LabelFrame(self.main,text="Staff Information",relief=RAISED,bd=2,bg="#00ffff",
        width=260,height=543,font=("times",14,"bold"))
        self.s.place(x=0,y=0)

        # Image Logo

        self.image_frame = Frame(self.s,width=185,height=100)
        self.image_frame.place(x=30,y=0)

        self.img_logo = Image.open(r"image\s.png")
        new_pic = self.img_logo.resize((185,100),Image.ANTIALIAS)
        self.img_logo =ImageTk.PhotoImage(new_pic)
        self.img = Label(self.image_frame, image=self.img_logo,compound=TOP,width=185,height=100,bg="#00ffff")
        self.img.place(x=0, y=0)

        #self.img_data = ImageTk.PhotoImage(file=r"image\s.png")
        #self.btn_data = Label(self.s,image=self.img_data,width=150,height=100,bg="#00ffff")
        #self.btn_data.place(x=20, y=0)

        # ======== Labels For Registration =========
        lbl_id = Label(self.s,text="Staff ID",
        bg="#00ffff",font=("arial",10,"bold")).place(x=0,y=120)

        lbl_name = Label(self.s,text="Staff Name",
        bg="#00ffff",font=("arial",10,"bold")).place(x=0,y=150)

        lbl_role = Label(self.s,text="Staff Role",
        bg="#00ffff",font=("arial",10,"bold")).place(x=0,y=180)

        lbl_dob = Label(self.s,text="Staff D.O.B",
        bg="#00ffff",font=("arial",10,"bold")).place(x=0,y=210)

        lbl_gender = Label(self.s,text="Staff Gender",
        bg="#00ffff",font=("arial",10,"bold")).place(x=0,y=240)

        lbl_email = Label(self.s,text="Staff Email",
        bg="#00ffff",font=("arial",10,"bold")).place(x=0,y=270)

        lbl_cnic = Label(self.s,text="Staff CNIC",
        bg="#00ffff",font=("arial",10,"bold")).place(x=0,y=300)

        lbl_address = Label(self.s,text="Staff Address",
        bg="#00ffff",font=("arial",10,"bold")).place(x=0,y=330)

        lbl_joining= Label(self.s,text="Joining Date",
        bg="#00ffff",font=("arial",10,"bold")).place(x=0,y=360)

        lbl_account= Label(self.s,text="Account No",
        bg="#00ffff",font=("arial",10,"bold")).place(x=0,y=390)

        lbl_phone = Label(self.s,text="Phone No",
        bg="#00ffff",font=("arial",10,"bold")).place(x=0,y=420)
        
        lbl_img = Label(self.s,text="Upload Image",
        bg="#00ffff",font=("arial",10,"bold")).place(x=0,y=462)

        # ======== Entries For Registration =========
        id = Entry(self.s,textvariable=self.id,
        bg="#FFF0F5",font=("arial",10,"bold")).place(x=100,y=120)

        name = Entry(self.s,textvariable=self.sname,
        bg="#FFF0F5",font=("arial",10,"bold")).place(x=100,y=150)

        role = Entry(self.s,textvariable=self.srole,
        bg="#FFF0F5",font=("arial",10,"bold")).place(x=100,y=180)

        dob = Entry(self.s,textvariable=self.sdob,
        bg="#FFF0F5",font=("arial",10,"bold")).place(x=100,y=210)

        gender = Entry(self.s,textvariable=self.sgender,
        bg="#FFF0F5",font=("arial",10,"bold")).place(x=100,y=240)

        email = Entry(self.s,textvariable=self.semail,
        bg="#FFF0F5",font=("arial",10,"bold")).place(x=100,y=270)

        cnic = Entry(self.s,textvariable=self.scnic,
        bg="#FFF0F5",font=("arial",10,"bold")).place(x=100,y=300)

        address = Entry(self.s,textvariable=self.saddress,
        bg="#FFF0F5",font=("arial",10,"bold")).place(x=100,y=330)

        joining = Entry(self.s,textvariable=self.join,
        bg="#FFF0F5",font=("arial",10,"bold")).place(x=100,y=358)

        ent_account = Entry(self.s,textvariable=self.account,
        bg="#FFF0F5",font=("arial",10,"bold")).place(x=100,y=388)

        ent_phone = Entry(self.s,textvariable=self.phone,
        bg="#FFF0F5",font=("arial",10,"bold")).place(x=100,y=418)

        # ======== Button for Image Upload
        image_upload= Button(self.s,width=19,command=self.uploadimage,
        text="Upload Image",bg="#00ffbf",font=("arial",8,"bold")).place(x=100,y=460)
        self.m = Entry(self.s,textvariable=self.image,width=34,bg="#00ffff",font=("arial",10,"bold"))
        self.m.place(x=0,y=490)
        
        
        #======= Search Frame =====
        self.search = LabelFrame(self.main,text="Search Staff Information",relief=RAISED,bd=2,bg="#F5F5DC",
        width=545,height=80,font=("times",14,"bold"))
        self.search.place(x=260,y=0)

        # Label and Entry Boxes For Search Box
        lbl_searchby = Label(self.search,text="Search By",
        bg="#F5F5DC",font=("times",14,"bold")).place(x=0,y=10)
        
        combo = ttk.Combobox(self.search,state="readonly",width=12,textvariable=self.search_by,
        font=("arial",10,"bold"))
        combo["value"]=("Search By","ID","Staff_Name","CNIC","Email")
        combo.current(0)
        combo.place(x=100,y=15)

        search_entry = Entry(self.search,text="Staff CNIC",textvariable=self.search_info,width=12,
        bg="#F5F5DC",font=("arial",13,"bold")).place(x=220,y=15)

        Search_btn= Button(self.search,width=10,bd=2,relief=GROOVE,command=self.search_data,
        text="Search",bg="#F5F5DC",font=("times",11,"bold")).place(x=340,y=10)

        View_all_btn= Button(self.search,width=10,bd=2,relief=GROOVE,command=self.show,
        text="View All",bg="#F5F5DC",font=("times",11,"bold")).place(x=440,y=10)

        
        #======= TreeView Frame =====
        treeview_frame = LabelFrame(self.main,text="Search Details",relief=RAISED,bd=2,bg="#00ffff",
        width=545,height=390,font=("times",14,"bold"))
        treeview_frame.place(x=260,y=80,width=545,height=390)

        scroll_x = ttk.Scrollbar(treeview_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(treeview_frame,orient=VERTICAL)

        # Styling treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",background="#F0E68C",forebackground="yellow",
                            fieldbackground="#F0E68C")
        style.map("Treeview",background=[('selected','#074463')])

        # TreeView Setting
        self.std_table = ttk.Treeview(treeview_frame,columns=("ID","N","R","D","J","G","E","C","A","AC","P","I"),
        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        # Scroll Bar Setting
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.std_table.xview)
        scroll_y.config(command=self.std_table.yview)

        
        # TreeView Labels Heading
        self.std_table.heading("ID",text="ID")
        self.std_table.heading("N",text="Name")
        self.std_table.heading("R",text="Role")
        self.std_table.heading("D",text="D.O.B")
        self.std_table.heading("J",text="Joinig Date")
        self.std_table.heading("G",text="Gender")
        self.std_table.heading("E",text="Email")
        self.std_table.heading("C",text="CNIC")
        self.std_table.heading("A",text="Address")
        self.std_table.heading("AC",text="Account")
        self.std_table.heading("P",text="Phone No")
        self.std_table.heading("I",text="Image")

        self.std_table["show"]= "headings"
        self.std_table.pack(fill=BOTH,expand=1)
        self.show()
        self.std_table.bind("<ButtonRelease>",self.get_cursor)

        # ======= Buttons Label Frame =======
        self.b_frame = LabelFrame(self.main,text="Buttons",relief=RAISED,bd=2,bg="#00ffbf",
        width=806,height=72,font=("times",14,"bold"))
        self.b_frame.place(x=260,y=470)

        # ========= Buttons ==========
        submit= Button(self.b_frame,width=9,bd=2,relief=GROOVE,command=self.save,
        text="Submit",bg="#00ffff",font=("times",11,"bold")).place(x=0,y=5)

        update= Button(self.b_frame,width=9,bd=2,relief=GROOVE,command=self.update,
        text="Update",bg="#00ffff",font=("times",11,"bold")).place(x=90,y=5)

        Delete= Button(self.b_frame,width=9,bd=2,relief=GROOVE,command=self.delete,
        text="Delete",bg="#00ffff",font=("times",11,"bold")).place(x=180,y=5)
        
        Clear= Button(self.b_frame,width=9,bd=2,relief=GROOVE,command=self.clear,
        text="Clear",bg="#00ffff",font=("times",11,"bold")).place(x=270,y=5)

        saveword= Button(self.b_frame,width=9,bd=2,relief=GROOVE,command=self.word,
        text="Word",bg="#00ffff",font=("times",11,"bold")).place(x=360,y=5)

        close_window= Button(self.b_frame,width=9,bd=2,relief=GROOVE,command=self.exit,
        text="Exit",bg="#00ffff",font=("times",11,"bold")).place(x=450,y=5)

    def uploadimage(self):
        self.image.set("")
        FilePath = filedialog.askopenfilename(initialdir=os.getcwd(),title="open images",
        filetype=(("JPG File","*.jpg"),("PNG File","*.png"),("All Files","*.*")))
        self.mm.deiconify()
        self.m.insert(0, FilePath)
        self.i = Image.open(FilePath)
        new_pic = self.i.resize((185,100),Image.ANTIALIAS)
        self.i =ImageTk.PhotoImage(new_pic)
        self.img_lbl = Label(self.image_frame, image=self.i,compound=TOP,width=190,height=100,bg="white")
        self.img_lbl.place(x=0, y=0)

    def save(self):
        if self.sname.get() == "" or self.sgender.get() == "" or self.image.get() == "":
            messagebox.showerror("Error","All fields are required")
            self.mm.deiconify()
        else:
            try:
                conn =mysql.connector.connect(host="localhost", user = "root", password = "12345", database = "sms")
                cursor = conn.cursor()
                cursor.execute("insert into staff_registration values(%s ,%s ,%s ,%s ,%s, %s, %s ,%s ,%s,%s,%s,%s)",(
                                                                                                self.id.get(),
                                                                                                self.sname.get(),
                                                                                                self.srole.get(),
                                                                                                self.sdob.get(),
                                                                                                self.join.get(),
                                                                                                self.sgender.get(),
                                                                                                self.semail.get(),
                                                                                                self.scnic.get(),
                                                                                                self.saddress.get(),
                                                                                                self.image.get(),
                                                                                                self.account.get(),
                                                                                                self.phone.get()
                ))
                conn.commit()
                self.show()
                self.clear()
                conn.close()
                messagebox.showinfo("Success", f"Staff Has been added",parent=self.mm)
            except Exception as e:
                messagebox.showerror("Error", f"Due To:{e}",parent=self.mm)
    
    def show(self):
        conn =mysql.connector.connect(host="localhost", user = "root", password = "12345", database = "sms")
        cursor = conn.cursor()
        cursor.execute("select * from staff_registration")
        data = cursor.fetchall()
        if len(data)!=0:
            self.std_table.delete(*self.std_table.get_children())
            for i in data:
                self.std_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    def get_cursor(self,event=""):
        try:
            row = self.std_table.focus()
            content = self.std_table.item(row)
            data = content["values"]
            self.id.set(data[0])
            self.sname.set(data[1])
            self.srole.set(data[2])
            self.sdob.set(data[3])
            self.join.set(data[4])
            self.sgender.set(data[5])
            self.semail.set(data[6])
            self.saddress.set(data[8])
            self.scnic.set(data[7])
            self.image.set(data[9])
            self.account.set(data[10])
            self.phone.set(data[11])
            a = self.image.get()
            self.i = Image.open(a)
            new_pic = self.i.resize((185,100),Image.ANTIALIAS)
            self.i =ImageTk.PhotoImage(new_pic)
            self.img_lbl = Label(self.image_frame, image=self.i,compound=TOP,width=185,height=100,bg="white")
            self.img_lbl.place(x=0, y=0)
        except Exception as e:
            pass

    def update(self):
        if self.sname.get() == "" or self.sgender.get() == "" or self.image.get() == "":
            messagebox.showerror("Error","All fields are required")
            self.mm.deiconify()
        else:
            try:
                update=messagebox.askyesno("Update","Are You Sure Update this Student data",parent=self.mm)
                if update>0:
                    conn =mysql.connector.connect(host="localhost", user = "root", password = "12345", database = "sms")
                    cursor = conn.cursor()
                    cursor.execute("update staff_registration set Staff_Name=%s,Role=%s,DOB=%s,Joinig_Date=%s,Gender=%s,Email=%s,Address=%s,Image=%s,CNIC=%s,Account_No=%s,Phone=%s where ID=%s ",(   
                                                                                                                                                                    self.sname.get(),   
                                                                                                                                                                    self.srole.get(),
                                                                                                                                                                    self.sdob.get(),
                                                                                                                                                                    self.join.get(),
                                                                                                                                                                    self.sgender.get(),
                                                                                                                                                                    self.semail.get(),
                                                                                                                                                                    self.saddress.get(),
                                                                                                                                                                    self.image.get(),
                                                                                                                                                                    self.scnic.get(),
                                                                                                                                                                    self.account.get(),
                                                                                                                                                                    self.phone.get(),
                                                                                                                                                                    self.id.get(),
                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.show()
                self.clear()
                conn.close()

                messagebox.showinfo("Success",f"Staff {self.sname.get()} Successfully Updated",parent=self.mm)
            except Exception as e:
                messagebox.showerror("Error", f"Due To:{e}",parent=self.mm)
    
    def delete(self):
        if self.sname.get() == "" or self.sgender.get() == "" or self.image.get() == "":
            messagebox.showerror("Error","All fields are required")
            self.mm.deiconify()
        else:
            try:
                delete=messagebox.askyesno("Update","Are You Sure Delete this Student Record",parent=self.mm)
                if delete>0:
                    conn =mysql.connector.connect(host="localhost", user = "root", password = "12345", database = "sms")
                    cursor = conn.cursor()
                    query=("delete from staff_registration where ID=%s")
                    value=(self.id.get(),)
                    cursor.execute(query,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.show()
                self.clear()
                conn.close()

                messagebox.showinfo("Success","Student Successfully Deleted",parent=self.mm)
            except Exception as e:
                messagebox.showerror("Error", f"Due To:{e}",parent=self.mm)

    def search_data(self):
        if self.search_info.get == "":
            messagebox.showerror("Error","Please Select Option")
            self.mm.deiconify()
        else:
            try:
                conn =mysql.connector.connect(host="localhost", user = "root", password = "12345", database = "sms")
                cursor = conn.cursor()
                cursor.execute("select * from staff_registration where "+str(self.search_by.get())+" LIKE '%"+str(self.search_info.get())+"%'")
                data = cursor.fetchall()
                if len(data)!=0:
                    self.std_table.delete(*self.std_table.get_children())
                    for i in data:
                        self.std_table.insert("",END,values=i)
                        conn.commit()
                        
                else:
                    messagebox.showerror("Error","Student Not Found")
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Due To:{e}",parent=self.mm)
        
    def clear(self):
        self.sname.set("")
        self.semail.set("")
        self.scnic.set("")
        self.sdob.set("")
        self.sgender.set("")
        self.srole.set("")
        self.saddress.set("")
        self.join.set("")
        self.image.set("")
        self.id.set("")
        self.account.set("")
        self.phone.set("")
        self.img_lbl.config(image = self.img_logo,bg="cyan")

    def word(self):
        doc = docx.Document()
        doc.add_paragraph()
        doc.add_heading("Student Registration Form",0)
        doc.add_picture(self.image.get(),width=docx.shared.Inches(2),height=docx.shared.Inches(2))
        doc.add_paragraph("Staff Name :-  "+self.sname.get())
        doc.add_paragraph("Staff Roll                    :-  "+self.srole.get())
        doc.add_paragraph("Staff Joining Date       :-  "+self.join.get())
        doc.add_paragraph("Staff DOB                 :-  "+self.sdob.get())
        doc.add_paragraph("Staff Gender    :-  "+self.sgender.get())
        doc.add_paragraph("Staff Email         :-  "+self.semail.get())
        doc.add_paragraph("Staff CNIC         :-  "+self.scnic.get())
        doc.add_paragraph("Staff Address        :-  "+self.saddress.get())

        doc.save("Staff Data\{}.docx".format(self.sname.get()))
        messagebox.showinfo("Success","Data Has Been Saved in Word File")
    
    def createfolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print("Error: Creating directory. "+ directory)
    createfolder("./Staff Data/")

    def exit(self):
        self.mm.destroy()
        

if __name__ == '__main__':
    mm = Tk()
    obj = staff_registration(mm)
    mm.mainloop()
