"""
Problem 14:
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time


def iter_seq(n):
    iterator = n
    iter_list = []
    while iterator != 1:
        iter_list.append(int(iterator))
        if iterator % 2 == 0:
            iterator /= 2
        else:
            iterator = 3 * iterator + 1
    iter_list.append(int(iterator))
    return iter_list


def max_iseq(n):
    i = n
    max_value = 0
    max_index = 0
    while i > 0:
        iter_value = len(iter_seq(i))
        if iter_value > max_value:
            print('setting new max index: ', i)
            max_value = iter_value
            max_index = i
        i -= 1
    return max_index


def main():
    s = time.time()
    print('index of largest chain: ', max_iseq(1000000))
    print('time taken: ', time.time() - s)


if __name__ == '__main__':
    main()
