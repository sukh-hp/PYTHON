# Faulty Calculator

a = input("Write First number\n")
b = input("Write Second Number\n")
c = input("What do you want to do?\n")

# Following calculations are faulty
if a=="45" and b=="23" and c=="*":
    print("Your answer is", "243")
elif a=="34" and b=="89" and c=='+':
    print("Your answer is", "100")

# Following calculations are not faulty
elif c == "+":
    print("Your answer is", int(a)+int(b))
elif c == "*":
    print("Your answer is", int(a)*int(b))
elif c == "/":
    print("Your answer is", int(a)/int(b))
elif c == "-":
    print("Your answer is", int(a)-int(b))
elif c=="**":
    print("Your answer is", int(a)**int(b))
elif c=="%":
    print("Your answer is", int(a)%int(b))
else:
    print("Error: Check inputs")