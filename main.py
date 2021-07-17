from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from DB import Data
from kivymd.uix.dialog import MDDialog
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu

class GIClaculator(MDApp, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('D:/Genshin Exp Calculator/venv/KV.kv')

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return self.screen

    db=Data('D:/Genshin Exp Calculator/venv/explist.csv')

class StartPage(Screen):
    pass

class Main(Screen):
    start_lvl=ObjectProperty(None)
    last_lvl = ObjectProperty(None)

    def get_all_exp(self, start_lvl, last_lvl):
        all_exp=


if __name__ == "__main__":
    GIClaculator().run()