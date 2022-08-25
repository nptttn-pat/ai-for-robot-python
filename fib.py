inp = int(input('Input nuber: '))
print("Entered: ",inp)
x1 = 1
x2 = 1
i = 0
if inp == 1:
   print("Fibonacci sequence: ")
   print(x1)
else:
   print("Fibonacci sequence: ")
   while i < inp:
       print(x1)
       chk = x1 + x2
       x1 = x2
       x2 = chk
       i = i + 1