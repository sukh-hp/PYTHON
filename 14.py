# i = 0
# while (i<20):
#     print(i, end=" ")
#     i = i+1

# while (True):
#     if i<5:
#         i = i + 1
#         continue
#     print(i, end=" ")
#     if(i==20):
#         break
#     i = i + 1

# a = int(input("Enter a number\n"))
# while (100 >= a):
#     a = int(input("Enter a number\n"))
#     if a>100:
#      print("Hurray You Have reached to 100!")
#     continue


while(True):
    inp = int(input("Enter a number\n"))
    if inp > 100:
        print("Y")
        break
    else:
        print("Try again")
        continue
