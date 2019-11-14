f = open('xyz.txt','r')
n = int(input("Enter The Number:"))
for i in range(n):
    print(f.readline())
f.close()