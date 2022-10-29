from cgitb import text
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import pywhatkit as pw
class Converter(App):
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # image widget
        self.window.add_widget(Image(source="Images/logo.png"))

        # label widget
        self.greeting = Label(
                        text= "Enter your text below!",
                        font_size= 18,
                        color= '#E45D81'
                        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5)
                    )

        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                      text= "Convert",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#00FFCE',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window
    
    def callback(self, instance):
     x = ' '
     pw.text_to_handwriting(self.user.text, "Output.png",[255,0,0])
     self.greeting.text = f"{x*12} Conversion Done! \nThanks for using the Software!"

# run Say Hello App
if __name__ == "__main__":
    Converter().run()