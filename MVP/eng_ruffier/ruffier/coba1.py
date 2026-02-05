import kivy.app as app
import kivy.uix.button as button
import kivy.uix.boxlayout as boxlayout
import kivy.uix.label as label
import kivy.uix.textinput as textinput

class MyApp(app.App):
    def build(self):
        self.layout = boxlayout.BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input = textinput.TextInput(hint_text='Enter some text', size_hint_y=None, height=40)
        self.layout.add_widget(self.input)

        self.button = button.Button(text='Submit', size_hint_y=None, height=40)
        self.button.bind(on_press=self.on_button_press)
        self.layout.add_widget(self.button)

        self.output_label = label.Label(text='Your input will appear here.', size_hint_y=None, height=40)
        self.layout.add_widget(self.output_label)

        return self.layout

    def on_button_press(self, instance):
        user_input = self.input.text
        self.output_label.text = f'You entered: {user_input}'
        


app = MyApp()
app.run()