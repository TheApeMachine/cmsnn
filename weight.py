import numpy as np

class Weight:

    def __init__(self):
        self.value = np.random.uniform(-1.0, 1.0)

    def build(self):
        return self
