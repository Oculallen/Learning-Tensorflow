from nodes import *
from decorators import *
import numpy as np
import random as rnd
import pickle
import sys
import main

def chunk(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

#@timer
class NeuralNet:
    """
    Main holder for the network


    """

    def __init__(self, name, layers):
        self.name = name
        self.net = [[Node((rnd.random() * 2)-1, i, layers[i+1]) for x in range(layers[i])] for i in range(0, layers.__len__()-1)]
        self.net.append([OutNode((rnd.random() * 2)-1) for x in range(layers[-1])])

    def get_output(self):
        return [n.value for n in self.net[-1]]

    def feed_forward(self, inp):
        for x, val in enumerate(inp):
            self.net[0][x].value = val

        for row in range(0,self.net.__len__()-1):
            for node in self.net[row]:
                node.activate()
                for link in node.links:
                    self.net[link.y][link.x].value = node.value * link.weight
                node.value = 0.0

        out = self.get_output()
        print(out)
        for x in self.net[-1]:
            x.value = 0.0
        return out

    def get_output(self):
        return [x.value for x in self.net[-1]]

    def train(self, dataName, caseFunc):
        with open(f'{dataName}', 'rb') as f:
            data = pickle.load(f)
            f.close()
        random.shuffle(data)
        trainData = list(chunk(data, 10))
        for i, val in enumerate(trainData):
            for j, dat in enumerate(val):
                inp = dat[0:-1]
                out = self.feed_forward(inp)
                case = list(caseFunc(out, dat[-1]))
                
if __name__ == "__main__":
    pass
