# print('This program will make a star pattern for the given number\n
# If entered number is odd the pattern will be upside down \n Enter Your number ')
# a = input()
# b = int(a)
# c = b/2
# battery = 1
# e = 1
#
# if c.is_integer():
#     while 1<= b:
#         print(battery*' ',    b * '* ')
#         b-=1
#         battery+=1
#         continue
# else:
#     battery=b
#     while 1<=b:
#         print(battery*' ', e * '* ')
#         battery-=1
#         e+=1
#         if battery==0:
#             break
#         else:
#             continue
#


print('This program will make a star pattern for the given number \n Enter Your number ')
a = int(input())
print('Do You Simple Triangle Or the Inverted one : S for Simple and I for Inverted')
c = input()

b = a/2
d = 1
e = 1

if c == 'I':
    while 1 <= a:
        print(d * " ", a * '* ')
        a -= 1
        d += 1
        continue
elif c == 'S':
    d = a
    while 1 <= a:
        print(d*' ', e * '* ')
        d -= 1
        e += 1
        if d == 0:
            break
        else:
            continue
else:
    print("Error:Check Inputs again")