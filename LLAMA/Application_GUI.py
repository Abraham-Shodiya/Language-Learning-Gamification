import tkinter as tk
from tkinter import messagebox
from Game import Game
from UserProfile import User, UserProfileManager


def get_user_profile(user_profiles, username):
    for user in user_profiles:
        if user['name'] == username:
            return user

class ApplicationGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.total_points = None
        self.current_username = None
        self.title("Group 04: LLAMA Project")
        self.geometry("550x600")
        self.configure(bg="#622567")
        self.home_page()

        self.game_language = 'en'
        self.game_difficulty = 'easy'
        self.final_score = 0

    def close_window(self, event=None):
        self.destroy()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def page_label(self, label_text, size):
        label = tk.Label(self, text=label_text, fg='#FFF', bg="#622567", font=("Helvetica", size, "bold"))
        label.pack(padx=20, pady=20)

    def page_title_label(self, page_title):
        self.page_label(page_title, 22)

    def page_text(self, text):
        self.page_label(text, 15)

    def exit_button(self):
        exit_bar = tk.Frame(self, bg="#622567", height=40)
        exit_bar.pack(side='bottom', fill='x')

        button_exit = tk.Button(
            exit_bar,
            text="Exit",
            command=lambda: self.close_window(),
            fg="#FFF",
            bg="#622567",
            font=("Arial", 12),
            relief=tk.FLAT,
        )
        button_exit.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

    def go_back(self):
        self.clear_window()
        self.home_page()

    def back_button(self, back_page, button_home=None):
        back_but = tk.Frame(self, bg="#622567", height=40)
        back_but.pack(side='bottom', fill='x')

        def resize_button(event=None):
            button.config(width=back_but.winfo_width())  # Adjust the division factor as needed

        back_but.bind('<Configure>', resize_button)

        if back_page == "home":
            button = tk.Button(
                back_but,
                text="Back To Home",
                command=lambda: self.go_back(),
                fg="#FFF",
                bg="#622567",
                activebackground="#622567",
                font=("Arial", 12),
                relief=tk.FLAT
            )
        else:
            button = tk.Button(
                back_but,
                text="Back",
                command=lambda: self.show_page(back_page),
                fg="#FFF",
                bg="#622567",
                activebackground="#622567",
                font=("Arial", 12),
                relief=tk.FLAT,
            )
        button.place(relx = 0.5, rely = 0.5, anchor=tk.CENTER)
        resize_button()

    def make_button(self, button_name, command_for_button):
        button_frame = tk.Frame(self, bg="#622567")
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

    def show_page(self, page_title):
        self.clear_window()

        if page_title == "Pick a Language":
            self.pick_language_page()

        elif page_title == "Pick a Difficulty":
            self.pick_difficulty_page()

        elif page_title == "Play":
            self.play_game_page()

        elif page_title == "Game Completed":
            self.game_completed_page()

        else:
            self.home_page()

    def home_page(self):
        self.clear_window()
        self.page_title_label("Language Learning Gamification")
        self.make_button("New Game", lambda: self.create_user())
        self.make_button("Load Game", lambda: self.load_user())
        self.exit_button()

    def create_user(self):
        self.clear_window()
        self.page_title_label("Create a New User")

        username_label = tk.Label(self, text="Username:", fg='#FFF', bg="#622567", font=("Helvetica", 12, "bold"))
        username_label.pack(pady=5)
        self.current_username = tk.Entry(self, font=("Helvetica", 12))
        self.current_username.pack(pady=5)

        save_button = tk.Button(
            self,
            text="Save User",
            command=lambda: self.save_user(self.current_username.get()),
            fg="#FFF",
            bg="#622567",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=5,
            relief=tk.FLAT)
        save_button.pack(pady=20)

        self.back_button(self.home_page)

    def save_user(self, username):
        new_user = User(name=username, highscore=0)

        manager = UserProfileManager("user_profiles.json")
        result = manager.save_user_profile(new_user)
        if result is not None:
            messagebox.showinfo("User Exists", f"{result}")
            self.create_user()

        elif result is None:
            messagebox.showinfo("User Added", f"\nUser {username}\nCreated successfully!")
            self.show_page("Pick a Language")

    def load_user(self):
        self.clear_window()
        self.page_title_label("Load User")
        self.page_text("Select User")
        manager = UserProfileManager("user_profiles.json")
        user_profiles = manager.load_profiles()

        # If no user is saved, a message will be showed
        if not user_profiles:
            self.page_text("No user profiles saved yet!")
            self.back_button("Back")
            return

        # Convert user profiles to a list of usernames
        usernames = [user['name'] for user in user_profiles]

        # Variable to hold the selected username
        self.current_username = tk.StringVar(self)

        self.current_username.set(usernames[0])

        user_menu = tk.OptionMenu(self, self.current_username, *usernames)
        user_menu.pack()

        self.make_button("Load User", lambda: self.load_selected_user(self.current_username.get()))

    def load_selected_user(self, current_username):
        messagebox.showinfo("User Loaded", f"User {current_username} loaded successfully!")
        self.show_page("Pick a Language")

    def new_game_page(self):
        self.show_page("Pick a Language")

    def pick_language_page(self):
        self.page_title_label("Pick a Language")

        def choose_language(language):
            self.game_language = language
            self.show_page("Pick a Difficulty")

        self.make_button("English", lambda: choose_language("en"))
        self.make_button("French", lambda: choose_language("fr"))
        self.make_button("Italian", lambda: choose_language("it"))
        self.exit_button()
        self.back_button("home")

    def pick_difficulty_page(self):
        self.page_title_label("Pick a Difficulty Level")
        self.page_text("Your Language is: " + self.game_language)

        def choose_difficulty(difficulty):
            self.game_difficulty = difficulty
            self.show_page("Play")

        self.make_button("Easy", lambda: choose_difficulty("Easy"))
        self.make_button("Medium", lambda: choose_difficulty("Medium"))
        self.make_button("Hard", lambda: choose_difficulty("Hard"))

        self.exit_button()
        self.back_button("home")
        self.back_button("Pick a Language")

    def play_game_page(self):
        self.page_title_label("Click Play to start")

        game = Game(self.game_language, self.game_difficulty)
        self.page_text(f"Language: {game.language} | Level: {game.difficulty}")
        self.make_button("Play", lambda: self.new_game_round(game))

        self.exit_button()
        self.back_button("home")
        self.back_button("Pick a Difficulty")

    def new_game_round(self, game):
        self.clear_window()
        if game.current_round < game.rounds:
            new_round = game.get_next_round()
            self.page_title_label("Round " + str(new_round.number))
            self.page_text(new_round.word)

            def choose_answer(answer):
                game.submit_answer(answer)
                self.new_game_round(game)

            self.make_button("Listen to pronunciation", lambda: game.pronounce_word(new_round.word))
            self.make_button("Bad", lambda: choose_answer("Bad"))
            self.make_button("Okay", lambda: choose_answer("Okay"))
            self.make_button("Good", lambda: choose_answer("Good"))

            self.exit_button()
            self.back_button("home")
        else:
            self.final_score = game.total_points
            self.show_page("Game Completed")

    def game_completed_page(self):
        self.page_title_label("Game Completed")
        self.page_text("Final Score: " + str(self.final_score))

        manager = UserProfileManager("user_profiles.json")
        user_profiles = manager.load_profiles()

        if any(profile['name'] == self.current_username.get() for profile in user_profiles):
            previous_highscore = get_user_profile(user_profiles, self.current_username.get())['highscore']
            if previous_highscore < self.final_score:
                manager.update_highscore(self.current_username.get(), self.final_score)
                self.page_text(f"{self.current_username.get()} New Highscore!")

        self.exit_button()
        self.back_button("home")

    def start(self):
        self.mainloop()
