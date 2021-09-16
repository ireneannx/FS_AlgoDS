# factorial function using loop
import time

ans_loop = 1
ans_recursion = 1


def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = i * factorial

    return factorial


# factorial using recursion
def better_factorial(num):
    if num == 0:
        return 1
    else:
        return num * (better_factorial(num - 1))


ans_loop = factorial(5)
ans_recursion = better_factorial(5)

print(ans_recursion)
