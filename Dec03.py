filein = open("binaries.txt", "r").readlines()
binaries = list(x.strip() for x in filein)


def bitmax(List, bit):
    """

    :param List: takes a list of strings
    :param bit: an index in the string
    :return: most common character at that index in each string
    """
    number = {"1": 0, "0": 0}
    bits = list((item[bit] for item in List))
    number["1"] = bits.count("1")
    number["0"] = bits.count("0")
    return max(number, key=number.get)


def gamma(List):
    return "".join(bitmax(List, ind) for ind in range(len(List[0])))


def epsilon(rate):
    return "".join(list(("1" if x == "0" else "0" for x in rate)))


g = gamma(binaries)
e = epsilon(g)
Part01 = int(g, 2)*int(e, 2)

print(Part01)


def whittle(List, minmax):
    bits = len(List[0])
    for ind in range(bits):
        if len(List) > 1:
            maxval = bitmax(List, ind)
            if minmax == "max":
                List = list(x for x in List if x[ind] == maxval)
            else:
                List = list(x for x in List if x[ind] != maxval)
        else:
            break
    return List[0]


oxy = int(whittle(binaries, "max"), 2)
CO2 = int(whittle(binaries, "min"), 2)
Part02 = oxy * CO2

print(Part02)
