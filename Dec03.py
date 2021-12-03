filein = open("binaries.txt", "r").readlines()
binaries = list(x.strip() for x in filein)


def bitmax(List, bit):
    '''

    :param List: takes a list of strings
    :param bit: an index in the string
    :return: most common character at that index in each string
    '''
    number = {"0": 0, "1": 0}
    bits = list((item[bit] for item in List))
    number["0"] = bits.count("0")
    number["1"] = bits.count("1")
    return max(number, key=number.get)


def gamma(List):
    return "".join(bitmax(List, ind) for ind in range(len(List[0])))


def epsilon(rate):
    return "".join(list(("1" if x == "0" else "0" for x in rate)))


g = gamma(binaries)
e = epsilon(g)
Part01 = int(g, 2)*int(e, 2)
print(Part01)
