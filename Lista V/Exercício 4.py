#Exercício D

res = []
for i in range(18644, 33087):
    if '2' in str(i) and '7' not in str(i):
        res.append(i)
print(len(res))