"""
This is the main file for the neural network

--------------------------------------------------
¦ Author: Morgan Allen                           ¦
¦Project: A-Level Project                        ¦
--------------------------------------------------

Notes
-----
This is gonna take a while
"""

#imports
from decorators import *
import numpy as np
from network import *
import pickle

#object definitions

#functions
def save_network(net):
    with open(f'{net.name}Network.pickle', 'wb') as f:
        pickle.dump(net, f)
        f.close()

@timer
def load_network(name):
    with open(f'{name}Network.pickle', 'rb') as f:
        net = pickle.load(f)
        f.close()
    return net

@timer
def house_case_train(inp, desired):
    case = True
    for i in range(len(inp)-1):
        if (i+1)*200000 >= desired and (i)*200000 < desired:
            yield 1.0
            case = False
        else:
            yield 0.0

    if case:
        yield 1.0
    else:
        yield 0.0

#main program
if __name__ == "__main__":
    net = load_network("HousePrice")
    net.feed_forward([2,3,4,3000,4,8])
    net.train("TrainingData.pickle", house_case_train)
    out = list(house_case_train([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 7893450))