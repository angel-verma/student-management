from tkinter import*
from PIL import ImageTk
from tkinter import messagebox


class LoginSystem:
    def __init__(self, root):
        # print("Hello")
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        # ==========All Images===========
        self.bg_icon = ImageTk.PhotoImage(file="images/bg.jpg")
        self.admin_icon = ImageTk.PhotoImage(file="images/admin.jpg")

        # ==========variable=========
        self.uname = StringVar()
        self.pass_ = StringVar()

        # background image
        bg_lbl = Label(self.root, image=self.bg_icon).pack()

        title = Label(self.root, text="Login System", font=(
            "times new roman", 40, "bold"), bd=5, relief=GROOVE, bg="yellow", fg="red")
        title.place(x=0, y=0, relwidth=1)

        Login_Frame = Frame(self.root, bg="white")
        Login_Frame.place(x=400, y=150)

        logolbl = Label(Login_Frame, image=self.admin_icon, bd=0).grid(
            row=0, column=0, pady=20, columnspan=2)

        lbluser = Label(Login_Frame, text="Username", font=(
            "times new roman", 20, "bold"), bg="white").grid(row=1, column=0, padx=20, pady=10)
        txtuser = Entry(Login_Frame, textvariable=self.uname, bd=5,
                        relief=GROOVE, font=("", 15)).grid(row=1, column=1, padx=20)

        lblpass = Label(Login_Frame, text="Password", font=(
            "times new roman", 20, "bold"), bg="white").grid(row=2, column=0, padx=20, pady=10)
        txtpass = Entry(Login_Frame, bd=5, textvariable=self.pass_,
                        relief=GROOVE, font=("", 15), show="*").grid(row=2, column=1, padx=20)

        btn_login = Button(Login_Frame, text="Login", width=15, font=(
            "times new roman", 16, "bold"), bg="yellow", fg="green", command=lambda: login(self)).grid(row=3, column=1, pady=10)


def login(self):
    if self.uname.get() == "" or self.pass_.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.uname.get() == "admin" or self.pass_.get() == "1234":
        # messagebox.showerror("Successfull", f"Welcome {self.uname.get()}")
        self.root.destroy()
        import student
        student.Student()
    else:
        messagebox.showerror("Error", "Username and Password doesn't match!")


root = Tk()
obj = LoginSystem(root)
root.mainloop()
