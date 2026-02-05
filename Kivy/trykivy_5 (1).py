# dual screen program
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
# A screen (an object of the Screen class) is a layout widget (Screen is a descendant of the RelativeLayout class).
# ScreenManager is a special widget that makes one of the screens specified in it visible.

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # the name of the screen must be passed to the constructor of the Screen class
        btn = Button(text="Switch to another screen")
        btn.on_press = self.next
        self.add_widget(btn) # screen is a widget on which all others (descendants) can be created

    def next(self):
        self.manager.transition.direction = 'left' # the Screen object has a "manager" property
                                                   # - is a link to the parent
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = Button(text="Come back, come back!")
        btn.on_press = self.next
        self.add_widget(btn)
        
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        # FirstScr will be shown because it was added first. This can be changed like this:
        # sm.current = 'second'
        return sm

app = MyApp()
app.run()