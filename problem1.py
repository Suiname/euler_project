def problem1():

  def multiple(number):
    if number % 3 == 0 or number % 5 == 0:
      return True
    else:
      return False

  def sum_multiples(multipleList):
    result = 0
    for multiple in multipleList:
      result += multiple
    return result

  multipleList = []
  for i in range(1000):
    if multiple(i):
      multipleList.append(i)
  print(sum_multiples(multipleList))

if __name__ == '__main__':
  problem1()