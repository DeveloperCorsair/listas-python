#Exercício C

res = []
for i in range(1067, 3627):
    if i % 2 == 0:
        while i % 7 == 0:            
            res.append(i)
            break
print(len(res))