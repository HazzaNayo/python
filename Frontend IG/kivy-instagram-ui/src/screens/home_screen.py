from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.title_label = Label(text='Home', font_size='24sp', size_hint_y=None, height=50)
        self.layout.add_widget(self.title_label)

        self.scroll_view = ScrollView()
        self.feed_layout = GridLayout(cols=1, size_hint_y=None)
        self.feed_layout.bind(minimum_height=self.feed_layout.setter('height'))

        # Sample posts
        for i in range(10):
            post_button = Button(text=f'Post {i + 1}', size_hint_y=None, height=100)
            self.feed_layout.add_widget(post_button)

        self.scroll_view.add_widget(self.feed_layout)
        self.layout.add_widget(self.scroll_view)

        self.add_widget(self.layout)