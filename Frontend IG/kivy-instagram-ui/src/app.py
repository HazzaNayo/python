from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class MainApp(App):
    def build(self):
        self.title = "Kivy Instagram UI"
        sm = ScreenManager()
        # Here you would add your screens to the ScreenManager
        # sm.add_widget(HomeScreen(name='home'))
        # sm.add_widget(ProfileScreen(name='profile'))
        # sm.add_widget(ExploreScreen(name='explore'))
        # sm.add_widget(PostDetailScreen(name='post_detail'))
        return sm

if __name__ == '__main__':
    MainApp().run()