def problem2():
  def fibonacci(n):
    if n == 1:
      return 1
    elif n == 2:
      return 2
    else:
      return fibonacci(n-1) + fibonacci(n-2)
  
  i = 1
  result = 0
  while fibonacci(i) < 4000000:
    if fibonacci(i) % 2 == 0:
      result += fibonacci(i)
    i += 1
  print(result)

if __name__ == '__main__':
  problem2()