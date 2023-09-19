import numpy as np

n=int(input("Nhap n: "))
m=int(input("Nhap m: "))
a=np.zeros((n,m))
b=np.zeros((n))


for i in range(n):
    for j in range(m):
        a[i,j]=float(input(f"a{i+1},{j+1}: "))
for i in range(n):
    b[i] = float(input(f"b{i + 1}: "))



a1=np.linalg.inv(a)
x=np.dot(a1,b)

print(x)



