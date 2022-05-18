from itertools import islice
from functools import reduce
from operator import mul

######################### Solution exercise 1 ###############################
def find_nr_of_trees(road,right=3,down=1):
    col=0
    nrOfTrees=0
    for row in islice(road.splitlines(), None, None, down):
        currentPosition= row[col % len(row)]
        col+=right;
        if (currentPosition=="#"): nrOfTrees+=1
            
    return nrOfTrees

######################## Solution exercise 2 ###############################

def test_slopes(map):
    dirs = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    counts = (find_nr_of_trees(map, r, d) for r, d in dirs)
    return reduce(mul, counts)


######################### Test ###############################

road = '''\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
'''
nrOfTrees= find_nr_of_trees(road)

assert nrOfTrees == 7

########################## Print results for part 1 #################################

with open("input") as f:
         road = f.read()

nrOfTrees= find_nr_of_trees(road)

print("Nr of trees part 1", nrOfTrees)

########################## Print results for part 2 #################################

with open("input") as f:
         road = f.read()

nrOfTrees= test_slopes(road)

print("Nr of trees part 2", nrOfTrees)