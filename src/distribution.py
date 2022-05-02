import numpy as np
from abc import abstractmethod

class Distribution(object):

    def __init__(self, size: int):
        self.size = size

    @abstractmethod
    def make_data(self):
        ...
        #raise NotImplemented("Implement this for a specific distribution")


class NormalDistribution(Distribution):

    def __init__(self, size: int):
        super(NormalDistribution, self).__init__(size)

    def make_data(self, size):
        np.normal
