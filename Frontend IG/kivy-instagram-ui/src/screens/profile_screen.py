from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button

class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # User Info Section
        self.user_info = GridLayout(cols=1, size_hint_y=None)
        self.user_info.bind(minimum_height=self.user_info.setter('height'))

        self.username_label = Label(text='Username', font_size=24, bold=True)
        self.bio_label = Label(text='This is the user bio.', size_hint_y=None, height=40)

        self.user_info.add_widget(self.username_label)
        self.user_info.add_widget(self.bio_label)

        self.layout.add_widget(self.user_info)

        # User Posts Section
        self.posts_label = Label(text='User Posts', font_size=20, size_hint_y=None, height=40)
        self.layout.add_widget(self.posts_label)

        # Placeholder for user posts
        self.posts_layout = GridLayout(cols=3, size_hint_y=None)
        self.posts_layout.bind(minimum_height=self.posts_layout.setter('height'))

        for i in range(6):  # Placeholder for 6 posts
            post_image = Image(source='path/to/post_image.png', size_hint=(None, None), size=(100, 100))
            self.posts_layout.add_widget(post_image)

        self.layout.add_widget(self.posts_layout)

        # Add a button to edit profile
        self.edit_button = Button(text='Edit Profile', size_hint_y=None, height=50)
        self.layout.add_widget(self.edit_button)

        self.add_widget(self.layout)