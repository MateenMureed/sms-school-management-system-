from tkinter import *
import mysql.connector
from tkinter import messagebox
from singup import login_singup
from PIL import ImageTk
from MainPage import import_class

class hello:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1024x600+0+0')
        self.root.title("User Login")
        self.root.resizable('false', 'false')

        # =================================== first frame ================================================
        self.fram_side = Frame(self.root, width=350, height=900, bg="#00FFFF")
        self.fram_side.place(x=0, y=0)
        # ===================================== second frame =============================================
        self.sub_left_fram = Frame(self.root, width=200, height=500, relief=RAISED, bd=1, bg="#00FFFF")
        self.sub_left_fram.place(x=150, y=50)

        self.pic = ImageTk.PhotoImage(file="images\logo.png")
        self.pic_lbl = Label(self.sub_left_fram, image=self.pic, bd=0, bg="#00FFFF")
        self.pic_lbl.place(x=0, y=0)

        # ====================================== third frame ====================================
        self.main_frame = Frame(self.root, width=800, height=500, relief=RAISED, bd=1, bg="white")
        self.main_frame.place(x=350, y=50)

        self.login_logo_pic = ImageTk.PhotoImage(file="images\login4.jfif")
        self.login_lbl = Label(self.main_frame, image=self.login_logo_pic, borderwidth=0)
        self.login_lbl.place(x=270, y=20)


        # ===================================== labels ==========================================

        self.lbl_username = Label(self.main_frame, text="User Name", font=('times new roman', 15, 'bold'), bg="white")
        self.lbl_username.place(x=300, y=250)

        self.lbl_password = Label(self.main_frame, text="Password", font=('times new roman', 15, 'bold'), bg="white")
        self.lbl_password.place(x=300, y=320)

        user = StringVar()
        password = StringVar()

        txt = Entry(self.main_frame, textvariable=user, font=(12), border=2)
        txt.place(x=300, y=280)

        txt1 = Entry(self.main_frame, textvariable=password, show="*", font=(12), border=2)
        txt1.place(x=300, y=360)

        def submit():
            coon = mysql.connector.connect(host="localhost", user="root",password="12345", database="cms")
            my_cursor = coon.cursor()
            my_cursor.execute("Select * from login where Email = %s and Password = %s", (
                user.get(),
                password.get()
            ))
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("error", "email or password is not correct ")
            else:
                messagebox.showinfo('info', 'Login successfully')
                lobby_variable = (self.root)
                open_lobby = import_class(lobby_variable)
            coon.commit()
            coon.close()

        def singup():
            open_singup = Toplevel(self.root)
            variable = login_singup(open_singup)
        def remove():
            user.set("")
            password.set("")

        self.btn_img = ImageTk.PhotoImage(file="images\singh6.png")
        self.btn_sing = Button(self.main_frame, command=submit, image=self.btn_img, bd=0, bg="white")
        self.btn_sing.place(x=150, y=404)

        self.pic2 = ImageTk.PhotoImage(file="images\singimgae.png")
        self.btn_sing = Button(self.main_frame, command=singup, text="Sing Up", compound="left", image=self.pic2,
                               bd=0, bg="white", font=('times new roman', 25, 'bold'))
        self.btn_sing.place(x=550, y=5)

        self.btn_reset = Button(self.main_frame, text="Remove", command=remove, bd=0, bg="white", fg="red")
        self.btn_reset.place(x=450, y=390)


if __name__ == '__main__':
    root = Tk()
    obj = hello(root)
    root.mainloop()
