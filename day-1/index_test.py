from index import findFirstCombination
import unittest
import os

class TestExercise(unittest.TestCase):
    
    def test_part_one_input(self):
        testinput = set(map(int, givenInputValues()))
        a, b = findFirstCombination(2, testinput)
        assert a+b == 2020, "Should be 2020"
        assert a*b == 514579, "Should be 514579"
    
    def test_part_one_file_input(self):
        testinput = set(map(int, givenFileInputValues('1st-part-data')))
        a, b = findFirstCombination(2, testinput)
        assert a+b == 2020, "Should be 2020"
        print(a*b)

    def test_part_two_input(self):
        testinput = set(map(int, givenInputValues()))
        a, b, c = findFirstCombination(3, testinput)
        assert a+b+c == 2020, "Should be 2020"
        assert a*b*c == 241861950, "Should be 241861950"

    def test_part_two_file_input(self):
        testinput = set(map(int, givenFileInputValues('2nd-part-data')))
        a, b,c = findFirstCombination(3, testinput)
        assert a+b+c == 2020, "Should be 2020"
        print(a*b*c)


def givenInputValues():
    return '''\
1721
979
366
299
675
1456'''.splitlines()

def givenFileInputValues(fileName):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    conf_path = os.path.join(dir_path,fileName)
    with open(conf_path) as f:
         return f.readlines()