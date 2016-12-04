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

        self.total_nodes = 0

        #Global variable that tracks all nodes
        global node_matrix
        node_matrix = []

        self.graph = Graph()

    def createNode(self, instance):
        global node_matrix
        self.total_nodes = self.total_nodes + 1
        var = self.total_nodes
        '''Creating a GraphNode Class.'''
        node = GraphNode(pos = (400,400), node_id = var)

        '''Creating a Node Matrix. Will use this matrix in APP Class for future calculations'''
        node_matrix.append(node)

        '''Adding the Widget to the drawing screen'''
        self.add_widget(node_matrix[-1])
        #node_matrix[-1].text = node.text
        #print node_matrix[-1].text

    def createEdge(self, instance):
        '''Creating a GraphEdge Class.'''

        '''Getting reference to the global node_matrix for tracking all nodes'''
        global node_matrix
        global edge_matrix


        '''Setting initial values of Node1 and Node2 to None.'''
        node2 = None
        node1 = None

        '''A for loop to get two nodes that are selected by double clicking. These nodes should have a changed colour in user interface.'''
        for i in range (0, len(node_matrix)):
            if (node_matrix[i].selected) and (node1 == None):
                node1 = i
                #node1 = node_matrix[i]
            if (node_matrix[i].selected) and (node_matrix[i] != node1):
                node2 = i
                #node2 = node_matrix[i]

        '''Creating a generic edge called 'c'. Addign that generic edge to the main game'''
        edge_list = [node_matrix[node1], node_matrix[node2]]
        theline = GraphEdge(edge_list)
        self.add_widget(theline)

        #Future - for integration with graph class

        edge_matrix.append(theline)


        #print node_matrix
        #print 'node matrix length is ----> ', len(node_matrix)
        #print 'edge matrix length is ----> ', len(edge_matrix)

        #c = None


        self.graph.add_edge(theline)

        print 'the graph is---->'
        print self.graph
