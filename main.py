from kivymd.app import MDApp 
from controleur.commande import Screen_Wave
from kivy.properties import ObjectProperty




class Main_Kivy(Screen_Wave):
    pass

class MainApp(MDApp):
    manager = ObjectProperty(None)
    def build(self):
        self.manager = Main_Kivy()
        return self.manager
        # return ContactLayoutEx()
MainApp().run()