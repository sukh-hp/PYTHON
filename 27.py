# L = 10  # Global Variable


# # noinspection PyShadowingNames
# def function1(n):
#     L = 5
#     print(L, n, 'I have Printed')


# print(L)
# function1('This is me')



# L = 10  # Global Variable

# def function1(n):
#     global L
#     L+=50
#     print(L, n, 'I have Printed')


# print(L)
# function1('This is me')

x = 34

def sukh():
    x = 20
    def anshu():
        global x
        x = 30
    print('Before calling anshu', x)
    anshu()
    print('After calling anshu', x)
    anshu()
sukh()
print(x)