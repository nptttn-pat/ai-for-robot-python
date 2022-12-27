print("Number: ",end='')
x = input()
F = [0,1]

print(1)
for i in range(1,int(x),1):
    Fn = F[0]+F[1]
    print(Fn)
    F[0] = F[1]
    F[1] = Fn
