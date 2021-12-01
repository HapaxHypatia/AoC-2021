data = open("input.txt", "r").readlines()
print(sum((1 for ind in range(1, len(data)) if int(data[ind]) > int(data[ind-1]))))
