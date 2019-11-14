f = open('xyz.txt','r')
x = int(input("Enter Number : "))
l = f.readlines()
c = len(l)
f.seek(0)
for i in range(c-x):
    f.readline()
for i in range(x):
    print(f.readline())
f.close()