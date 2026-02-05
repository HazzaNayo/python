from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class NavBar(BoxLayout):
    def __init__(self, **kwargs):
        super(NavBar, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        
        # Create buttons for navigation
        home_button = Button(text='Home')
        profile_button = Button(text='Profile')
        explore_button = Button(text='Explore')
        
        # Add buttons to the navigation bar
        self.add_widget(home_button)
        self.add_widget(profile_button)
        self.add_widget(explore_button)
        
        # Add a label for the app title
        title_label = Label(text='Instagram Clone', size_hint_x=None, width=200)
        self.add_widget(title_label)