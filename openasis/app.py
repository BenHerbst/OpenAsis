import kivy
from kivy.app import App
from kivy.uix.label import Label

class OpenAsis(App):
    def build(self):
        return Label(text="Hello World")
