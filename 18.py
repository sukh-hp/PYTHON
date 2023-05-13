a = 4
b = 6
c = sum((a, b))
print(c)


def fun1():
    print('Hello')


print(fun1())
fun1()


def function1(a, b):
    print("Hello", a + b)


print(function1)
function1(5, 7)


def func1(a, b):
    average = (a+b)/2
    print(average)


func1(a, b)
func1(5, 7)


def func2(a, b):
    """This is for average"""
    average = (a+b)/2
    # print(average)
    return average


v = func2(34, 12)
print(v)

print(func2.__doc__)
