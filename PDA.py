f = open('date.in')
matrix = [['0' for x in range(1000)] for y in range(1000)]
ini = 0
fin = 0
for x in f.readlines():
    if len(x.split()) == 2:
        ini = int(x.split()[0])
        fin = int(x.split()[1])
        print(ini, fin)
    else:
        matrix[ini][(int(x.split(' ', 1)[0]) if x.split(' ', 1)[0] < 'a' else ord(x.split(' ', 1)[0]))] = (x.split(' ', 1)[1].replace('\n', '')+' '+str(fin))
        print((x.split(' ', 1)[1].replace('\n', '')+' '+str(fin)))
