from unittest import TestCase
from UserProfile import  UserProfileManager


class TestUserProfileManager(TestCase):
    def test_save_user_profile(self):
        manager = UserProfileManager("test_users.json")
        user = {
                'name': "JOnathan Testington",
                'age': "adult",
                'highscore': 33
            }
        manager.save_user_profile(user)

    def test_save_duplicated_user_profile(self):
        manager = UserProfileManager("test_users.json")
        user = {
            'name': "John",
            'age': "adult",
            'highscore': 0
        }
        user1 = {
            'name': "John",
            'age': "child",
            'highscore': 0
        }
        # Saving the first user (expecting None)
        result = manager.save_user_profile(user)
        print(result)
        self.assertIsNone(result)

        # Attempting to save the duplicated user (expecting an exception)
        result2 = manager.save_user_profile(user1)
        print(result2)
        self.assertIsNotNone(result2)

