# var1 = 6
# var2 = 89
# var3 = int(input())
# if var3 > var2:
#     print("Greater")
# elif var3==var2:
#     print("Equal")
# else:
#     print("Lesser");
"""list1 = [1, 2, 3, 4]
if 5 in list1:
    print("Yes")
else:
    print("No")
if 438 not in list1:
    print("Hurray")
"""
print("Enter Your age:")
age: int = int(input())

if age < 7:
    print("You are too short")
elif age > 60:
    print("You are too old")
elif age < 18:
    print("No")
elif age == 18:
    print("We cannot decide")
else:
    print('Yes')
