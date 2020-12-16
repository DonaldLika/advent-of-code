from itertools import islice

######################### Solution ###############################
def find_nr_of_trees(road):
    col=0
    nrOfTrees=0
    for row in islice(road.splitlines(), None, None, 1):
        currentPosition= row[col % len(row)]
        col+=3;
        if (currentPosition=="#"): nrOfTrees+=1
            
    return nrOfTrees

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

print("Nr of trees", nrOfTrees)