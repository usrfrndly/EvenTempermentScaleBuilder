"""
Jaclyn Horowitz
Music Software Projects 2014
"""


from EvenTemperedScale import EvenTemperedScale
from PythagSeries import PythagSeries
import IntervalSpacingTest
import EvenTempermentTest

def main():
    # Change base_frequency manually
    base_frequency = 528
    print("Your base frequency is %d hertz" % base_frequency)
    even_scale = EvenTemperedScale(base_frequency)
    even_scale.print_even_tempered_scale()
    pythag_scale = PythagSeries(base_frequency)
    print(pythag_scale.get_spacing(1,3))
    print(pythag_scale.get_spacing(2,5))
    EvenTempermentTest.test_et_scale(even_scale)
    IntervalSpacingTest.test_interval_spacing(pythag_scale)

if __name__ == '__main__':
    main()


