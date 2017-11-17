from collections import Counter

class Parser:

    def __init__(self):
        self.dict = []

    def tokenize(self, data):
        tokens = Counter()

        for d in data:
            for word in d[0].split(' '):
                tokens[word] += 1

        for token in tokens:
            self.dict.append(token)

    def prepare(self, data):
        self.tokenize(data)

        new_data = []

        for d in data:
            new_input = []
            new_label = []

            for word in d[0].split(' '):
                for letter in list(word):
                    new_input.append(self.dict.index(letter))

            new_data.append([new_input])

        return new_data
