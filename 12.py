# list1 = ["Sukh", "Anshu", "Prabh"]
# print(list1)
# for item in list1:
#     print(item)
# list2 = [["Sukh", 1], ["Anshu", 2], ["Prabh",3]]
# for item, marks in list2:
#     print(item, "had got", marks, "marks")
# dic1 = dict(list2)
# print(dic1)
# for item, marks in dic1.items():
#     print(item, "had got", marks, "marks")
# for item in dic1:
#     print(item)

list5 = [1, 34, 454, 346544, 232, 122 , 34, 2]
list5.sort()
set1 = set(list5)

for item in set1:
    if item<400:
        print(item)
