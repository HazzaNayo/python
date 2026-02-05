from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class ExploreScreen(Screen):
    def __init__(self, **kwargs):
        super(ExploreScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.title_label = Label(text='Explore', font_size='24sp', size_hint_y=None, height=50)
        self.layout.add_widget(self.title_label)

        self.grid = GridLayout(cols=2, spacing=10, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        for i in range(10):  # Example for adding 10 explore items
            btn = Button(text=f'Explore Item {i + 1}', size_hint_y=None, height=100)
            self.grid.add_widget(btn)

        self.layout.add_widget(self.grid)
        self.add_widget(self.layout)