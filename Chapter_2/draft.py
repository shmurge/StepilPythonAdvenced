n = int(input())
k = int(input())
j = 1

ls = []

for i in range(1, n+1):
    ls.append(i)

while len(ls) > 1:
    for i in range(len(ls)):
        if j % k == 0:
            ls[i] = 0
        j += 1

    for i in range(len(ls)):
        if 0 in ls:
            ls.remove(0)
        else:
            break

print(*ls)