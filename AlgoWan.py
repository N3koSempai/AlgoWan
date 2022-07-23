from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import time
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
Window.size=(300,450)



class LoginApp(MDApp):
    dialog = None

    def build(self):

        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palet = "Red"
        self.theme_cls.accent_palette = "Green"

        return Builder.load_file("Algowangui.kv")




    def login(self):
        if self.root.ids.user.text == 'admin' and self.root.ids.password.text == '123':
            if not self.dialog:
                self.dialog = MDDialog(

                    title = 'Login',
                    text = f"Bienvenido {self.root.ids.user.text}!",
                    buttons = [
                        MDFlatButton(
                        text = "Ok", text_color = self.theme_cls.accent_color

                        ),],

                )
                self.dialog.open()

    def close(self):
        self.dialog.dismiss()


if __name__ == "__main__":
    LoginApp().run()
