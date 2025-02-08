import kivy
kivy.require("2.1.0")

from kivy.config import Config
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from character import *

char = Character()

class BuildScreen(GridLayout):
    def __init__(self, **kwargs):
        super(BuildScreen, self).__init__(**kwargs)


class BuildApp(App):
    def build(self):
        self.title = 'Dead Frontier Build Tool'
        return BuildScreen()
        

if __name__ == "__main__":
    BuildApp().run()
    print(char)