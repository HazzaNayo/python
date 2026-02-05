import unittest
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screen import Screen
from kivy.app import App

class TestUI(unittest.TestCase):
    def setUp(self):
        Builder.load_file('src/kv/main.kv')
        Builder.load_file('src/kv/home.kv')
        Builder.load_file('src/kv/profile.kv')
        Builder.load_file('src/kv/widgets.kv')

        self.app = App.get_running_app()
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(ProfileScreen(name='profile'))
        self.sm.add_widget(ExploreScreen(name='explore'))
        self.sm.add_widget(PostDetailScreen(name='post_detail'))
        self.sm.current = 'home'

    def test_home_screen_loads(self):
        self.assertIsInstance(self.sm.current_screen, HomeScreen)

    def test_profile_screen_loads(self):
        self.sm.current = 'profile'
        self.assertIsInstance(self.sm.current_screen, ProfileScreen)

    def test_explore_screen_loads(self):
        self.sm.current = 'explore'
        self.assertIsInstance(self.sm.current_screen, ExploreScreen)

    def test_post_detail_screen_loads(self):
        self.sm.current = 'post_detail'
        self.assertIsInstance(self.sm.current_screen, PostDetailScreen)

if __name__ == '__main__':
    unittest.main()