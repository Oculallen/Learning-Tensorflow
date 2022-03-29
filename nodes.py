from decorators import *
import time
import numpy as np
import math
import random as rnd

class Node:
    """
    This is the base node class for a neural network

    Properties
    ----------
    value : float
        Contains the current value of the node pre or post activation
    links[] : list<Point>
        Contains the x - y coordinates of the destination nodes
    bias : float 
        Contains the inherent bias attached to the node used in the activation

    Methods
    -------
    activate()
        Returns the activated function of the current value stored in the node
    clear()
        clears the value of the property value

    Notes
    -----
    Maybe want to do away with the object later on and go for a numpy array?
    """

    def __init__(self, b, layer, width):
        self.value = 0.0
        self.links = [NodeLink(x, layer+1) for x in range(0, width)]
        self.bias = b

    def activate(self):
        self.value = 1 / (1 + math.exp(-self.value))

    def clear(self):
        self.value = 0.0

class OutNode(Node):
    def __init__(self, b):
        self.value = 0.0
        self.bias = b
        self.links = []

class NodeLink:
    """
    Link to another node
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.weight = (rnd.random() * 2)-1