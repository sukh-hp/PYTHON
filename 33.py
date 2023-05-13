import random
from random import shuffle
list1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
         "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
list2 = ['!','@','#','$','&','?']
a = random.choices(list1, k=6)
b = random.choices(list2,k=2)
list3 = a+b
shuffle(list3)
print(list3)
print("".join(str(i) for i in list3))