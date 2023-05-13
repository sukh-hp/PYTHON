def factorial(x):
    fac = 1
    for i in range(x):
        fac = fac * (i + 1)
    return fac


def factorial_rec(x):
    if x == 1:
        return 1
    else:
        return x * factorial_rec(x-1)


x = int(input('Enter a number')) # type: ignore

print("Factorial of the given number is", factorial(x))
print("Factorial of the given number with rec is", factorial_rec(x))
