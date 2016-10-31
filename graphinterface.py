from graphnode import GraphNode
from graphedge import GraphEdge

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


class GraphInterface(Widget):
    def __init__(self, **kwargs):
        super(GraphInterface, self).__init__(**kwargs)

        #Global variable that tracks all edges
        global edge_matrix
        edge_matrix = []

        #Global variable that tracks all nodes
        global node_matrix
        node_matrix = []

        self.graph = Graph()

    def createNode(self, instance):
        global node_matrix

        '''Creating a GraphNode Class.'''
        node = GraphNode(pos = (400,400))

        '''Creating a Node Matrix. Will use this matrix in APP Class for future calculations'''
        node_matrix.append(node)

        '''Setting node variable to None. Probably not required; to be investigated in future'''
        node = None

        '''Adding the Widget to the drawing screen'''
        self.add_widget(node_matrix[-1])
        node_matrix[-1].text = 'Button'+ str(len(node_matrix))
        print node_matrix[-1].text

    def createEdge(self, instance):
        '''Creating a GraphEdge Class.'''

        '''Getting reference to the global node_matrix for tracking all nodes'''
        global node_matrix
        global edge_matrix


        '''Setting initial values of Node1 and Node2 to None. Not sure if required.
        To be investigated'''
        node2 = None
        node1 = None

        '''A for loop to get two nodes that are selected by double clicking. These nodes should
        have a changed colour in user interface.'''
        for i in range (0, len(node_matrix)):
            if (node_matrix[i].selected) and (node1 == None):
                node1 = node_matrix[i]
            if (node_matrix[i].selected) and (node_matrix[i] != node1):
                node2 = node_matrix[i]

        '''Creating a generic edge called 'c'. Addign that generic edge to the main game'''
        c = GraphEdge(node1, node2)
        self.add_widget(c)

        #Future - for integration with graph class

        edge_matrix.append(c)


        print node_matrix
        print 'node matrix length is ----> ', len(node_matrix)
        print 'edge matrix length is ----> ', len(edge_matrix)

        #c = None
        '''node1 = None
        node2 = None'''

        self.graph.add_edge([edge_matrix[-1].node1,edge_matrix[-1].node2])

        print self.graph
