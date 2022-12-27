def fibonacci_generator(n):
  if n <= 0:
    return
  elif n == 1:
    yield 1
  elif n == 2:
    yield 1
    yield 1
  else:
    a, b = 1, 1
    yield a
    yield b
    for i in range(2, n):
      a, b = b, a + b
      yield b

num = int(input('Number: '))
for x in fibonacci_generator(num):
  print(x)
