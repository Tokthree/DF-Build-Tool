from kivy.properties import NumericProperty, ObjectProperty, DictProperty, ListProperty
from kivy.uix.behaviors.codenavigation import EventDispatcher
class Profession():
    def __init__(self, name: str, stats: dict):
        self.name = name
        self.stats = stats

    def __repr__(self):
        repr_string = f'\n---Profession Stats---\n\nProfession name: {self.name}\n'
        for key in self.stats:
            repr_string += f'Bonus {key}:\n'
            for key2 in self.stats[key]:
                repr_string += f'- {key2}: {self.stats[key][key2]}\n'
            repr_string += '\n'
        
        return repr_string

class Implant():
    def __init__(self, name: str, stats: dict):
        self.name = name
        self.stats = stats

class Character(EventDispatcher):
    level = NumericProperty(1)
    required_level = NumericProperty(1)
    profession = ObjectProperty(Profession('test', {
            'stats':{
                'strength':10,
                'endurance':0,
                'agility':0,
                'accuracy':0,
                'critical':0,
                'reloading':0,
                'dexterity':0,
                'stealth':0
            },
            'proficiencies':{
                'melee':0,
                'pistols':0,
                'rifles':0,
                'shotguns':0,
                'machineguns':0,
                'explosives':0
            }
        }))
    stat_points = NumericProperty(0)
    stat_points_used = NumericProperty(0)
    proficiency_points = NumericProperty(0)
    proficiency_points_used = NumericProperty(0)
    stats = DictProperty({
            'strength':25,
            'endurance':25,
            'agility':25,
            'accuracy':25,
            'critical':25,
            'reloading':25,
            'dexterity':0,
            'stealth':0
        })
    proficiencies = DictProperty({
            'melee':5,
            'pistols':5,
            'rifles':0,
            'shotguns':0,
            'machineguns':0,
            'explosives':0
        })
    equipment = DictProperty({
            'weapon1':{'accuracy':8, 'reloading':1, 'critical':0},
            'weapon2':{'accuracy':0, 'reloading':8, 'critical':1},
            'weapon3':{'accuracy':1, 'reloading':0, 'critical':8},
            'armour':{'agility':24, 'endurance':12}
        })
    implants = ListProperty([None for _ in range(20)])
    equipment_bonus_totals = DictProperty({})
    stat_bonus_totals = DictProperty({})
    proficiency_bonus_totals = DictProperty({})
    stat_totals = DictProperty({})
    proficiency_totals = DictProperty({})
    def __init__(self):
        self.update_equipment_bonus_totals()
        self.update_statprof_bonus_totals()
        self.update_statprof_totals()

    def set_level(self, value: int):
        self.level = value
        if value <= 50:
            self.stat_points = 5 * (value - 1)
            self.proficiency_points = 5 * (value - 1)
        elif value <= 220:
            self.stat_points = 245 + (value - 50)
            self.proficiency_points = 245 + (2 * (value - 50))
        else:
            self.stat_points = 415 + (value - 220)
            self.proficiency_points = 585 + (value - 220)

    def set_profession(self, profession: Profession):
        self.profession = profession
        self.update_statprof_bonus_totals()
        self.update_statprof_totals()

    def set_stat(self, key: str, value: int):
        self.stats[key] = value
        self.stat_points_used = (value - 25)
        #self.stat_points_used = 0
        #for _key in self.stats:
            #self.stat_points_used += (self.stats[_key] - 25)
        self.update_statprof_totals()

    def set_proficiency(self, key: str, value: int):
        self.proficiencies[key] = value
        self.update_statprof_totals()

    def set_equipment(self, equipment: dict):
        self.equipment = {}
        for key in equipment:
            self.equipment[key] = {}
            for key2 in equipment[key]:
                self.equipment[key][key2] = equipment[key][key2]

        self.update_equipment_bonus_totals()
        self.update_statprof_bonus_totals()
        self.update_statprof_totals()

    def set_implant(self, index: str, implant: Implant):
        self.implants[index] = implant

    def update_equipment_bonus_totals(self):
        self.equpment_bonus_totals = {}
        for key in self.equipment:
            for key2 in self.equipment[key]:
                if key2 not in self.equpment_bonus_totals:
                    self.equpment_bonus_totals[key2] = 0
                self.equpment_bonus_totals[key2] += self.equipment[key][key2]

    def update_statprof_bonus_totals(self):
        for key in self.stats:
            if key in self.equpment_bonus_totals:
                self.stat_bonus_totals = {**self.stat_bonus_totals, f'{key}':(self.profession.stats['stats'][key] + self.equpment_bonus_totals[key])}
            else:
                self.stat_bonus_totals = {**self.stat_bonus_totals, f'{key}':self.profession.stats['stats'][key]}
        for key in self.proficiencies:
            self.proficiency_bonus_totals = {**self.proficiency_bonus_totals, f'{key}':self.profession.stats['proficiencies'][key]}

    def update_statprof_totals(self):
        for key in self.stats:
            self.stat_totals = {**self.stat_totals, f'{key}':(self.stats[key] + self.stat_bonus_totals[key])}
        for key in self.proficiencies:
            self.proficiency_totals = {**self.proficiency_totals, f'{key}':(self.proficiencies[key] + self.proficiency_bonus_totals[key])}

    def __repr__(self):
        repr_string = f'---Basic Stats---\n\nLevel: {self.level}\nStat points: {self.stat_points}\nProficiency points: {self.proficiency_points}\n\n\n---Allocated stats---\n\n'
        for key in self.stats:
            repr_string += f'- {key}: {self.stats[key]}\n'

        repr_string += f'\n\n---Allocated proficiencies---\n\n'
        for key in self.proficiencies:
            repr_string += f'- {key}: {self.proficiencies[key]}\n'
        
        repr_string += f'\n\n---Equipment Bonuses---\n\n'
        for key in self.equipment:
            repr_string += f'{key}:\n'
            for key2 in self.equipment[key]:
                repr_string += f'- {key2}: {self.equipment[key][key2]}\n'
            repr_string += f'\n'

        repr_string += f'\n---Profession Stats---\n\nProfession name: {self.profession.name}\n'
        for key in self.profession.stats:
            repr_string += f'Bonus {key}:\n'
            for key2 in self.profession.stats[key]:
                repr_string += f'- {key2}: {self.profession.stats[key][key2]}\n'
            repr_string += '\n'

        repr_string += f'\n---Equipment Bonus Totals---\n\n'
        for key in self.equpment_bonus_totals:
            repr_string += f'- {key}: {self.equpment_bonus_totals[key]}\n'

        repr_string += f'\n\n---Bonus Totals---\n\n'
        for key in self.statprof_bonus_totals:
            repr_string += f'Bonus {key}:\n'
            for key2 in self.statprof_bonus_totals[key]:
                repr_string += f'- {key2}: {self.statprof_bonus_totals[key][key2]}\n'
            repr_string += '\n'

        repr_string += f'\n---Stat Totals---\n\n'
        for key in self.statprof_totals:
            repr_string += f'{key}:\n'
            for key2 in self.statprof_totals[key]:
                repr_string += f'- {key2}: {self.statprof_totals[key][key2]}\n'
            repr_string += '\n'


        return repr_string