def problem5():
  def first_twenty(number):
    for i in range(20):
      if number % (i + 1) != 0:
        return False
    return True
  

  i = 20
  while not first_twenty(i):
    for j in reversed(range(20)):
      if i % (j+1) != 0:
        i *= (j+1)
        break
  reduced = False
  while not reduced:
    for j in range(20):
      if (j + 1) != 1 and i % (j + 1) == 0 and first_twenty(i / (j + 1)):
        i = int(i / (j + 1))
        break
      elif j == 19:
        reduced = True
  print(i)
  
if __name__ == '__main__':
  problem5()