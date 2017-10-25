def problem6():
    def sum_of_squares(number):
        result = 0
        for square in range(number):
            result += (square + 1) * (square + 1)
        return result

    def square_of_sums(number):
        result = 0
        for square in range(number):
            result += (square + 1)
        return result * result

    print(square_of_sums(100) - sum_of_squares(100))


if __name__ == '__main__':
    problem6()
