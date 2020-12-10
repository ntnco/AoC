from aoc_2020 import get_input

inp = get_input(3).split('\n')
print(len(inp))


def count_trees(for_x, for_y):
    w = len(inp[0])
    x = 0
    y = 0
    
    num_trees = 0
    while y < len(inp):
        cur_car = inp[y][x] 
        x = (x + for_x) % w
        y += for_y
        if cur_car == '#':
            num_trees += 1
    
    return num_trees

tree_counts = []


tree_counts.append(count_trees(1,1))
tree_counts.append(count_trees(3,1))
tree_counts.append(count_trees(5,1))
tree_counts.append(count_trees(7,1))
tree_counts.append(count_trees(1,2))

res = 1
for c in tree_counts:
    res *= c

print(res)
