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
    character = Character()

    def __init__(self, **kwargs):
        super(BuildScreen, self).__init__(**kwargs)
        with open('./data/professionData.json') as f:
            self.professionData = json.load(f)
        self.populate_select()

    def populate_select(self):
        for key in self.professionData:
            self.ids.professionSelect.values.append(key)
    
    def profession_select(self):
        element = self.ids.professionSelect
        self.character.set_profession(Profession(element.text, self.professionData[element.text]))

    def level_input(self, action: str):
        element = self.ids.levelInput
        if action == 'input':
            if element.text:
                if int(element.text) > 415:
                    element.text = '415'
        else:
            if not element.text:
                element.text = '1'
            self.character.set_level(int(element.text))


class BuildApp(App):
    def build(self):
        self.title = 'Dead Frontier Build Tool'
        return BuildScreen()
        

if __name__ == "__main__":
    BuildApp().run()
    #print(char)