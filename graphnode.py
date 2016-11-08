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
from tabbedview import CustomTab

class GraphNode(Widget):
    '''The Node creating Class'''
    r = NumericProperty(1)

    def __init__(self, **kwargs):
        super(GraphNode, self).__init__(**kwargs)

        '''This creates a circle at specified position initally. The node can then be dragged to
        different position. '''

        '''Creating a label for the node represented by ellipse. Inital text will be New Node.
        Once its dragged from the original position, its name changes based on when its created'''

        '''Any change to the position of the node will trigger update_object function'''

        '''This variable is used to get connection points of the edges'''
        self.selected = 0



    def save_settings(self, instance):
        
        self.popup.dismiss()


    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos) and touch.is_triple_tap:
            print 'triple tap happended'
            box = BoxLayout(orientation='vertical')

            tab_view = CustomTab()
            box.add_widget(tab_view)



            save_settings_b = Button(text = 'Save', size_hint=(.2,.2))
            box.add_widget(save_settings_b)
            self.popup = Popup(title='Settings', content=box, size_hint=(.8,.8), auto_dismiss=False)
            self.popup.open()
            save_settings_b.bind(on_press=self.save_settings)



        elif self.collide_point(*touch.pos) and touch.is_double_tap:
            '''Colour changing effect when a node is selected'''
            self.selected = not self.selected
            if self.selected:
                self.r = 0
            elif not self.selected:
                self.r = 1

        elif self.collide_point(*touch.pos):
            '''For dragging the node to new position. Grab is a kivy function'''
            touch.grab(self)
            #print 'grabed item'

    def on_touch_move(self, touch):
        '''For dragging the node to new position. Grab is a kivy function'''
        if touch.grab_current is self:
            self.pos =  (touch.x, touch.y)


    def on_touch_up(self, touch):
        '''For dragging the node to new position. Grab is a kivy function'''
        if touch.grab_current is self:
            #print "ungrabed a button"
            touch.ungrab(self)
