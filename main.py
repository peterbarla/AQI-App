from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
import requests
import json

class Screen(Widget):
    result_city = ObjectProperty(None)
    result_aqi = ObjectProperty(None)
    entry = ObjectProperty(None)

    def pressed(self):
        try:
            api_url = requests.get("https://api.waqi.info/feed/" + self.entry.text + "/?token=3787f1c6f54214f6d420b52e2be8e7db95a10b1d")
            api = json.loads(api_url.content)
        except Exception as e:
            api = "ERROR"
        if api['status'] == "error":
            self.result_city.text = "City not found!"
            self.result_aqi.text = ""
        else:
            self.result_city.text = self.entry.text + ": " + api['data']['city']['name']
            self.result_aqi.text = "Air quality: " + str(api['data']['aqi'])
        self.entry.text = ""

class MyApp(App):
    def build(self):
        return Screen()

if __name__ == "__main__":
    MyApp().run()
