import click
from parser import Parser

class Trainer:

    def __init__(self, data):
        self.data = data

    def train_sentence(self, network, sentence):
        input_count = len(network.layers[0].neurons)
        state       = []
        memories    = []

        # Process the input layers, injecting them with the data that was given to
        # the network.
        data_frame = list(sentence)

        for df in xrange(len(data_frame)):
            network.layers[0].neurons[df % input_count].process(voltage=ord(data_frame[df]) / 10.0, memory=0.0)

        for li in xrange(len(network.layers)):
            if li + 1 < len(network.layers):
                for ni in network.layers[li + 1].neurons:
                    for vi in network.layers[li].neurons:
                        # Process the current neuron in the current layer.
                        memory = vi.memories[0]['memory']

                        ni.process(vi.voltage, memory)

                        # Append the state and the strongest short-term memory for
                        # incorporation into the long-term memory.
                        if len(ni.memories) > 0:
                            state.append(ni.voltage)
                            memories.append(ni.memories[0]['memory'])

        return state, memories

    def run(self, network, epochs=100):
        print 'TRAINING NETWORK...'

        with click.progressbar(xrange(epochs)) as bar:
            for i in bar:
                for data in self.data:
                    data = data.split(' ')

                    for di in xrange(len(data)):
                        state, memories = self.train_sentence(network, data[di])

                    if len(memories) > 0:
                        try:
                            # See if this state was already stored in the long-term memory
                            # and, if so, overwrite the current memory value with the new one.
                            match = (item for item in network.memories if item["state"] == state).next()
                            match['memory'] = memories
                        except StopIteration:
                            try:
                                # See if this memory was already stored in the long-term memory
                                # and, if so, overwrite with the current state with the new one.
                                match = (item for item in network.memories if item["memory"] == memories).next()
                                match['state'] = network.hash(state)
                            except StopIteration:
                                # The memory was not stored in the long-term memory yet by either state
                                # or content, so make a new long-term memory.
                                network.memories.append({
                                    'state':  network.hash(state),
                                    'memory': memories
                                })

        print "TRAINING COMPLETED!\n"
