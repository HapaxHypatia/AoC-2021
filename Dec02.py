moves = list(x.strip("\n") for x in open("movements.txt", "r").readlines())


def part01(data):
    x = 0
    y = 0

    for item in data:
        direction = item.rstrip('0123456789').strip()
        distance = int(item[len(direction):])
        match direction:
            case "forward": x += distance
            case "up": y -= distance
            case "down": y += distance
    return x*y


def part02(data):
    x = 0
    y = 0
    aim = 0

    for item in data:
        direction = item.rstrip('0123456789').strip()
        distance = int(item[len(direction):])
        match direction:
            case "forward":
                x += distance
                y += aim*distance
            case "up":
                aim -= distance
            case "down":
                aim += distance
    return x*y


print(part01(moves))
print(part02(moves))
