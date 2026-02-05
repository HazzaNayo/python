from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button

class PostDetailScreen(Screen):
    def __init__(self, **kwargs):
        super(PostDetailScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Placeholder for post image
        self.post_image = Image(source='path/to/post/image.jpg', size_hint=(1, 0.7))
        self.layout.add_widget(self.post_image)

        # Placeholder for post description
        self.post_description = Label(text='Post description goes here', size_hint=(1, 0.2))
        self.layout.add_widget(self.post_description)

        # Back button
        self.back_button = Button(text='Back', size_hint=(1, 0.1))
        self.back_button.bind(on_press=self.go_back)
        self.layout.add_widget(self.back_button)

        self.add_widget(self.layout)

    def go_back(self, instance):
        self.manager.current = 'home'  # Change to the appropriate screen name