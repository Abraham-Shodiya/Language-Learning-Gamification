import json
import os


class User:
    def __init__(self, name, highscore):
        self.name = name
        self.highscore = highscore


class UserProfileManager:
    def __init__(self, filename):
        self.filename = filename

    def save_user_profile(self, new_user):
        profiles = self.load_profiles()
        user_exists = False

        # Check if the user already exists
        for user in profiles:
            if user['name'].lower() == new_user.name.lower():
                user_exists = True
                break

        # If the user does not exist, append the new user
        if not user_exists:
            profiles.append({
                'name': new_user.name.lower(),
                'highscore': new_user.highscore
            })
            self.save_profiles(profiles)
            return None

        elif user_exists:
            return "A user with the same name already exists."

    def load_profiles(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    profiles = json.load(file)
            else:
                profiles = []
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading profiles: {e}")
            profiles = []
        return profiles

    def save_profiles(self, profiles):
        try:
            with open(self.filename, 'w') as file:
                json.dump(profiles, file, indent=2)
        except IOError as e:
            print(f"Error saving profiles: {e}")

    def update_highscore(self, username, new_highscore):
        profiles = self.load_profiles()

        for profile in profiles:
            if profile['name'].lower() == username.lower():
                profile['highscore'] = new_highscore
                break

        self.save_profiles(profiles)