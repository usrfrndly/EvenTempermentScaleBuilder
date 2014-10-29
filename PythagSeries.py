"""
PythagSeries.py
Jaclyn Horowitz
Music Software Projects 2014
"""


from Scale import Scale
from PythagSeriesInterval import PythagSeriesInterval
from fractions import gcd

'''
PythagSeries class : Represents the pythagorean series and is initialized with a base frequency.
'''



class PythagSeries(Scale):

    def __init__(self,base_fq):
        super(PythagSeries, self).__init__(base_fq, 7)
        self.interval_list = [-1, 0, 1, 2, 3, 4, 5]
        # An array that contains properties for each interval_number_unsorted in the pythag series
        self.generate_pythag_scale()

    # generate_pythag_scale(): adds information for each interval_number_unsorted in the pythagorean series to the pythag_scale_intervals array
    def generate_pythag_scale(self):
        i = 0
        for interval in self.interval_list:
            self.scale_intervals[i] =(PythagSeriesInterval(self.base_freq,interval))
            self.scale_intervals[i].set_note_name()
            i += 1
        self.scale_intervals.append(self.get_octave())


    # show_all_rows(): Prints each row in the pythagorithmic series
    def show_series_columns(self):
        print("[Interval, Numerator, Denominator, Factor,"
              " Interval Frequency, Octave, Octave Denom, Factor (Octave Adjusted), Final Frequency ]")
        for i in range(0, len(self.scale_intervals)):
            self.scale_intervals[i].show_column()

    def get_octave(self):
        octave = PythagSeriesInterval(self.base_freq,8)
        octave_freq = self.base_freq * 2
        octave.final_frequency = octave_freq
        octave.note_number = self.num_intervals
        octave.numerator = 2
        octave.new_denom = 1
        octave.set_note_name()
        return octave

    def get_next_mode(self):
        self.scale_intervals = self.sort_by_final_frequency()
        self.scale_intervals.pop(0)
        octave = self.get_octave()
        self.scale_intervals.append(octave)
        return self.scale_intervals

    def get_spacing(self,interval_number_left,interval_number_right):

        sorted_scale = self.sort_by_final_frequency()
        numerator = sorted_scale[interval_number_right-1].numerator * sorted_scale[interval_number_left-1].new_denom
        denominator = sorted_scale[interval_number_right-1].new_denom * sorted_scale[interval_number_left-1].numerator
        divide = gcd(numerator,denominator)
        reducedNumerator = str(int(numerator/divide))
        reducedDenom = str(int(denominator/divide))
        return str(reducedNumerator) + "/" + str(reducedDenom)



