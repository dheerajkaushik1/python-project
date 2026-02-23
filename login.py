from tkinter import *
from tkinter import messagebox
from db import Database
from quiz import QuizApp

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.db = Database()

        self.root.title("MCQ Test System - Login")
        self.root.geometry("700x500")
        self.root.configure(bg="#e9eef3")

        self.build_ui()

    def build_ui(self):
        self.card = Frame(self.root, bg="white", width=400, height=350)
        self.card.place(relx=0.5, rely=0.5, anchor=CENTER)

        Label(
            self.card,
            text="Welcome Back",
            font=("Helvetica", 20, "bold"),
            bg="white",
            fg="#222"
        ).pack(pady=(30, 10))

        Label(
            self.card,
            text="Login to continue",
            font=("Helvetica", 11),
            bg="white",
            fg="#666"
        ).pack(pady=(0, 25))

        Label(self.card, text="Username", bg="white", anchor="w").pack(fill="x", padx=40)
        self.username = Entry(self.card, font=("Helvetica", 11), bd=1, relief="solid")
        self.username.pack(fill="x", padx=40, pady=(5, 15), ipady=6)

        Label(self.card, text="Password", bg="white", anchor="w").pack(fill="x", padx=40)
        self.password = Entry(self.card, font=("Helvetica", 11), show="*", bd=1, relief="solid")
        self.password.pack(fill="x", padx=40, pady=(5, 25), ipady=6)

        Button(
            self.card,
            text="Login",
            font=("Helvetica", 11, "bold"),
            bg="#4a90e2",
            fg="white",
            bd=0,
            activebackground="#357ABD",
            activeforeground="white",
            command=self.login
        ).pack(fill="x", padx=40, ipady=8)

        Button(
            self.card,
            text="Create Account",
            font=("Helvetica", 10),
            bg="white",
            fg="#4a90e2",
            bd=0,
            activebackground="white",
            activeforeground="#357ABD",
            command=self.register
        ).pack(pady=15)

    def login(self):
        user = self.db.login_user(
            self.username.get(),
            self.password.get(),
        )

        if user:
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()

            from dashboard import DashboardApp
            new_root = Tk()
            DashboardApp(new_root, user)
            new_root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def register(self):
        from register import RegisterApp
        self.root.destroy()
        new_root = Tk()
        RegisterApp(new_root)
        new_root.mainloop()
