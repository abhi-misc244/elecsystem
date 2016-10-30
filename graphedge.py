from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.graphics import Color, Ellipse, Line
from kivy.clock import Clock
from graphtheory import Graph
from functools import partial

class GraphEdge(Widget):
    '''The Edge creating class. This needs two nodes as inputs.'''

    def __init__(self,node1, node2, **kwargs):
        super(GraphEdge, self).__init__(**kwargs)
        self.node1 = node1
        self.node2 = node2

        '''This is the name of the edge'''
        self.text = 'Edge--'+node1.text + '-' + node2.text

        '''The points list of the edge.'''
        self.points = list(node1.center) + list(node2.center)

        '''Drawing a line between the two nodes given with class creation'''
        with self.canvas:
            Color(1,1,1)
            self.object = Line(points=self.points, width=3)

        '''Whenever anoy of the nodes position changes, this triggers update_object function'''
        self.node1.bind(pos=self.update_object)
        self.node2.bind(pos=self.update_object)

    def update_object(self, node, pos):
        '''With the bind function, this function gets the node object and the position of the node as inputself. '''

        '''Reassign the values of points to match the new position of node'''
        self.points = list(self.node1.center) + list(self.node2.center)

        '''Clear the canvas. Redraw the line between unmoved node and moved node'''
        with self.canvas:
            self.canvas.clear()
            Color(1,1,1)
            self.object= Line(points=self.points, width=3)
    pass
