import click

class Dreamer:

    def __init__(self, network):
        self.network = network

    def run(self):
        print 'DREAM SEQUENCE STARTED...'

        for l in self.network.layers:
            with click.progressbar(xrange(len(l.neurons))) as bar:
                for i in bar:
                    for n in l.neurons:
                        while len(n.memories) > 0:
                            n.process(voltage=0.0)

        print "DREAM SEQUENCE COMPLETED!\n"
