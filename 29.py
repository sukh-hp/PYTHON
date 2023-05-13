def fibonacci(a):
    if a == 1:
        return 0
    elif a == 2:
        return 1
    else:
        return fibonacci(a-1)+fibonacci(a-2)

a = int(input('Which Number do you want?\n'))
print(fibonacci(a))