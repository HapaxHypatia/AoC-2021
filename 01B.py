data = list((int(x) for x in open("input.txt", "r").readlines()))
print(sum((1 for ind in range(1, len(data)-2) if (data[ind] + data[ind+1] + data[ind+2]) > (data[ind-1] + data[ind] + data[ind+1]))))
