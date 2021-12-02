depths = list((int(x) for x in open("input.txt", "r").readlines()))


def part1(data):
    '''

    :param data: list of integers
    :return: number of times the value increased from one list item to the next
    '''
    return sum((1 for ind in range(1, len(data)) if data[ind] > data[ind-1]))


def part2(data):
    '''

    :param data: list of integers
    :return: the number of times the average value of 3 consecutive list items increases
    '''
    return sum((1 for ind in range(1, len(data) - 2)
                if (data[ind] + data[ind + 1] + data[ind + 2]) > (data[ind - 1] + data[ind] + data[ind + 1])))


print(part1(depths))
print(part2(depths))