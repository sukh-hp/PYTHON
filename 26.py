with open('Sukh.txt') as f:
    a =f.readlines()
    print(a)


f = open('Sukh.txt')
b = f.read(6)
print(b)
f.close()