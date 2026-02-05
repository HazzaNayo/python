from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from screens.home_screen import HomeScreen
from screens.profile_screen import ProfileScreen
from screens.explore_screen import ExploreScreen
from screens.post_detail_screen import PostDetailScreen

class MyScreenManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        Builder.load_file('kv/main.kv')
        return MyScreenManager()

if __name__ == '__main__':
    MainApp().run()