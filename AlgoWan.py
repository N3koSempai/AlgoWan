from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel



class ALgoWan(MDApp):

    x = 'your balance is %s algorand' % 155
    def build(self):
        self.theme_cls.material_style = "M3"

        result= Builder.load_file('./Algowangui.kv')
        print(self.root)
        return result


ALgoWan().run()
