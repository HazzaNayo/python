from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class StoryWidget(BoxLayout):
    def __init__(self, stories, **kwargs):
        super(StoryWidget, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = '100dp'

        scroll_view = ScrollView(do_scroll_x=True, do_scroll_y=False)
        grid_layout = GridLayout(cols=len(stories), size_hint_x=None, width=len(stories) * 100)

        for story in stories:
            story_item = BoxLayout(orientation='vertical', size_hint_x=None, width='100dp')
            story_image = Image(source=story['image'], size_hint=(1, 0.8))
            story_label = Label(text=story['username'], size_hint=(1, 0.2))

            story_item.add_widget(story_image)
            story_item.add_widget(story_label)
            grid_layout.add_widget(story_item)

        scroll_view.add_widget(grid_layout)
        self.add_widget(scroll_view)