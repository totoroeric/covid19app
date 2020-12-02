from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from kivy.uix.button import ButtonBehavior, Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, CardTransition
from kivy.config import Config

Config.set('graphics','width','960')
Config.set('graphics','height','720')
Config.set('graphics','borderless','1')
Config.write()
# 上述设置窗口大小和边框

class DashboardScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class LabelButton(ButtonBehavior, Label):
    pass

class Spacer(Label):
    pass

GUI = Builder.load_file("main.kv")
# 载入主界面定义文件

class MainApp(App):

    def build(self):
        return GUI

    def on_start(self):
        LabelBase.register(name= 'myriad_pro_reg', fn_regular='MYRIADPRO-REGULAR.OTF')
        LabelBase.register(name= 'd_din_reg', fn_regular='D-DIN.otf')
        LabelBase.register(name= 'roboto_medium', fn_regular='Roboto-Medium.ttf')
        LabelBase.register(name= 'roboto_thin', fn_regular='Roboto-Thin.ttf')
        LabelBase.register(name= 'bistecca', fn_regular='Bistecca.ttf')
        LabelBase.register(name= 'teko_reg', fn_regular='Teko-Regular.ttf')
        LabelBase.register(name= 'barlow_medium', fn_regular='BarlowCondensed-Medium.ttf')
        LabelBase.register(name= 'barlow_bold', fn_regular='BarlowCondensed-SemiBold.ttf')




    def close(self):
        quit()

    def minimize(self):
        Window.minimize()

MainApp().run()   






