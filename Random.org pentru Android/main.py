import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random
kivy.require('1.9.0')

class Algorithm(BoxLayout):
    def __init__(self):
        super(Algorithm,self).__init__()

    def generate(self):
        self.used_label.text=str(random.randint(0,1000))

class Random_generate(App):
    def build(self):
        return Algorithm()

Random_genera=Random_generate()
Random_genera.run()