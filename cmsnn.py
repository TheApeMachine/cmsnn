#!/usr/bin/python

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

from network import Network
from trainer import Trainer
from dreamer import Dreamer

def main():
    data = [
        'the quick brown fox jumped over the lazy dog'
    ]

    network = Network({
        'layers': [
            {'neurons': 1},
            {'neurons': 1}
        ]
    }, 1).build()

    trainer = Trainer(data)
    trainer.run(network, 10)

    cap = cv2.VideoCapture(0)

    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    # dreamer = Dreamer(network)
    # dreamer.run()

    # plots = network.layers[1].neurons[0].plots
    #
    # plt.plot(plots)
    # plt.show()

    # while True:
    #     raw = raw_input('>')
    #     state, memories = trainer.train_sentence(network, raw)
    #
    #     result = ''
    #
    #     for m in memories:
    #         result.join(str(unichr(int(m * 10))))
    #
    #     print result

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print "CMSNN v0.1b\n"
    main()
