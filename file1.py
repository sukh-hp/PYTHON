# number_value= int(input('How Much?--->'))
def lister(a):
    s = 2
    listee ={1}
    while (True):
        if max(listee)<a:
            listee.add(s)
            s = s +1
            continue
        elif max(listee)>=a:
            break
    listeeee = list(listee)
    # print(listeeee)
    return listeeee
# print(lister(number_value))