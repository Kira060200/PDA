f = open('date.in')
matrix = [[[['`' for x in range(200)] for y in range(20)] for z in range(200)] for k in range(20)]
ini = 0
fin = 0
start = int(f.readline()) #starea initiala
final = []    #starile finale
maxi = 0
poz = -1
for x in f.readline().split():
    final.append(int(x))
#print(start, final)
for x in f.readlines():
    if len(x.split()) == 2:
        ini = int(x.split()[0])
        fin = int(x.split()[1])
        #print(ini, fin)
        if maxi < ini:
            maxi = ini
        if maxi < fin:
            maxi=fin
    else:
        matrix[ini][(int(x.split(' ', 1)[0]) if x.split(' ', 1)[0] < 'a' else ord(x.split(' ', 1)[0]))][fin][int(x.split(' ', 2)[1]) if x.split(' ', 2)[1] < 'a' else ord(x.split(' ', 2)[1])] = x.split(' ', 2)[2].replace('\n', '')
        #print((x.split(' ', 1)[1].replace('\n', '')+' '+str(fin)))
word = input('Enter word: ')
ok = False
stack = ['z']
# def check():
#     stack = ['z']
#     current = start
#     for x in word:
#         popped = stack.pop()
#         if matrix[int(current)][int(x) if x < 'a' else ord(x)][int(popped) if popped < 'a' else ord(popped)] != '`':
#             temp = ""
#             for i in matrix[int(current)][int(x) if x < 'a' else ord(x)][int(popped) if popped < 'a' else ord(popped)].split()[0]:
#                 temp = i + temp
#             for y in temp:
#                 if y!='e':
#                     stack.append(y)
#             #print(stack)
#             current = matrix[int(current)][int(x) if x < 'a' else ord(x)][int(popped) if popped < 'a' else ord(popped)].split()[1]
#             #print(int(current))
#         else:
#             return False
#     if (current in final) and (len(stack) == 1) and (stack[0] == 'z'):
#         return True
#     if len(stack) == 1:
#         popped = stack.pop()
#         if (matrix[int(current)][ord('e')][int(popped) if popped < 'a' else ord(popped)].split()[1] in final) or (int(matrix[int(current)][ord('e')][int(popped) if popped < 'a' else ord(popped)].split()[1]) in final):
#             return True
#     return False


def DFS(x, litera):
    global ok
    global poz
    global stack
    for i in range(maxi+1):
        if litera == 0:
            stack = ['z']
        #print(litera, i, stack)
        if len(stack) > 0 and litera < len(word):
            popped = stack.pop()
            if (matrix[x][int(word[litera]) if word[litera] < 'a' else ord(word[litera])][i][int(popped) if popped < 'a' else ord(popped)] != '`') or matrix[x][ord('e')][i][int(popped) if popped < 'a' else ord(popped)] != '`':
                temp = ""
                #print(stack, end=' ')
                if matrix[x][int(word[litera]) if word[litera] < 'a' else ord(word[litera])][i][int(popped) if popped < 'a' else ord(popped)] != '`':
                    for j in matrix[x][int(word[litera]) if word[litera] < 'a' else ord(word[litera])][i][int(popped) if popped < 'a' else ord(popped)]:
                        temp = j + temp
                else:
                    for j in matrix[x][ord('e')][i][int(popped) if popped < 'a' else ord(popped)]:
                        temp = j + temp
                for y in temp:
                    if y != 'e':
                        stack.append(y)
                poz = i
                #print(temp, word[litera], poz, stack)
                DFS(i, litera+1)
            else:
                stack.append(popped)
        else:
            if poz in final and len(stack) == 1 and litera < len(word):
                ok = True
                return 0


DFS(start, 0)
print(ok)
