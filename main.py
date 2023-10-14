from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.graphics import Color, Rectangle

from Scraper.api_handler import get_guardian, get_bing, get_openai

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.input_box = TextInput(hint_text='Search for:', multiline=False, size_hint=(1, 0.1))
        self.input_box.bind(on_text_validate=self.on_enter)
        
        self.output_label = Label(size_hint=(1, 0.8), halign='left', valign='top')
        # self.output_label.bind(size=self.resize_text)
        
        with self.output_label.canvas.before:
            Color(rgba=(0, 0, 0, 0))  # sets color to transparent
            self.rect = Rectangle(size=self.output_label.size, pos=self.output_label.pos)
        
        # self.output_label.bind(size=self.update_rect, pos=self.update_rect)
        
        self.video = Video(source='your_animation.mp4', play=True)
        
        self.layout.add_widget(self.input_box)
        self.layout.add_widget(self.output_label)
        self.layout.add_widget(self.video)
        
        return self.layout

    def on_enter(self, instance):
        query = self.input_box.text
        headlines = self.get_headlines(query)
        response = self.get_ai_response(headlines)
        self.output_label.text = response

    def get_headlines(self, query):
        return get_guardian(query)

    def list_to_string(self, headlines):
        headlines_string = ""
        for headline in headlines:
            headlines_string += "* " + headline + "\n"
        return headlines_string

    def get_ai_response(self, headlines):
        headlines = self.list_to_string(headlines)
        boilerplate = (
            "This is a list of recent headlines about a specific company, please analyze them and give me advice on "
            "whether it is currently safe to invest in this company based on its media coverage.\n{headlines}\n"
            "Be professional and concise, keep your answers to one or two paragraphs."
        ).format(headlines=headlines)
        response = get_openai(boilerplate)
        return response

if __name__ == '__main__':
    MyApp().run()
