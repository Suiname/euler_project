def next_prime(number):
    prime = False
    result = number + 1
    while not prime:
        for i in range(result)[2:]:
            if result % i == 0:
                result += 1
                break
            elif i == result - 1:
                prime = True
    return result


def nth_prime(n):
    first_primes = [2, 3, 5, 7, 11, 13]
    if n < 7:
        return first_primes[n-1]
    else:
        index = 6
        prime = 13
        while index < n:
            prime = next_prime(prime)
            index += 1
        return prime


def main():
    number = 10001
    print nth_prime(number)


if __name__ == '__main__':
    main()