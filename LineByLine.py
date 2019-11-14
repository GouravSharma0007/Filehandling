f = open('xyz.txt','r')
n = f.readlines()
print(n)
for i in n:
    print(i)
f.close()