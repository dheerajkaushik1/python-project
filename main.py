from tkinter import *
from login import LoginApp

def main():
    root = Tk()
    root.title("MCQ Test - Login")
    root.geometry("400x400")
    LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

