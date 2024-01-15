import tkinter as tk
from tkinter.ttk import *

class Game:
    Language = ""
    Difficulty_level = ""
    Word_Min_Len = 0
    Word_Max_Len = 1
    Round = 0
    Points = 0

def close_window(event=None):
    window.destroy()

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def page_label(label_text,size):
    label = tk.Label(window, text = label_text, fg = '#FFF', bg = "#622567", font=("Helvetica", size, "bold"))
    label.pack(padx=20, pady=20)

def page_title_lable(page_title):
    page_label(page_title, 22)

def page_text(text):
    page_label(text,15)

def exit_button():
    exit_bar = tk.Frame(window, bg="#622567", height=40)
    exit_bar.pack(side='bottom', fill='x')

    button_exit = tk.Button(
        exit_bar,
        text="Exit",
        command=lambda: close_window(),
        fg="#FFF",
        bg="#622567",
        font=("Arial", 12),
        relief=tk.FLAT,
    )
    button_exit.pack(side=tk.RIGHT, padx=5)

    button_home = tk.Button(
        exit_bar,
        text="Back",
        command=lambda: go_back(),
        fg="#FFF",
        bg="#622567",
        activebackground="#622567",
        font=("Arial", 12),
        relief=tk.FLAT,
    )
    button_home.pack(side=tk.LEFT, padx=5, pady=5)  # Added pady to lower the "Back To Home" button

def go_back():
    clear_window()
    home_page()

def back_button(back_page, button_home=None):
    back_but = tk.Frame(window, bg="#622567", height=40)
    back_but.pack(side='bottom', fill='x')

    def resize_button(event=None):
        button.config(width=back_but.winfo_width())  # Adjust the division factor as needed

    back_but.bind('<Configure>', resize_button)

    if back_page == "home":
        button = tk.Button(
            back_but,
            text="Back To Home",
            command=lambda: go_back(),
            fg="#FFF",
            bg="#622567",
            activebackground="#622567",
            font=("Arial", 12),
            relief=tk.FLAT,
        )
<<<<<<< .mine


||||||| .r92
        #button.pack(side=tk.centre, padx=5)
=======

>>>>>>> .r98
    else:
        button = tk.Button(
            back_but,
            text="Back",
            command=lambda: show_page(back_page),
            fg="#FFF",
            bg="#622567",
            activebackground="#622567",
            font=("Arial", 12),
            relief=tk.FLAT,
        )

<<<<<<< .mine
    button.pack(side=tk.LEFT, padx=5)
||||||| .r92
    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
=======

    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
>>>>>>> .r98
    resize_button()


def sound_button():
    #this is where the text to speech will be put
    pass

def random_word():
    page_text("Random word " + str(Game.Round))
    page_text("Min word length " + str(Game.Word_Min_Len) + " | Max word length " + str(Game.Word_Max_Len))

def make_button(button_name,command_for_button):
    button_frame = tk.Frame(window, bg="#622567")
    button_frame.pack(pady=15, padx=50)

    def resize_button(event=None):
        button.config(width=button_frame.winfo_width())

    button_frame.bind('<Configure>', resize_button)

    button = tk.Button(
        button_frame,
        text=button_name,
        command=command_for_button,
        fg="#FFF",
        bg="#622567",
        activebackground="#622567",
        font=("Arial", 12, "bold"),
        padx=10,
        pady=5,
        relief=tk.FLAT,
    )
    button.pack(fill=tk.X, padx=50, pady=5)


def show_page(page_title):
    clear_window()

    if page_title == "Pick a Language":
        page_title_lable(page_title)
        make_button("English", lambda: show_page("English"))
        make_button("French", lambda: show_page("French"))
        make_button("Italian", lambda: show_page("Italian"))
        exit_button()
        back_button("home")


    elif page_title in ["English", "French", "Italian"]:
        Game.Language = page_title
        page_title_lable("Pick a Difficulty Level")
        page_text("Your Language is: " + Game.Language)
        #page_text("Pick the Difficulty")
        make_button("Easy", lambda: show_page("Easy"))
        make_button("Medium", lambda: show_page("Medium"))
        make_button("Hard", lambda: show_page("Hard"))
        exit_button()
        back_button("home")
        back_button("Pick a Language")

    elif page_title in ["Easy", "Medium", "Hard"]:
        Game.Difficulty_level = page_title
        if page_title == "Easy":
            Game.Word_Min_Len = 2
            Game.Word_Max_Len = 4
        elif page_title == "Medium":
            Game.Word_Min_Len = 5
            Game.Word_Max_Len = 6
        elif page_title == "Hard":
            Game.Word_Min_Len = 7
            Game.Word_Max_Len = 10

        Game.Round = 0
        Game.Points = 0
        page_title_lable("Click Play to start")
        page_text("Language: " + Game.Language + " | Level: " + Game.Difficulty_level)
        make_button("Play", lambda: show_page("Play"))
        exit_button()
        back_button("home")
        back_button(Game.Language)

    elif page_title in ["Play", "Bad", "Okay", "Good"]:
        Game.Round += 1
        if page_title == "Bad":
            Game.Points = Game.Points + 1
        elif page_title == "Okay":
            Game.Points = Game.Points + 2
        elif page_title == "Good":
            Game.Points = Game.Points + 3


        if Game.Round <= 20:
            page_title_lable("Round " + str(Game.Round))

            random_word()

            make_button("Sound Button", lambda: sound_button())
            make_button("Bad", lambda: show_page("Bad"))
            make_button("Okay", lambda: show_page("Okay"))
            make_button("Good", lambda: show_page("Good"))
            exit_button()
            back_button("home")
            back_button(Game.Language)
        else:
            page_title_lable("Completed")
            page_text("Final Score: " + str(Game.Points) + "/60")
            exit_button()
            back_button("home")


def home_page():
    clear_window()
    page_title_lable("Language Learning Gamification")
    make_button("Game",(lambda: show_page("Pick a Language")))
    exit_button()

def main():
    global window
    window = tk.Tk()
    window.title("Group 04: LLAMA Project")
    window.geometry("600x550")  # Set window size to 400x600
    window.configure(bg="#622567")  # Set forest green background color
    home_page()
    window.mainloop()

if __name__ == "__main__":
    main()