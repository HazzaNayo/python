# event handling "clicked on the button"

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

def tst():
    print('HELLO!')

class MyApp(App):
    def build(self):
        txt = Label(text='This is a label')
        btn = Button(text='This is a button')
        btn.on_press = tst # the on_press method of the btn object becomes equal to the tst function
                           # that is, calling btn.on_press() is equivalent to calling tst()
                           # a method named on_press is called automatically when the button is clicked
                             
        layout = BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout

MyApp().run() # the program monitors the click on the button and prints the text