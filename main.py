from kivy.app import App
#kivy.require("1.8.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.label import Label
from graphnode import GraphNode
from graphedge import GraphEdge
from graphinterface import GraphInterface
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty, ObjectProperty

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        box = BoxLayout(orientation='vertical')
        label = Label(text='Drawing Screen')
        box.add_widget(label)
        self.game = GraphInterface()
        box.add_widget(self.game)

        box2 = BoxLayout(orientation='horizontal')

        button = Button (text = 'To Calculating Screen', size_hint=(.2,.2))
        button.bind(on_press=self.switch_screen)
        box2.add_widget(button)

        node_button = Button (text = 'Create Node', size_hint=(.2,.2))
        node_button.bind(on_press=self.game.createNode)
        box2.add_widget(node_button)

        edge_button = Button (text = 'Create Edge', size_hint=(.2,.2))
        edge_button.bind(on_press=self.game.createEdge)
        box2.add_widget(edge_button)

        box.add_widget(box2)
        self.add_widget(box)


    def switch_screen(self, instance):
        global mat
        self.parent.current = 'calculating_screen'
        mat = self.game.graph
        print 'this is mat---->>>', mat

class AnotherScreen(Screen):
    def __init__(self, **kwargs):
        super(AnotherScreen, self).__init__(**kwargs)
        global mat

        self.box = BoxLayout(orientation = 'vertical')
        label = Label(text='Calculating Screen')
        self.box.add_widget(label)

        self.add_widget(self.box)

        box2=BoxLayout(orientation='horizontal')

        button = Button (text = 'To Main Screen', size_hint=(.2,.2))
        button.bind(on_press=self.switch_screen)
        box2.add_widget(button)

        self.box.add_widget(box2)

    def switch_screen(self, instance):
        self.parent.current = 'drawing_screen'

class ScreenManagement(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        presentation = ScreenManager(transition=FadeTransition())
        drawing_screen = MainScreen(name='drawing_screen')
        calculating_screen = AnotherScreen(name = 'calculating_screen')
        presentation.add_widget(drawing_screen)
        presentation.add_widget(calculating_screen)
        #presentation.screens[0].bind(mat=presentation.screens[0].setter('b'))
        return presentation

if __name__ == "__main__":
    MainApp().run()
