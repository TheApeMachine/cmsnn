from neuron import Neuron

class Layer:

    def __init__(self):
        self.neurons = []

    def build(self, neuron_count, weight_count):
        for _ in xrange(neuron_count):
            self.neurons.append(Neuron().build(weight_count))

        return self
