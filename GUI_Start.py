import tkinter as tk
from tkinter import messagebox


def close_window(event=None):
    window.destroy()


def page_label(page_title):
    label = tk.Label(window, text=page_title, fg='#FFF', bg="#622567", font=("Helvetica", 22, "bold"))
    label.pack(padx=20, pady=20)


def exit_button():
    exit_bar = tk.Frame(window, bg="#622567", height=40)
    exit_bar.pack(side='bottom', fill='x')
    exit_bar.bind("<Button-1>", close_window)

    button = tk.Button(
        exit_bar,
        text="Exit",
        command=lambda: close_window(),
        fg="#FFF",
        bg="#622567",
        font=("Arial", 12),
        relief=tk.FLAT,
    )
    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


##def button(button_name):


def main_page():
    page_label("Language Learning Gamification")
    ##button("Start Game")
    exit_button()


window = tk.Tk()
window.title("GUI for project")
window.geometry("600x500")  # Set window size to 400x600
window.configure(bg="#622567")  # Set forest green background color
main_page()
window.mainloop()











