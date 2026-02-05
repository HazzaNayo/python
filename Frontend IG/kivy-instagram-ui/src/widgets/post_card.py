from kivy.uix.card import Card
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty

class PostCard(Card):
    post_image = StringProperty()
    post_caption = StringProperty()
    post_user = StringProperty()

    def __init__(self, **kwargs):
        super(PostCard, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (None, None)
        self.size = (300, 400)

        self.image = Image(source=self.post_image)
        self.caption = Label(text=self.post_caption, size_hint_y=None, height=40)
        self.user = Label(text=self.post_user, size_hint_y=None, height=30)
        self.like_button = Button(text='Like', size_hint_y=None, height=50)

        self.add_widget(self.image)
        self.add_widget(self.caption)
        self.add_widget(self.user)
        self.add_widget(self.like_button)