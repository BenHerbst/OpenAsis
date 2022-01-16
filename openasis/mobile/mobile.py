import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import openasis.core.core as cr

class VerticalSplit(BoxLayout):
    message = ObjectProperty(None)

    def send_message_text(self):
        print(cr.take_query(self.message.text))
        self.message.text = ""

class OpenasisApp(App):
    def build(self):
        return VerticalSplit()
