"""
The function gets the remainder of the a and b, then just gets the remainder all over again
until the value of b is zero.
"""


def do_it_recursion(a, b):
    return a if b == 0 else do_it_recursion(b, a % b)

print('With Recursion', do_it_recursion(1071, 1029))  # 21


def do_it_not_recursion(a, b):
    while True:
        if b == 0:
            return a

        temp = a % b
        a = b
        b = temp

    return a


print('No recursion', do_it_not_recursion(1071, 1029))  # 21
