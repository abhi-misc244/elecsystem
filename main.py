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
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty, ObjectProperty

class MainScreen(Screen):
    mat = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        box = BoxLayout(orientation='vertical')
        label = Label(text='Drawing Screen')
        box.add_widget(label)
        self.game = GraphInterface()
        box.add_widget(self.game)

        button = Button (text = 'To Calculating Screen', size_hint=(.2,.2))
        button.bind(on_press=self.switch_screen)
        box.add_widget(button)

        node_button = Button (text = 'Create Node', size_hint=(.2,.2))
        node_button.bind(on_press=self.game.createNode)
        box.add_widget(node_button)

        edge_button = Button (text = 'Create Edge', size_hint=(.2,.2))
        edge_button.bind(on_press=self.game.createEdge)
        box.add_widget(edge_button)
        self.add_widget(box)

    def switch_screen(self, instance):
        self.parent.current = 'calculating_screen'
        mat = self.game.graph

class AnotherScreen(Screen):
    b = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(AnotherScreen, self).__init__(**kwargs)
        box = BoxLayout()
        label = Label(text='Calculating Screen')
        box.add_widget(label)
        self.add_widget(box)

        button = Button (text = 'To Main Screen', size_hint=(.2,.2))
        button.bind(on_press=self.switch_screen)
        self.add_widget(button)



    def switch_screen(self, instance):
        self.parent.current = 'drawing_screen'
        print self.b
        #self.b = self.parent.mat


class ScreenManagement(ScreenManager):
    pass

''''def updategraph(object):
    print '-------------'
    presentation.screens[1].b = presentation.screens[0].mat
''''
presentation = ScreenManager(transition=FadeTransition())
drawing_screen = MainScreen(name='drawing_screen')
calculating_screen = AnotherScreen(name = 'calculating_screen')
presentation.add_widget(drawing_screen)
presentation.add_widget(calculating_screen)

''''print presentation.screens[0].mat
print presentation.screens[1].b
presentation.screens[0].bind(mat = updategraph)
print presentation.screens[0].mat
print presentation.screens[1].b
''''

'''List all variable shared bewteen screen here.
Create ObjectProperty instances in both screens.
Use "bind" and "setter" function to link two variables in different screens'''

class MainApp(App):
    def build(self):
        #presentation.current = 'drawing_screen'
        #presentation.Screen(calculating_screen)
        return presentation

if __name__ == "__main__":
    MainApp().run()
