list1 = {1,2}
s=3
while (True):
    if max(list1)<100:
        list1.add(s)
        s = s +1
        continue
    elif max(list1)>=100:
        break