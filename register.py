from tkinter import *
from tkinter import messagebox
from db import Database

class RegisterApp:
    def __init__(self, root):
        self.root = root
        self.db = Database()

        self.root.title("MCQ Test System - Register")
        self.root.geometry("700x550")
        self.root.configure(bg="#e9eef3")

        self.build_ui()

    def build_ui(self):
        self.card = Frame(self.root, bg="white", width=420, height=420)
        self.card.place(relx=0.5, rely=0.5, anchor=CENTER)

        Label(
            self.card,
            text="Create Account",
            font=("Helvetica", 20, "bold"),
            bg="white",
            fg="#222"
        ).pack(pady=(35, 20))

        Label(self.card, text="Full Name", bg="white", anchor="w").pack(fill="x", padx=40)
        self.name = Entry(self.card, font=("Helvetica", 11), bd=1, relief="solid")
        self.name.pack(fill="x", padx=40, pady=(5, 15), ipady=6)

        Label(self.card, text="Username", bg="white", anchor="w").pack(fill="x", padx=40)
        self.username = Entry(self.card, font=("Helvetica", 11), bd=1, relief="solid")
        self.username.pack(fill="x", padx=40, pady=(5, 15), ipady=6)

        Label(self.card, text="Password", bg="white", anchor="w").pack(fill="x", padx=40)
        self.password = Entry(self.card, font=("Helvetica", 11), show="*", bd=1, relief="solid")
        self.password.pack(fill="x", padx=40, pady=(5, 25), ipady=6)

        Button(
            self.card,
            text="Register",
            font=("Helvetica", 11, "bold"),
            bg="#4a90e2",
            fg="white",
            bd=0,
            activebackground="#357ABD",
            activeforeground="white",
            command=self.register_user
        ).pack(fill="x", padx=40, ipady=8)

    def register_user(self):
        sucess = self.db.register_user(
            self.name.get(),
            self.username.get(),
            self.password.get()
        )

        user = self.db.login_user(
            self.username.get(),
            self.password.get()
        )

        if sucess:
            messagebox.showinfo("Success", "User registered successfully!")
            self.root.destroy()

            from dashboard import DashboardApp
            new_root = Tk()
            DashboardApp(new_root, user)
            new_root.mainloop()
        else:
            messagebox.showerror("Error", "Username Already Exists")