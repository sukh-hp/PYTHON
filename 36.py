def func1(a, b, c, d, e):
    print(a, b, c, d, e)


def func2(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(key, value)


func1('Sukh', 'Anshu', 'Prabh', 'Vishwas', 'Akash')
normal = 'This is normal'
lis = ['Sukh', 'Anshu', 'Prabh', 'Vishwas', 'Akash']
dd = {'Sukh':'SS', 'Prabh':'PM', 'Anshu':'AK'}
func2(normal, *lis, **dd)