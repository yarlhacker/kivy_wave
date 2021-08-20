from kivy.uix.screenmanager import ScreenManager 

class Screen_Wave(ScreenManager):
    
    screen_stack = []

    def push(self,name_screen):
        self.screen_stack.append(self.current)
        self.current  = name_screen
        self.transition.direction = 'left'
        
    def pop (self):
        name_screen = self.screen_stack[-1]
        del self.screen_stack[-1]
        self.current  = name_screen
        self.transition.direction = "right"