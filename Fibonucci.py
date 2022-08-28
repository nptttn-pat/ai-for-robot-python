input_num = int(input("Number : "))
num1 = 0
num2 = 1
fibo = 1
while fibo < input_num:
  print(fibo)
  fibo = num1 + num2
  num1 = num2
  num2 = fibo