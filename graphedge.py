from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty, StringProperty
from kivy.graphics import Color, Ellipse, Line
from kivy.clock import Clock
from graphtheory import Graph
from functools import partial
from tabbedview import CustomTab
from tabbedview import EdgeTab


class GraphEdge(Widget):
    '''The Edge creating class. This needs two nodes as inputs.'''
    points = ListProperty(None)
    edge_x = NumericProperty(50)
    edge_y = NumericProperty(50)
    edge_name = StringProperty('TBC')
    edge_cable = StringProperty('TBC')

    def __init__(self,node1, node2, **kwargs):
        super(GraphEdge, self).__init__(**kwargs)
        self.node1 = node1
        self.node2 = node2


        '''This is the name of the edge'''
        self.text = 'Edge--'+node1.text + '-' + node2.text

        '''The points list of the edge.'''
        self.points = list(node1.center) + list(node2.center)

        self.edge_x = (self.node1.x + self.node2.x)/2
        self.edge_y = (self.node1.y + self.node2.y)/2


        '''Whenever anoy of the nodes position changes, this triggers update_object function'''
        self.node1.bind(pos=self.update_object)
        self.node2.bind(pos=self.update_object)

    def update_object(self, node, pos):
        '''With the bind function, this function gets the node object and the position of the node as inputself. '''

        '''Reassign the values of points to match the new position of node'''
        self.points = list(self.node1.center) + list(self.node2.center)
        self.edge_x = (abs(self.node1.x) + abs(self.node2.x))/2
        self.edge_y = (abs(self.node1.y) + abs(self.node2.y))/2

    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos) and touch.is_triple_tap:
            box = BoxLayout(orientation='vertical')
            self.tab_view = EdgeTab()
            box.add_widget(self.tab_view)
            save_settings_b = Button(text = 'Save', size_hint=(.2,.2))
            box.add_widget(save_settings_b)
            self.popup = Popup(title='Settings', content=box, size_hint=(.8,.8), auto_dismiss=False)
            self.popup.open()
            save_settings_b.bind(on_press=self.save_settings)

    def save_settings(self, instance):
        self.edge_name = self.tab_view.ids.edge_name.text

        self.edge_name = self.edge_name + '\n' + str(self.tab_view.resistance)+' Ohms'


        self.edge_cable = self.tab_view.ids.btn_size.text +  " " +  self.tab_view.ids.btn_core.text + " " + self.tab_view.ids.btn_insulation.text
        self.popup.dismiss()
    pass
