def problem3():
  def largest_prime(number):
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    return number
    
  print(largest_prime(600851475143))

if __name__ == '__main__':
  problem3()