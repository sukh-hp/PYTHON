def getdate():
    import datetime
    return datetime.datetime.now()


a = getdate()
print(type(a))


def repeat():
    print('Welcome to the Sukh Health Management System\nWhose Exercise or Diet You want to Know?')
    while True:
        print(a, 'Enter 1 for Sukh 2 for Prabh 3 for Anshu')
        b = int(input())
        if b != 1 and b != 2 and b != 3:
            print('Error:Check your inputs ')
            continue
        else:
            break

    while True:
        print("Do You want to Read or add?\nEnter 1 for Read and 2 for Write")
        c = int(input())
        if c != 1 and c != 2:
            print('Error: Check your inputs!')
            continue
        else:
            break
    while True:
        if c == 1:
            print('What do You Want to Read\nEnter 1 for Food and 2 for Exercise')
            read_first = int(input())
            break
        elif c == 2:
            print('What do You Want to Write\nEnter 1 for Food and 2 for Exercise')
            write_first = int(input())
            break
        else:
            print('Check Your Inputs')
            continue

    if b == 1 and c == 1 and read_first == 1:
        with open('Sukh-Food.txt') as f:
            v = f.read()
            print(v)
    elif b == 1 and c == 1 and read_first == 2:
        with open('Sukh-ex.txt') as f:
            v = f.read()
            print(v)
    elif b == 2 and c == 1 and read_first == 1:
        with open('Prabh-Food.txt') as f:
            v = f.read()
            print(v)
    elif b == 2 and c == 1 and read_first == 2:
        with open('Prabh-ex.txt') as f:
            v = f.read()
            print(v)
    elif b == 3 and c == 1 and read_first == 1:
        with open('Anshu-Food.txt') as f:
            v = f.read()
            print(v)
    elif b == 3 and c == 1 and read_first == 2:
        with open('Anshu-ex.txt') as f:
            v = f.read()
        print(v)

    elif int(b) == 1 and int(c) == 2 and int(write_first) == 1:
        with open('Sukh-Food.txt', 'a') as f:
            g: str = input('What you have consumed today?')
            f.write(g)  # type: ignore
            f.write('\n')
    elif int(b) == 1 and int(c) == 2 and int(write_first) == 2:
        with open('Sukh-ex.txt', 'a') as f:
            g: str = input('What you have done today?')
            f.write(g)  # type: ignore
            f.write('\n')
    elif int(b) == 2 and int(c) == 2 and int(write_first) == 1:
        with open('Prabh-Food.txt', 'a') as f:
            g: str = input('What you have consumed today?')
            f.write(g)  # type: ignore
            f.write('\n')
    elif int(b) == 2 and int(c) == 2 and int(write_first) == 2:
        with open('Prabh-ex.txt', 'a') as f:
            g: str = input('What you have done today?')
            f.write(g)  # type: ignore
            f.write('\n')
    elif int(b) == 3 and int(c) == 2 and int(write_first) == 1:
        with open('Anshu-Food.txt', 'a') as f:
            g: str = input('What you have consumed today?')
            f.write(g)  # type: ignore
            f.write('\n')
    elif int(b) == 3 and int(c) == 2 and int(write_first) == 2:
        with open('Anshu-ex.txt', 'a') as f:
            g: str = input('What you have done today?')
            f.write(g)  # type: ignore
            f.write('\n')
    guess = input('Do you want more to read or Write?Y or N')
    if guess.upper() == "Y":
        repeat()
    elif guess.upper() == "N":
        exit()


repeat()
