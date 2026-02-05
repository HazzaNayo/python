from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        txt = Label(text='This is a label')
        btn = Button(text='This is a button')
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout
    
app = MyApp()
app.run()
