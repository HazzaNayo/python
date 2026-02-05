"""Instagram-like UI (no backend) using Kivy.

Single-file app that shows:
- Top bar (logo + actions)
- Horizontal stories row (scrollable)
- A few feed posts with placeholder colors/images and action buttons
- Bottom navigation bar

Run with: python main.py
"""
import sys
try:
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.gridlayout import GridLayout
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.uix.image import Image
    from kivy.uix.scrollview import ScrollView
    from kivy.uix.widget import Widget
    from kivy.core.window import Window
    from kivy.metrics import dp
    from kivy.lang import Builder
except Exception as e:
    sys.stderr.write("Kivy import failed: {}\n".format(e))
    sys.stderr.write("Please install Kivy (see requirements.txt) and ensure proper backend on Windows.\n")
    sys.exit(1)

# set a reasonable window size for desktop preview
Window.size = (360, 720)

KV = '''
<StoryBubble@BoxLayout>:
    size_hint: None, None
    size: dp(72), dp(96)
    orientation: 'vertical'
    padding: dp(6)

    canvas.before:
        Color:
            rgba: root.bg_color
        Ellipse:
            size: dp(56), dp(56)
            pos: self.x + dp(8), self.y + dp(28)

    Widget:

<PostCard@BoxLayout>:
    orientation: 'vertical'
    size_hint_y: None
    height: self.minimum_height
    padding: dp(8)
    spacing: dp(6)

    BoxLayout:
        size_hint_y: None
        height: dp(48)
        spacing: dp(8)
        Image:
            source: root.avatar_source
            size_hint: None, None
            size: dp(40), dp(40)
        Label:
            text: root.username
            valign: 'middle'
            halign: 'left'

    Image:
        source: root.image_source
        size_hint_y: None
        height: dp(300)
        allow_stretch: True
        keep_ratio: False

    BoxLayout:
        size_hint_y: None
        height: dp(40)
        spacing: dp(8)
        Button:
            text: '\u2661'
            size_hint_x: None
            width: dp(48)
        Button:
            text: '\u2709'
            size_hint_x: None
            width: dp(48)
        Button:
            text: '\u21aa'
            size_hint_x: None
            width: dp(48)

    Label:
        text: root.caption
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None

BoxLayout:
    orientation: 'vertical'

    # Top bar
    BoxLayout:
        size_hint_y: None
        height: dp(56)
        padding: dp(8)
        spacing: dp(8)
        canvas.before:
            Color:
                rgba: 1,1,1,1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: '[b]InstaClone[/b]'
            markup: True
            halign: 'left'
            valign: 'middle'
        BoxLayout:
            size_hint_x: None
            width: dp(120)
            spacing: dp(8)
            Button:
                text: 'TV'
            Button:
                text: '+'

    # Stories
    ScrollView:
        size_hint_y: None
        height: dp(110)
        do_scroll_y: False
        do_scroll_x: True

        GridLayout:
            id: stories_layout
            cols: 1
            size_hint_x: None
            width: self.minimum_width
            height: dp(110)
            row_default_height: dp(96)
            row_force_default: True
            spacing: dp(8)
            padding: dp(8)

    # Feed
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
        GridLayout:
            id: feed_layout
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            row_default_height: 'auto'
            spacing: dp(8)
            padding: dp(8)

    # Bottom nav
    BoxLayout:
        size_hint_y: None
        height: dp(56)
        spacing: dp(8)
        padding: dp(8)
        canvas.before:
            Color:
                rgba: .95, .95, .95, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Button:
            text: 'Home'
        Button:
            text: 'Search'
        Button:
            text: 'Reels'
        Button:
            text: 'Shop'
        Button:
            text: 'Profile'
'''

class InstagramApp(App):
    def build(self):
        root = Builder.load_string(KV)
        # populate stories
        stories = [
            {'bg_color': (1, .4, .4, 1), 'label': 'Your Story'},
            {'bg_color': (.6, .9, .6, 1), 'label': 'friend1'},
            {'bg_color': (.6, .6, .9, 1), 'label': 'travel'},
            {'bg_color': (.9, .6, .9, 1), 'label': 'food'},
            {'bg_color': (.9, .8, .6, 1), 'label': 'work'},
        ]

        stories_layout = root.ids.stories_layout
        for s in stories:
            w = Builder.template('StoryBubble') if False else None
            # We can't easily instantiate the template above directly, so create a BoxLayout manually
            item = BoxLayout(orientation='vertical', size_hint=(None, None), size=(dp(72), dp(96)), padding=dp(6))
            # draw colored circle using canvas on a Widget
            circle = Widget(size_hint=(None, None), size=(dp(56), dp(56)))
            with circle.canvas.before:
                from kivy.graphics import Color, Ellipse
                Color(*s['bg_color'])
                Ellipse(size=(dp(56), dp(56)), pos=(0, dp(28)))
            lbl = Label(text=s['label'], size_hint_y=None, height=dp(28), halign='center')
            lbl.text_size = (dp(72), None)
            item.add_widget(circle)
            item.add_widget(lbl)
            stories_layout.add_widget(item)

        # populate feed
        feed_layout = root.ids.feed_layout
        sample_posts = [
            {'username': 'alice', 'avatar_source': '', 'image_source': '', 'caption': 'Sunset at the beach'},
            {'username': 'bob', 'avatar_source': '', 'image_source': '', 'caption': 'Morning coffee vibes'},
            {'username': 'carol', 'avatar_source': '', 'image_source': '', 'caption': 'Hiking today!'},
        ]

        for p in sample_posts:
            card = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(420), padding=dp(8), spacing=dp(6))
            # header
            header = BoxLayout(size_hint_y=None, height=dp(48), spacing=dp(8))
            avatar = Widget(size_hint=(None, None), size=(dp(40), dp(40)))
            with avatar.canvas.before:
                from kivy.graphics import Color, Ellipse
                Color(.7, .7, .7, 1)
                Ellipse(size=(dp(40), dp(40)), pos=(0,0))
            header.add_widget(avatar)
            header.add_widget(Label(text=p['username'], valign='middle', halign='left'))
            card.add_widget(header)

            # image placeholder
            img = Widget(size_hint_y=None, height=dp(300))
            with img.canvas.before:
                from kivy.graphics import Color, Rectangle
                Color(.85, .85, .9, 1)
                Rectangle(pos=img.pos, size=img.size)
            # Because pos/size may change, bind to update
            def _update_rect(instance, value, rect_params=(img,)):
                # rebuild rectangle to the widget's area
                img.canvas.before.clear()
                from kivy.graphics import Color, Rectangle
                Color(.85, .85, .9, 1)
                Rectangle(pos=img.pos, size=img.size)

            img.bind(pos=_update_rect, size=_update_rect)
            card.add_widget(img)

            # actions
            actions = BoxLayout(size_hint_y=None, height=dp(40), spacing=dp(8))
            actions.add_widget(Button(text='\u2661', size_hint_x=None, width=dp(48)))
            actions.add_widget(Button(text='\u2709', size_hint_x=None, width=dp(48)))
            actions.add_widget(Button(text='\u21aa', size_hint_x=None, width=dp(48)))
            card.add_widget(actions)

            # caption
            caption = Label(text=p['caption'], size_hint_y=None, height=dp(40), text_size=(Window.width - dp(32), None))
            card.add_widget(caption)

            feed_layout.add_widget(card)

        return root


if __name__ == '__main__':
    InstagramApp().run()