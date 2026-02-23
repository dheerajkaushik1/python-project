from tkinter import *
from tkinter import messagebox
from db import Database

class QuizApp:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.root.title("MCQ Test System")
        self.root.geometry("1000x700")
        self.root.configure(bg="#e9eef3")

        self.db = Database()
        self.questions = self.db.fetch_questions()

        self.option_map = {
            0: "A",
            1: "B",
            2: "C",
            3: "D"
        }

        self.current_page = 0
        self.user_answers = {}

        self.time_left = 20

        self.build_ui()
        self.show_questions()
        self.update_timer()

    def build_ui(self):
        self.header = Frame(self.root, bg="#4a90e2", height=60)
        self.header.pack(fill="x")

        Label(
            self.header,
            text="MCQ Examination System",
            font=("Helvetica", 16, "bold"),
            bg="#4a90e2",
            fg="white"
        ).pack(side=LEFT, padx=20)

        self.timer_label = Label(
            self.header,
            text="Time Left: 10:00",
            font=("Helvetica", 14, "bold"),
            bg="#4a90e2",
            fg="white"
)
        self.timer_label.pack(side=RIGHT, padx=20)

        self.card = Frame(self.root, bg="white")
        self.card.pack(padx=40, pady=20, fill="both", expand=True)

        self.canvas = Canvas(self.card, bg="white", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = Scrollbar(self.card, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame = Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.nav_frame = Frame(self.root, bg="#e9eef3")
        self.nav_frame.pack(pady=10)

        Button(
            self.nav_frame,
            text="Previous",
            font=("Helvetica", 10, "bold"),
            bg="#cccccc",
            bd=0,
            padx=20,
            command=self.prev_page
        ).pack(side=LEFT, padx=10, ipady=6)

        Button(
            self.nav_frame,
            text="Next",
            font=("Helvetica", 10, "bold"),
            bg="#4a90e2",
            fg="white",
            bd=0,
            padx=20,
            activebackground="#357ABD",
            activeforeground="white",
            command=self.next_page
        ).pack(side=LEFT, padx=10, ipady=6)

        Button(
            self.nav_frame,
            text="Submit Test",
            font=("Helvetica", 10, "bold"),
            bg="#28a745",
            fg="white",
            bd=0,
            padx=20,
            activebackground="#1e7e34",
            activeforeground="white",
            command=self.submit_test
        ).pack(side=LEFT, padx=10, ipady=6)

        self.canvas.bind_all(
            "<MouseWheel>",
            lambda event: self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        )

    def show_questions(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        start = self.current_page * 10
        end = start + 10

        for i, q in enumerate(self.questions[start:end]):
            q_id = q[0]

            Label(
                self.frame,
                text=f"Q{start+i+1}. {q[1]}",
                font=("Helvetica", 12, "bold"),
                bg="white",
                anchor="w",
                wraplength=850,
                justify=LEFT
            ).pack(fill="x", pady=(15, 5), padx=20)

            var = IntVar(value=self.user_answers.get(q_id, -1))

            for idx, option in enumerate(q[2:6]):
                Radiobutton(
                    self.frame,
                    text=option,
                    variable=var,
                    value=idx,
                    font=("Helvetica", 11),
                    bg="white",
                    anchor="w",
                    activebackground="white"
                ).pack(anchor="w", padx=40)

            self.user_answers[q_id] = var

    def next_page(self):
        if (self.current_page + 1) * 10 < len(self.questions):
            self.current_page += 1
            self.show_questions()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.show_questions()

    def submit_test(self):
        score = 0
        total = len(self.questions)

        for q in self.questions:
            q_id = q[0]
            correct_answer = q[6]

            var = self.user_answers.get(q_id)
            if var:
                selected = var.get()
            else:
                selected = -1

            if self.option_map.get(selected) == correct_answer:
                score += 1
        
        messagebox.showinfo(
            "Result",
            f"Your score: {score} / {total}"
        )

        self.root.destroy()

        from dashboard import DashboardApp
        new_root = Tk()
        DashboardApp(new_root, self.user)
        new_root.mainloop()

    def update_timer(self):
        mins = self.time_left // 60
        secs = self.time_left % 60

        self.timer_label.config(text=f"Time Left: {mins:02}:{secs:02}")

        if self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time's Up!", "You have run out of time.")
            self.submit_test()