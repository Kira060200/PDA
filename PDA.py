f = open('date.in')
matrix = [[['`' for x in range(200)] for y in range(200)] for k in range(200)]
ini = 0
fin = 0
start = int(f.readline()) #starea initiala
final = []    #starile finale
for x in f.readline().split():
    final.append(int(x))
#print(start, final)
for x in f.readlines():
    if len(x.split()) == 2:
        ini = int(x.split()[0])
        fin = int(x.split()[1])
        #print(ini, fin)
    else:
        matrix[ini][(int(x.split(' ', 1)[0]) if x.split(' ', 1)[0] < 'a' else ord(x.split(' ', 1)[0]))][int(x.split(' ', 2)[1]) if x.split(' ', 2)[1] < 'a' else ord(x.split(' ', 2)[1])] = (x.split(' ', 2)[2].replace('\n', '')+' '+str(fin))
        #print((x.split(' ', 1)[1].replace('\n', '')+' '+str(fin)))
word = input('Enter word: ')


def check():
    stack = ['z']
    current = start
    for x in word:
        popped = stack.pop()
        if matrix[int(current)][int(x) if x < 'a' else ord(x)][int(popped) if popped < 'a' else ord(popped)] != '`':
            temp = ""
            for i in matrix[int(current)][int(x) if x < 'a' else ord(x)][int(popped) if popped < 'a' else ord(popped)].split()[0]:
                temp = i + temp
            for y in temp:
                if y!='e':
                    stack.append(y)
            #print(stack)
            current = matrix[int(current)][int(x) if x < 'a' else ord(x)][int(popped) if popped < 'a' else ord(popped)].split()[1]
            #print(int(current))
        else:
            return False
    if (current in final) and (len(stack) == 1) and (stack[0] == 'z'):
        return True
    if len(stack) == 1:
        popped = stack.pop()
        if (matrix[int(current)][ord('e')][int(popped) if popped < 'a' else ord(popped)].split()[1] in final) or (int(matrix[int(current)][ord('e')][int(popped) if popped < 'a' else ord(popped)].split()[1]) in final):
            return True
    return False


print(check())

