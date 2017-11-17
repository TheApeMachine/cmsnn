import hashlib
from layer import Layer

class Network:

    def __init__(self, design, simulations):
        self.design      = design
        self.simulations = simulations
        self.layers      = []
        self.memories    = []
        self.concepts    = []

    def hash(self, value):
        return hashlib.md5(''.join(map(str, value))).hexdigest()

    def build(self):
        for l in xrange(len(self.design['layers'])):
            layer = self.design['layers'][l]

            if l is 0:
                weight_count = 0
            else:
                weight_count = self.design['layers'][l - 1]['neurons']

            self.layers.append(
                Layer().build(
                    layer['neurons'],
                    weight_count
                )
            )

        return self
