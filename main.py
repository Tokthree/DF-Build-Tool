import kivy
kivy.require("2.1.0")

from kivy.config import Config
Config.set('graphics', 'width', '1550')
Config.set('graphics', 'height', '872')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import os
import sys
import json
import pyperclip
from plyer import filechooser
from datetime import datetime

from character import Character
from style import Style

def resource_path(relative):
        try:
            base_path = sys._MEIPASS
        except:
            base_path = os.path.abspath('.')
        return os.path.join(base_path, relative)

class BuildScreen(BoxLayout):
    character = Character()
    style = Style()

    def __init__(self, **kwargs):
        super(BuildScreen, self).__init__(**kwargs)
        with open(resource_path('data/professionData.json')) as f:
            self.professionData = json.load(f)
            f.close()
        self.populate_select()

    def populate_select(self):
        for key in self.professionData:
            self.ids.pSelect.values.append(key)

    def profession_select(self):
        element = self.ids.pSelect
        self.character.set_profession(element.text, self.professionData[element.text]['stats'], self.professionData[element.text]['proficiencies'])

    def level_input(self, action: str):
        element = self.ids.lInput
        if action == 'input':
            if element.text:
                if int(element.text) > 415:
                    element.text = '415'
        else:
            if not element.text:
                element.text = '1'
            self.character.set_level(int(element.text))

    def set_label_color(self, source):
        if source == 'stats':
            element = self.ids.sPointsLabel
            if self.character.stat_points_used > self.character.stat_points:
                element.color = [1,0,0,1]
            elif self.character.stat_points_used < self.character.stat_points:
                element.color = [1,1,0,1]
            else:
                element.color = [0,1,0,1]
        elif source == 'proficiencies':
            element = self.ids.pPointsLabel
            if self.character.proficiency_points_used > self.character.proficiency_points:
                element.color = [1,0,0,1]
            elif self.character.proficiency_points_used < self.character.proficiency_points:
                element.color = [1,1,0,1]
            else:
                element.color = [0,1,0,1]
        else:
            element = self.ids.reqLevel
            if self.character.required_level > 415:
                element.color = [1,0,0,1]
            else:
                element.color = [1,1,1,1]

    def button_manager(self, action, target = None):
        match action:
            case 'copy':
                pyperclip.copy(self.character)
            case 'open':
                self.load_data()
            case 'save':
                self.save_data()
            case 'reset':
                match target:
                    case 'stats':
                        self.reset_stats()
                    case 'equipment':
                        self.reset_equipment()
                    case 'all':
                        self.reset_stats()
                        self.reset_equipment()

    def load_data(self):
        fpath = filechooser.open_file(title='Pick a JSON file...', filters=[('*.json')])
        if not fpath:
            return

        try:
            with open(fpath[0], 'r') as f:
                fdata = json.load(f)

                for key in fdata['stats']:
                    self.ids[key].value = fdata['stats'][key]
                for key in fdata['proficiencies']:
                    self.ids[key].value = fdata['proficiencies'][key]
                for key in fdata['equipment']:
                    id = ''
                    match key:
                        case 'weapon1':
                            id = 'w1'
                        case 'weapon2':
                            id = 'w2'
                        case 'weapon3':
                            id = 'w3'
                        case 'armour':
                            id = 'a'
                    for key2 in fdata['equipment'][key]:
                        self.ids[f'{id}{str.capitalize(key2)}'].value = fdata['equipment'][key][key2]
                self.ids.pSelect.text = fdata['profession_name']
                self.ids.lInput.text = str(fdata['level'])
                self.level_input('validate')
        except OSError:
            print('Could not open/read file: ', fpath[0])
            return

    def save_data(self):
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))
        now = datetime.now()
        fname = os.path.join(application_path, f'saved builds/saved_build_{now.strftime("%d-%m-%Y_%H-%M-%S")}.json')
        fdata = self.character.toJSON()

        os.makedirs(os.path.dirname(fname), exist_ok=True)

        try:
            with open(fname, 'x') as f:
                f.write(fdata)
        except FileExistsError:
            print(f'File already exists: {fname}')
            return

    def reset_stats(self):
        self.ids.pSelect.text = 'Production / Roleplay'
        self.ids.lInput.text = '1'
        for key in self.ids:
            if key in self.character.stats or key in self.character.proficiencies:
                self.ids[key].value = self.ids[key].min
        self.level_input('validate')

    def reset_equipment(self):
        for key in self.ids:
            if 'w1' in key or 'w2' in key or 'w3' in key:
                self.ids[key].value = 0
        self.ids.aEndurance.value = 0
        self.ids.aAgility.value = 0

class BuildApp(App):
    def build(self):
        self.title = 'Dead Frontier Build Tool'
        self.icon = resource_path('app.ico')
        return BuildScreen()


if __name__ == "__main__":
    BuildApp().run()