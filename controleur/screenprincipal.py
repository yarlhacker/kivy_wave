from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleview import RecycleView
from kivy.properties import ListProperty
from kivy.lang import Builder

Builder.load_file("view/screenprincipal.kv")


class BoxLayoutEx(BoxLayout):
    list_item = ListProperty([])

    def on_parent(self, *_):
        self.list_item = [
            {
                'id': 5
            },
            {
                'id': 5
            },
            {
                'id': 5
            },
            {
                'id': 5
            },
            {
                'id': 5
            },
            {
                'id': 5
            },
            {
                'id': 5
            },
            {
                'id': 5
            },
            {
                'id': 5
            },
            {
                'id': 5
            },
            {
                'id': 5
            },
            {
                'id': 5
            },
            {
                'id': 5
            },
            {
                'id': 5
            },
            {
                'id': 5
            },
        ]
