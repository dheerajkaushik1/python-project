from tkinter import *
from quiz import QuizApp
from login import LoginApp

class DashboardApp:
    def __init__(self, root, user):
        self.root = root
        self.user = user

        self.root.title("Dashboard")
        self.root.geometry("700x500")
        self.root.configure(bg="#e9eef3")

        self.build_ui()

    def build_ui(self):
        self.card = Frame(self.root, bg="white", width=500, height=400)
        self.card.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.content = Frame(self.card, bg="white")
        self.content.pack(fill="both", expand=True, padx=40, pady=40)

        Label(
            self.content,
            text="Student Dashboard",
            font=("Helvetica", 20, "bold"),
            bg="white",
            fg="#222"
        ).pack(pady=(0, 25))

        Frame(self.content, bg="#dddddd", height=1).pack(fill="x", pady=(0, 20))

        Label(
            self.content,
            text=f"Name: {self.user[1]}",
            font=("Helvetica", 12),
            bg="white",
            anchor="w"
        ).pack(fill="x", pady=5)

        Label(
            self.content,
            text=f"Username: {self.user[2]}",
            font=("Helvetica", 12),
            bg="white",
            anchor="w"
        ).pack(fill="x", pady=5)

        Label(self.content, bg="white").pack(pady=15)

        Button(
            self.content,
            text="Start Test",
            font=("Helvetica", 11, "bold"),
            bg="#4a90e2",
            fg="white",
            bd=0,
            padx=20,
            activebackground="#357ABD",
            activeforeground="white",
            command=self.start_test
        ).pack(ipady=8, fill="x")

        Button(
            self.content,
            text="Logout",
            font=("Helvetica", 10),
            bg="#cccccc",
            bd=0,
            command=self.logout
        ).pack(ipady=6, fill="x", pady=10)

    def start_test(self):
        self.root.destroy()
        new_root = Tk()
        QuizApp(new_root, self.user)
        new_root.mainloop()

    def logout(self):
        self.root.destroy()
        new_root = Tk()
        LoginApp(new_root)
        new_root.mainloop()
