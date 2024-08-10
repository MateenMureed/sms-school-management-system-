# Imprting Tkinter and its Libraries
from tkinter import *
import time
from PIL import Image,ImageTk

# importing Modules
#from staff import staff_registration
#from student import Backend
#from pros import prospectus
#from fee import fee_functions
#from payroll import FrontEnd

#Abstract Class
from abc import ABC, abstractmethod


class lobby_class(ABC):

    def __init__(self,mm):
        self.mm = mm
        self.mm.geometry('1010x690+0+0')
        self.mm.title("Main Lobby")
        #self.mm.resizable('false', 'false')
        self.mm.configure(bg="black")

        # ============= Title ===============
        title = Label(self.mm,width=38,text="SCHOOL MANAGEMENT SYSTEM",relief=RAISED,bg="seashell",
        font=("Times",27,"bold"),bd=6).place(x=200,y=0)

        # ========= Main Page Image ===========
        self.img = Image.open(r"image\2nd.jpg")
        new = self.img.resize((804,450),Image.ANTIALIAS)
        self.img =ImageTk.PhotoImage(new)
        self.img_lbl = Label(self.mm, image=self.img,compound=TOP,width=804,height=450,bg="white")
        self.img_lbl.place(x=200, y=235)

        # Clock Frame
        clock_frame = LabelFrame(self.mm,text="Clock Frame",font=("Times",12,"bold"),relief=RAISED,
        bd=2,bg="lightyellow",width=810,height=180).place(x=200,y=55)
        
        self.lbl_h = Label(clock_frame,text="12",bg="#087587",fg="white",
        font=("Times",40,"bold"),width=150,height=90)
        self.lbl_h.place(x=280,y=77,width=150,height=90)

        self.lbl_h2 = Label(clock_frame,text="HOURS",bg="lightyellow",
        font=("Times",25,"bold"),width=150,height=40)
        self.lbl_h2.place(x=280,y=177,width=150,height=40)


        self.lbl_m = Label(clock_frame,text="12",bg="#3333ff",fg="white",
        font=("Times",40,"bold"),width=150,height=90)
        self.lbl_m.place(x=440,y=77,width=150,height=90)

        self.lbl_m2 = Label(clock_frame,text="MINUTE",bg="lightyellow",
        font=("Times",25,"bold"),width=150,height=40)
        self.lbl_m2.place(x=440,y=177,width=150,height=40)

        self.lbl_s = Label(clock_frame,text="12",fg="white",bg="#ff0450",
        font=("Times",40,"bold"),width=150,height=90)
        self.lbl_s.place(x=620,y=77,width=150,height=90)

        lbl_s2 = Label(clock_frame,text="SECOND",bg="lightyellow",
        font=("Times",25,"bold"),width=150,height=40)
        lbl_s2.place(x=620,y=177,width=150,height=40)


        self.lbl_noon = Label(clock_frame,text="AM",bg="#ff0000",fg="white",
        font=("Times",40,"bold"),width=150,height=90)
        self.lbl_noon.place(x=800,y=77,width=150,height=90)

        lbl_noon = Label(clock_frame,text="NOON",bg="lightyellow",
        font=("Times",25,"bold"),width=150,height=40).place(x=800,y=177,width=150,height=40)


        # Left Frame
        left_frame =Frame(self.mm,width=200,height=690,relief=RAISED,bg="#00FFFF",bd=2)
        left_frame.place(x=0, y=0)

        # ========= Logo Image ===============
        self.logo = Image.open(r"image\logo.png")
        n = self.logo.resize((192,100),Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(n)
        self.btn_logo = Label(left_frame,image=self.logo,bg="#00FFFF",
        bd=2,width=192,font=('times',18,'bold'),height=120)
        self.btn_logo.place(x=0, y=0)

        #============ Left Frame Buttons =========
        
        #============= Prospectus Button Image ==========
        self.img_course = ImageTk.PhotoImage(file=r"image\courses.png")
        self.btn_course = Button(left_frame, text="Prospectus",width=180,image=self.img_course,bg="#00FFFF",command=self.prospectus_window,
        compound="top",borderwidth=2,font=('times new roman', 18, 'bold'),relief=RIDGE)
        self.btn_course.place(x=3, y=122, height=85)

        #============ Student Registation Button Image ========
        self.img_reg = ImageTk.PhotoImage(file=r"image\r.png")
        self.btn_registration = Button(left_frame,text="Student\nRegistration",width=180,bg="#00FFFF",command=self.student,
        image=self.img_reg,compound="right",borderwidth=2,font=('times',18,'bold'),height=70,relief=RIDGE)
        self.btn_registration.place(x=3, y=212)

        # =========== Staff Registration Button Image
        self.img_staff = ImageTk.PhotoImage(file=r"image\staff.png")
        self.btn_staff = Button(left_frame,text="Staff\nRegistration",command=self.staff_btn,image=self.img_staff,compound="right",bg="#00FFFF",
        borderwidth=2,relief=RIDGE,width=180,font=('times new roman', 18, 'bold'),height=70)
        self.btn_staff.place(x=3, y=295)

        # =========== fee Button Image
        self.img_fee = ImageTk.PhotoImage(file=r"image\f.png")
        self.btn_fee = Button(left_frame,text="Fee\nRegistration",command=self.fee_record,image=self.img_fee,compound="right",bg="#00FFFF",
        borderwidth=2,relief=RIDGE,width=180,font=('times new roman', 18, 'bold'),height=70)
        self.btn_fee.place(x=3, y=378)

        # =========== payroll Button Image
        self.img_pay = ImageTk.PhotoImage(file=r"image\pay.png")
        self.btn_pay = Button(left_frame,text="Payroll\nManagement", command=self.pay_window, image=self.img_pay,compound="right",bg="#00FFFF",
        borderwidth=2,relief=RIDGE,width=180,font=('times new roman', 18, 'bold'),height=70)
        self.btn_pay.place(x=3, y=462)


        # =========== Exit Button Image
        self.img_exit = ImageTk.PhotoImage(file=r"image\exit.png")
        self.btn_exit = Button(left_frame,command=self.exit,image=self.img_exit,bd=0,relief=RIDGE,
        bg="#00FFFF", text="Exit", font=("Times",18,"bold"), compound="top",borderwidth=2, width=180, height=100)
        self.btn_exit.place(x=3, y=550)
        self.clock()

    def clock(self):
        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
        self.s = str(time.strftime("%S"))

        if int(self.h)>12 and int(self.m)>0:
            self.lbl_noon.config(text="PM")

        if int(self.h)>12:
            self.h =str((int(self.h)-12))

        self.lbl_h.config(text=self.h)
        self.lbl_m.config(text=self.m)
        self.lbl_s.config(text=self.s)
        self.lbl_h.after(200,self.clock)

    def student(self):
        pass
    def staff_btn(self):
        pass
    def fee_record(self):
        pass
    def prospectus_window(self):
        pass
    def search_window(self):
        pass
    def exit(self):
        self.mm.destroy()

class import_class(lobby_class):
    def pay_window(self):
        self.new_window = Toplevel(self.mm)
        self.a = FrontEnd(self.new_window)
    def student(self):
        self.new_window = Toplevel(self.mm)
        self.app = Backend(self.new_window) 
    def staff_btn(self):
        self.new_window = Toplevel(self.mm)
        self.app = staff_registration(self.new_window)
    def fee_record(self):
        self.new_window = Toplevel(self.mm)
        self.app = fee_functions(self.new_window)
    def prospectus_window(self):
        self.new_window = Toplevel(self.mm)
        self.app = prospectus(self.new_window)


if __name__ == '__main__':
    mm = Tk()
    obj = import_class(mm)
    mm.mainloop()
