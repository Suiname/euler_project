def problem4():
  def is_palindrome(number):
    num_as_str = str(number)
    last_index = len(num_as_str) - 1
    for i in range(len(num_as_str)):
      if num_as_str[i] != num_as_str[last_index - i]:
        return False
    return True

  def largest_palindrome():
    a = 999
    b = 999
    products = []
    while a != 99:
      products.append(a*b)
      if b == 100:
        a -= 1
        b = 999
      else:
        b -= 1
    for product in list(reversed(sorted(products))):
      if is_palindrome(product):
        return product
    return 0

  print(largest_palindrome())

if __name__ == '__main__':
  problem4()