num1 = input('1st number\n')
num2 = input('2nd number\n')

try:
    print('The sum of the numbers is', int(num1)+ int(num2))
except Exception as e:
    print(e)

print('important')