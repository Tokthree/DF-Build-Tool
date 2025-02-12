from kivy.uix.behaviors.codenavigation import EventDispatcher

class Style(EventDispatcher):
    pos_float_center = {'center_x': .5, 'top': 1}
    pos_float_left = {'x': 0.005, 'top': 1}
    pos_float_left_nogap = {'x': 0, 'top': 1}
    pos_float_right = {'right': 0.995, 'top': 1}
    pos_float_right_nogap = {'right': 1, 'top': 1}