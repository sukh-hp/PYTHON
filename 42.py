import file1
# MAP FUNCTION
# num1 = ['2','5','7']

# # for i in range(len(num1)):
# #     num1[i] = int(num1[i])

# num1 = list(map(int,num1))

# num1[2] = num1[2] + 3
# # print(num1[2])

# num2 = [1,3,5,7,9,3,6,8]

# # def sq(a):
# #     return a*a

# # square = list(map(sq,num2))
# # print(square)


# square = list(map(lambda x:x*x,num2))
# print(square)


# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# func = [square,cube]
# for i in range(5):
#     val = list(map(lambda x:x(i),func))
#     print(val)

# --------------------Filter Function----------------------

numbers = file1.lister(4)


# def is_greater_5(num):
#     return num>5

# gr_than_5 = list(filter(is_greater_5,numbers))
# print(gr_than_5)

# --------------------Reduce Function----------------------
from functools import reduce
# num = 0
# for i in numbers:
#     num = num + i
# print(num)


prod = reduce(lambda x,y:x+y,numbers)
print(prod)