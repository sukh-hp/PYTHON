d1 = {}
print(type(d1))
d2 = {'Sukh': "Burger", 'Anshu': "Noodles", 'Prabh': "MOMO", 'Vishwas': {"B": "Parantha", "L": "Roti", "D": "Chol"},
      'DIl': "Junk", 'Komal': "Ji"}
del d2["Komal"]
d3 = d2.copy()
print(d2)
del d3['Sukh']
print(d3)
print(d2["Sukh"])
d2.update({"LO":"SI"})
print(d2)
print(d2.keys())
print(d2.items())