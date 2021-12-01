depths = open("input.txt", "r").readlines()

def part1(depths):
    return sum((1 for ind in range(1, len(depths)) if int(depths[ind]) > int(depths[ind-1])))

def part2(depths):
    sum((1 for ind in range(1, len(data) - 2) if
         (depths[ind] + depths[ind + 1] + depths[ind + 2]) > (depths[ind - 1] + depths[ind] + depths[ind + 1])))