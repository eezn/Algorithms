# Fibonacci sequence

# O(2^n) : recursive
# O(n) : iterator
# O(1) : form (70항 이상 부정확)

import math

# O(2^n)
def find_fibonacci_seq_rec(n):
    if n < 2: return n
    return find_fibonacci_seq_rec(n - 1) + find_fibonacci_seq_rec(n - 2)

# O(n)
def find_fibonacci_seq_iter(n):
    if n < 2: return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

# O(1)
def find_fibonacci_seq_form(n):
    sq5 = math.sqrt(5)
    phi = (1 + sq5) / 2
    return int(math.floor(phi ** n / sq5))


def test_find_fib():
    n = 10
    assert(find_fibonacci_seq_rec(n) == 55)
    assert(find_fibonacci_seq_iter(n) == 55)
    assert(find_fibonacci_seq_form(n) == 55)
    print('pass')

if __name__=="__main__":
    test_find_fib()