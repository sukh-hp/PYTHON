import time
'''
initial = time.time()

k = 0
while k<45:
    print('Sukh')
    time.sleep(2)
    k+=1

print(time.time()-initial)


initial2 = time.time()


for i in range(45):
    print('Sukh')

print(time.time()-initial2)

a = (0.41497135162353516, 0.4722263813018799)
print(a[1]-a[0]) # type: ignore
print(a)

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
'''
print(time.ctime(1682181670.3331041))

a = time.gmtime(1682181670.3331041)
for item in a:
    print(item)
gmmm = time.localtime()
# time_string = time.s  
print(time.localtime(1682181670.3331041))
print(time.strftime("%Y-%m-%d %H:%M:%S", gmmm))
# print(time.gmtime(1682181670.3331041))
