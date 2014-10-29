from Interval import Interval
import math

even_interval_factor = math.pow(2,(1/12))

class EvenTemperedInterval(Interval):
    def __init__(self, base_fq, interval):
        super(EvenTemperedInterval, self).__init__(base_fq,interval)
        self.final_frequency = self.get_final_frequency()
        self.cents = self.interval_number_unsorted * 100

    def __repr__(self):
        return '{}: {}, {} '.format(self.__class__.__name__, self.interval_number_unsorted,self.final_frequency)

    def get_final_frequency(self):
        multiply = math.pow(even_interval_factor,self.interval_number_unsorted)
        return round(float(self.base_fq * multiply),2)



