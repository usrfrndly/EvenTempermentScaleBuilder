"""
HarmonicSeriesRow.py
Jaclyn Horowitz
Music Software Projects 2014
"""





class Interval(object):

    def __init__(self, basefrq, interval):
        self.interval_number_unsorted = int(interval)
        self.base_fq = basefrq
        self.note_number = None
        self.note_name = None
        self.final_frequency = 0

    def __repr__(self):
        return '{}: {} '.format(self.__class__.__name__,self.interval_number_unsorted)
