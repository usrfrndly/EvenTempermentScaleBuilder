from EvenTemperedInterval import EvenTemperedInterval
from Scale import Scale

class EvenTemperedScale(Scale):
    def __init__(self, base_fq):
        super(EvenTemperedScale, self).__init__(base_fq, 13)
        # We are looking at the seven tone scale
        #self.interval_list = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.generate_even_tempered_scale()

    def generate_even_tempered_scale(self):
        for x in range(self.num_intervals):
            self.scale_intervals[x] = EvenTemperedInterval(self.base_freq,x)

    def print_even_tempered_scale(self):
        for interval in self.scale_intervals:
            print(interval)

