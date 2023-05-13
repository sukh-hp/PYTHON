# list1 = {1,2}
# s=3
# while (True):
#     if max(list1)<100:
#         list1.add(s)
#         s = s +1
#         continue
#     elif max(list1)>=100:
#         break
#
# n1 =  print(list1)

n = 20

print("Welcome to the game!\nPlease Guess a number between 0-100 in 10 lives")

lives = 10
while (True):
    print("You have", int(lives), "lives left")
    inp = int(input("Enter a number\n"))
    lives = lives - 1
    if lives == 0:
        print("Game Over")
        break
    elif inp<=25 and inp>=15 and not inp==20:
        print("Just Close")
    elif inp > n:
        print("Too High")
    elif inp < n:
        print("Too Low")
    else:
        print("Hurray! You got it.")
        if lives == 9:
            print("You get it in", 10 - lives, "Guess.")
        else:
            print("You get it in", 10 - lives, "Guesses.")
        break
    continue
