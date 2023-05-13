l1 = ['Bhindi', 'Aloo', 'Choclate','Limca']

# i = 1

# for item in l1:
#     if i%2 != 0:
#         print(f'Jagge {item} Khareed Lavi.')
#     i += 1

for index, item in enumerate(l1):
    if index%2==0:
         print(f'Jagge {item} Khareed Lavi.')