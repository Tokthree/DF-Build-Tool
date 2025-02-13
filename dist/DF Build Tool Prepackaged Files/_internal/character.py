from kivy.properties import NumericProperty, DictProperty, StringProperty
from kivy.uix.behaviors.codenavigation import EventDispatcher

class Implant():
    def __init__(self, name: str, stats: dict):
        self.name = name
        self.stats = stats

class Character(EventDispatcher):
    level = NumericProperty(1)
    required_level = NumericProperty(1)
    profession_name = StringProperty('Production / Roleplay')
    profession_stats = DictProperty({
        'strength':0,
        'endurance':0,
        'agility':0,
        'accuracy':0,
        'critical':0,
        'reloading':0,
        'dexterity':0,
        'stealth':0
    })
    profession_proficiencies = DictProperty({
        'melee':0,
        'pistols':0,
        'rifles':0,
        'shotguns':0,
        'machineguns':0,
        'explosives':0
    })
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
            'weapon1':{'accuracy':0, 'reloading':0, 'critical':0},
            'weapon2':{'accuracy':0, 'reloading':0, 'critical':0},
            'weapon3':{'accuracy':0, 'reloading':0, 'critical':0},
            'armour':{'agility':0, 'endurance':0}
        })
    equipment_bonus_totals = DictProperty({})
    stat_totals = DictProperty({})

    def __init__(self):
        self.update()

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

    def set_profession(self, name: str, stats: dict, proficiencies: dict):
        self.profession_name = name
        self.profession_stats = stats
        self.profession_proficiencies = proficiencies
        self.update()

    def set_stat(self, key: str, value: int):
        self.stats[key] = int(value)
        self.update()

    def set_proficiency(self, key: str, value: int):
        self.proficiencies[key] = int(value)
        self.update()

    def set_equipment(self, slot: str, key: str, value: int):
        self.equipment[slot] = {**self.equipment[slot], f'{key}':value}
        self.update()

    def update_equipment_bonus_totals(self):
        equipment_bonus_totals_temp = {}
        for key in self.equipment:
            for key2 in self.stats:
                if key2 not in equipment_bonus_totals_temp:
                    equipment_bonus_totals_temp[key2] = 0
                if key2 in self.equipment[key]:
                    equipment_bonus_totals_temp[key2] += self.equipment[key][key2]
        self.equipment_bonus_totals = equipment_bonus_totals_temp

    def update_stat_totals(self):
        for key in self.stats:
            if key in self.equipment_bonus_totals:
                self.stat_totals = {**self.stat_totals, f'{key}':(self.stats[key] + self.equipment_bonus_totals[key])}
            else:
                self.stat_totals = {**self.stat_totals, f'{key}':self.stats[key]}

    def update_point_allocation(self):
        self.stat_points_used = 0
        required_level_stats = 0
        self.proficiency_points_used = 0
        required_level_proficiencies = 0

        for key in self.stats:
            if key == 'dexterity' or key == 'stealth':
                self.stat_points_used += self.stats[key] - self.profession_stats[key]
            else:
                self.stat_points_used += self.stats[key] - (25 + self.profession_stats[key])

        if self.stat_points_used <= 245:
            required_level_stats = (self.stat_points_used / 5) + 1
        else:
            required_level_stats = 50 + (self.stat_points_used - 245)

        for key in self.proficiencies:
            if key == 'melee' or key == 'pistols':
                self.proficiency_points_used += self.proficiencies[key] - (5 + self.profession_proficiencies[key])
            else:
                self.proficiency_points_used += self.proficiencies[key] - self.profession_proficiencies[key]

        if self.proficiency_points_used <= 245:
            required_level_proficiencies = (self.proficiency_points_used / 5) + 1
        elif self.proficiency_points_used <= 585:
            required_level_proficiencies = 50 + ((self.proficiency_points_used - 245) / 2)
        else:
            required_level_proficiencies = 220 + (self.proficiency_points_used - 585)

        if required_level_stats > required_level_proficiencies:
            self.required_level = required_level_stats
        else:
            self.required_level = required_level_proficiencies

    def update(self):
        self.update_equipment_bonus_totals()
        self.update_stat_totals()
        self.update_point_allocation()

    def toJSON(self):
        json_string = f'{{"level": {self.level},"profession_name": "{self.profession_name}","stats": {self.stats},"proficiencies": {self.proficiencies},"equipment": {self.equipment}}}'.replace("'", '"')
        return json_string

    def __repr__(self):
        repr_string = f'---Basic Stats---\n\nLevel: {self.level}\nRequired level: {self.required_level}\nStat points: {self.stat_points}\nStat points allocated: {self.stat_points_used}\nProficiency points: {self.proficiency_points}\nProficiency points allocated: {self.proficiency_points_used}\n\n\n---Allocated stats---\n\n'
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

        repr_string += f'\n---Profession Stats---\n\nProfession name: {self.profession_name}\n\nBonus stats:\n'
        for key in self.profession_stats:
            repr_string += f'- {key}: {self.profession_stats[key]}\n'
        repr_string += '\n'
        for key in self.profession_proficiencies:
            repr_string += f'- {key}: {self.profession_proficiencies[key]}\n'
        repr_string += '\n'

        repr_string += f'\n---Equipment Bonus Totals---\n\n'
        for key in self.equipment_bonus_totals:
            repr_string += f'- {key}: {self.equipment_bonus_totals[key]}\n'

        repr_string += f'\n\n---Stat Totals---\n\nStats:\n'
        for key in self.stat_totals:
            repr_string += f'- {key}: {self.stat_totals[key]}\n'
        repr_string += '\nProficiencies:\n'
        for key in self.proficiencies:
            repr_string += f'- {key}: {self.proficiencies[key]}\n'

        return repr_string