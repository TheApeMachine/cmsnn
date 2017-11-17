import numpy as np
from weight import Weight

class Neuron:

    def __init__(self):
        self.rest      = -70.6
        self.threshold = -60.0
        self.peak      = 40.0
        self.voltage   = self.rest
        self.s_channel = 1.0
        self.p_channel = 40.0
        self.feedback  = 1.0
        self.fired     = False
        self.weights   = []
        self.memories  = []
        self.plots     = []

    def build(self, weight_count):
        for _ in xrange(weight_count):
            self.weights.append(Weight().build())

        return self

    def get_memory(self):
        if len(self.memories) > 0:
            return self.memories.pop(0)['memory']
        else:
            return 0.0

    def set_memory(self, memory):
        try:
            match = (item for item in self.memories if item["memory"] == memory).next()
            match['weight'].value += 0.01
        except StopIteration:
            self.memories.append({
                'memory': memory,
                'weight': Weight().build()
            })

    def clamp_voltage(self, n):
        return max(self.rest, min(n, self.peak))

    def process(self, voltage=0.0, memory=0.0):
        # Neuron is in a firing state.
        if self.fired is True:
            # Neuron has peaked, it should revert back to resting state.
            if self.voltage > self.rest:
                self.p_channel -= self.feedback
                self.voltage   -= self.p_channel

            # Neuron is back at resting state.
            else:
                self.fired     = False
                self.p_channel = 40.0

        # Neuron is not firing.
        else:
            # Neuron has not reached threshold voltage yet.
            if self.voltage < self.threshold:
                self.voltage += (voltage + self.get_memory() + memory) * (1.0 + sum(item.value for item in self.weights))

            # Neuron is passed the threshold and sodium channels
            # are open and generating a peak.
            elif self.voltage < self.peak:
                self.s_channel += self.feedback
                self.voltage   += self.s_channel

            # Neuron has peaked and should fire.
            else:
                self.fired     = True
                self.s_channel = 1.0

        # Clamp the coltage between its resting and peaking state.
        self.voltage = self.clamp_voltage(self.voltage)

        # Store the short-term memory.
        if voltage > 0.0:
            if memory is 0.0:
                memory = voltage

            self.set_memory(memory)

        print memory

        # Store for plotting this neuron later.
        self.plots.append(self.voltage)
