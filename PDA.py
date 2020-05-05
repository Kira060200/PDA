f = open('date.in')
matrix = [['0' for x in range(100)] for y in range(100)]
for x in f.readline().split():
    print(x, len(x))
