import kivy
kivy.require("2.1.0")

from kivy.config import Config
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import json

from character import *

class BuildScreen(GridLayout):
    def __init__(self, **kwargs):
        super(BuildScreen, self).__init__(**kwargs)
        with open('./data/professionData.json') as f:
            self.professionData = json.load(f)
        self.character = Character()
        self.populate_select()

    def populate_select(self):
        for key in self.professionData:
            self.ids.professionSelect.values.append(key)
    
    def profession_select(self):
        self.character.set_profession(Profession(self.ids.professionSelect.text, self.professionData[self.ids.professionSelect.text]))


class BuildApp(App):
    def build(self):
        self.title = 'Dead Frontier Build Tool'
        return BuildScreen()
        

if __name__ == "__main__":
    BuildApp().run()
    #print(char)