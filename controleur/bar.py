from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from kivy.lang import Builder

Builder.load_file("view/bar.kv")


class Menu_Bar(BoxLayout):
    title = StringProperty()