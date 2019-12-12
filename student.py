from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox


class Student:
    def __init__(self):
        self.root = Tk()
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        # ==============label======================
        title = Label(self.root, text="Student Management System", font=(
            "times new roman", 40, "bold"), bg="light green", fg="white", bd=10, relief=GROOVE)
        title.pack(side=TOP, fill=X)

        # ==================All variables=========================
        self.roll_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # ===================manage frame============================
        manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="light green")
        manage_frame.place(x=20, y=100, width=450, height=580)

        m_title = Label(manage_frame, text="Manage Students", font=(
            "times new roman", 20, "bold"), bg="light green", fg="white")
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(manage_frame, text="Roll Number", font=(
            "times new roman", 16, "bold"), bg="light green", fg="white")
        lbl_roll.grid(row=1, column=0, pady=10, padx=10, sticky=W)

        txt_roll = Entry(manage_frame, font=(
            "times new roman", 16, "bold"), textvariable=self.roll_no_var, bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky=W)

        lbl_name = Label(manage_frame, text="Name", font=(
            "times new roman", 16, "bold"), bg="light green", fg="white")
        lbl_name.grid(row=2, column=0, pady=10, padx=10, sticky=W)

        txt_name = Entry(manage_frame, font=(
            "times new roman", 16, "bold"), textvariable=self.name_var, bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky=W)

        lbl_email = Label(manage_frame, text="Email", font=(
            "times new roman", 16, "bold"), bg="light green", fg="white")
        lbl_email.grid(row=3, column=0, pady=10, padx=10, sticky=W)

        txt_email = Entry(manage_frame, font=(
            "times new roman", 16, "bold"), textvariable=self.email_var, bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky=W)

        lbl_gender = Label(manage_frame, text="Gender", font=(
            "times new roman", 16, "bold"), bg="light green", fg="white")
        lbl_gender.grid(row=4, column=0, pady=10, padx=10, sticky=W)

        combo_gender = ttk.Combobox(manage_frame, font=(
            "times new roman", 14, "bold"), textvariable=self.gender_var, state="readonly")
        combo_gender['values'] = ("male", "female", "other")
        combo_gender.grid(row=4, column=1, padx=10, pady=10)

        lbl_cno = Label(manage_frame, text="Contact No", font=(
            "times new roman", 16, "bold"), bg="light green", fg="white")
        lbl_cno.grid(row=5, column=0, pady=10, padx=10, sticky=W)

        txt_cno = Entry(manage_frame, font=(
            "times new roman", 16, "bold"), textvariable=self.contact_var, bd=5, relief=GROOVE)
        txt_cno.grid(row=5, column=1, pady=10, padx=20, sticky=W)

        lbl_dob = Label(manage_frame, text="D.O.B", font=(
            "times new roman", 16, "bold"), bg="light green", fg="white")
        lbl_dob.grid(row=6, column=0, pady=10, padx=10, sticky=W)

        txt_dob = Entry(manage_frame, font=(
            "times new roman", 16, "bold"), textvariable=self.dob_var, bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky=W)

        lbl_address = Label(manage_frame, text="Address", font=(
            "times new roman", 16, "bold"), bg="light green", fg="white")
        lbl_address.grid(row=7, column=0, pady=10, padx=10, sticky=W)

        self.txt_address = Text(
            manage_frame, width=34, height=4, font=("", 10))
        self.txt_address.grid(row=7, column=1, padx=10, pady=10, sticky=W)

        # ==================button frame===================
        btn_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="light green")
        btn_frame.place(x=10, y=500, width=420)

        add_btn = Button(btn_frame, text="Add", width=10, command=self.add_students).grid(
            row=0, column=0, padx=10, pady=10)
        update_btn = Button(btn_frame, text="Update", width=10, command=self.update_data).grid(
            row=0, column=1, padx=10, pady=10)
        delete_btn = Button(btn_frame, text="Delete", width=10, command=self.delete_data).grid(
            row=0, column=2, padx=10, pady=10)
        clear_btn = Button(btn_frame, text="Clear", width=10, command=self.clear).grid(
            row=0, column=3, padx=10, pady=10)

        # ===================detail frame============================
        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="light green")
        detail_frame.place(x=500, y=100, width=800, height=580)

        lbl_address = Label(detail_frame, text="Search By", font=(
            "times new roman", 16, "bold"), bg="light green", fg="white")
        lbl_address.grid(row=0, column=0, pady=10, padx=10, sticky=W)

        combo_search = ttk.Combobox(detail_frame, font=(
            "times new roman", 12, "bold"), textvariable=self.search_by, state="readonly")
        combo_search['values'] = ("rollno", "name", "contact")
        combo_search.grid(row=0, column=1, padx=10, pady=10)

        txt_search = Entry(detail_frame, textvariable=self.search_txt, font=(
            "times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky=W)

        search_btn = Button(detail_frame, text="Search", width=10, command=self.search_data).grid(
            row=0, column=3, padx=10, pady=10)
        searchall_btn = Button(detail_frame, text="Search All", width=10, command=self.fetch_data).grid(
            row=0, column=4, padx=10, pady=10)

        # ================tabel frame===================
        tabel_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="light green")
        tabel_frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(tabel_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(tabel_frame, orient=VERTICAL)
        self.student_tabel = ttk.Treeview(tabel_frame, columns=(
            "roll", "name", "email", "gender", "contact", "dob", "address"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_tabel.xview)
        scroll_y.config(command=self.student_tabel.yview)
        self.student_tabel.heading("roll", text="Roll No.")
        self.student_tabel.heading("name", text="Name")
        self.student_tabel.heading("email", text="Email")
        self.student_tabel.heading("gender", text="Gender")
        self.student_tabel.heading("contact", text="Contact")
        self.student_tabel.heading("dob", text="DOB")
        self.student_tabel.heading("address", text="Address")
        self.student_tabel['show'] = 'headings'
        self.student_tabel.column("roll", width=100)
        self.student_tabel.column("name", width=100)
        self.student_tabel.column("email", width=100)
        self.student_tabel.column("gender", width=100)
        self.student_tabel.column("contact", width=100)
        self.student_tabel.column("dob", width=100)
        self.student_tabel.column("address", width=150)
        self.student_tabel.pack(fill=BOTH, expand=1)

        self.student_tabel.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()
        self.root.mainloop()

    def add_students(self):
        if self.roll_no_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            conn = pymysql.connect(host="localhost", user="root",
                                   password="", database="student_management")
            cur = conn.cursor()
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)", (
                self.roll_no_var.get(),
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.txt_address.get('1.0', END)
            ))
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted!")

    def fetch_data(self):

        conn = pymysql.connect(host="localhost", user="root",
                               password="", database="student_management")
        cur = conn.cursor()
        cur.execute("select * from student")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for row in rows:
                self.student_tabel.insert('', END, values=row)
                conn.commit()
            conn.close()

    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete('1.0', END)

    def get_cursor(self, event):
        cursor_row = self.student_tabel.focus()
        contents = self.student_tabel.item(cursor_row)
        row = contents['values']
        # print(row)

        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[6])

    def update_data(self):
        conn = pymysql.connect(host="localhost", user="root",
                               password="", database="student_management")
        cur = conn.cursor()
        cur.execute("update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where rollno=%s",
                    (
                        self.name_var.get(),
                        self.email_var.get(),
                        self.gender_var.get(),
                        self.contact_var.get(),
                        self.dob_var.get(),
                        self.txt_address.get('1.0', END),
                        self.roll_no_var.get()
                    ))
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()

    def delete_data(self):
        conn = pymysql.connect(host="localhost", user="root",
                               password="", database="student_management")
        cur = conn.cursor()
        cur.execute("delete from student where rollno=%s",
                    self.roll_no_var.get())
        conn.commit()
        conn.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        conn = pymysql.connect(host="localhost", user="root",
                               password="", database="student_management")
        cur = conn.cursor()
        cur.execute("select * from student where"+str(self.search_by.get())
                    + " LIKE '%"+str(self.search_txt.get()))+"%'"
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for row in rows:
                self.student_tabel.insert('', END, values=row)
            conn.commit()
        conn.close()


# root = Tk()
# ob = Student(root)
# root.mainloop()
