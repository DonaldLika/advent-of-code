import unittest
import os

######################### Solution ###############################

def findFirstCombination(totalNumbers, inputValues, summary=2020):
     if totalNumbers == 1:
        return [summary] if summary in inputValues  else None

     for n in inputValues:
        result= findFirstCombination(totalNumbers-1,inputValues,summary-n)
        if result:
            return [n,*result]

######################### Test ###############################

testinput = set(map(int, '''\
1721
979
366
299
675
1456'''.splitlines()))

a, b = findFirstCombination(2, testinput)
assert a+b == 2020, "Should be 2020"
assert a*b == 514579, "Should be 514579"

a, b, c = findFirstCombination(3, testinput)
assert a+b+c == 2020, "Should be 2020"
assert a*b*c == 241861950, "Should be 241861950"

################### Print results for part 1,2 ################
with open("input") as f:
         fileInput= set(map(int, f.readlines()))

a, b = findFirstCombination(2, fileInput)

print("2020 with 2 numbers combination {} x {}= {}".format(a,b,a*b))

a, b, c = findFirstCombination(3, fileInput)

print("2020 with 3 numbers combination {} x {} x {} = {}".format(a,b,c,a*b*c))