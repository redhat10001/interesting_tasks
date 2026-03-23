
A=[1, 2, 3, 4, 5, 6]
n=2
m=3
c=0
B=[[0]*m for i in range (n)]
for i in range (n):
         for j in range (m):
                B[i][j]=A[c]
                c+=1

print (B)
