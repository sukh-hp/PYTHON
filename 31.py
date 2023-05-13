# while True:
#     a = int(input('Enter First Number'))
#     b = int(input('Enter Second Number'))

#     print(a+b)
#     c = input('Do You want any other calculation?Y or N')
#     if c.upper() == "Y":
#         continue
#     else:
#         print('Bye.....')
#         break

def sum():
    a = int(input('Enter First Number'))
    b = int(input('Enter Second Number'))

    print(a+b)
    c = input('Do You want any other calculation?Y or N')
    if c.upper()=="Y":
        sum()
    else:
        exit()
sum()