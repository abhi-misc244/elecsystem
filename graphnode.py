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

class GraphNode(Widget):
    '''The Node creating Class'''

    def __init__(self, **kwargs):
        super(GraphNode, self).__init__(**kwargs)

        '''This creates a circle at specified position initally. The node can then be dragged to
        different position. '''
        with self.canvas:
            Color(1,1,1)
            self.object = Ellipse(pos=(400,400))

        '''Creating a label for the node represented by ellipse. Inital text will be New Node.
        Once its dragged from the original position, its name changes based on when its created'''
        self.l = Label(text='New Node', color=[1,0,1,1], size=(200,200),pos=self.pos)
        self.add_widget(self.l)
        self.text = "New Node"

        '''Any change to the position of the node will trigger update_object function'''
        self.bind(pos=self.update_object)

        '''This variable is used to get connection points of the edges'''
        self.selected = 0


    def update_object(self, *args):
        '''Ellipse position is set as widget position'''
        self.object.pos = self.pos

        '''The lable position is set as widget position'''
        self.l.pos = self.pos
        self.l.text = self.text

        '''Had to do this as label kept dissapearing whenever canvas was cleared.
        Not sure why this was happening. to be investigated'''
        self.remove_widget(self.l)
        self.add_widget(self.l)

    def save_settings(self, instance):
        self.text = self.textinput.text
        self.update_object()
        self.popup.dismiss()


    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos) and touch.is_triple_tap:
            print 'triple tap happended'
            box = BoxLayout(orientation='vertical')

            sub_box1 = BoxLayout(orientation='horizontal')
            sub_box1.add_widget(Label(text='Name'))
            self.textinput = TextInput(text = self.text, multiline = False)
            sub_box1.add_widget(self.textinput)

            box.add_widget(sub_box1)

            save_settings_b = Button(text = 'Save')
            box.add_widget(save_settings_b)
            self.popup = Popup(title='Settings', content=box, size_hint=(.3,.3), auto_dismiss=False)
            self.popup.open()
            save_settings_b.bind(on_press=self.save_settings)

            self.update_object()


        elif self.collide_point(*touch.pos) and touch.is_double_tap:
            '''Colour changing effect when a node is selected'''
            self.selected = not self.selected
            if self.selected:
                with self.canvas:
                    self.canvas.clear()
                    Color(1,0,1)
                    self.object = Ellipse(pos=(self.center))
                    self.update_object()
            elif not self.selected:
                with self.canvas:
                    self.canvas.clear()
                    Color(1,1,1)
                    self.object = Ellipse(pos=(self.center))
                    self.update_object()

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
