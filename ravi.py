# a=input("enter the character:")
# if(a==a.upper()):
#     print("charater is uppercase")
# else:
#     print("character is lower case")


mat1=[[1,2],[2,3]]
mat2=[[2,3],[1,2]]
result=[[0,0],[0,0]]
for i in range(len(mat1)):
    for j in range(len(mat2)):
        for k in range(len):
            result[i][j]+=mat1[i][k]*mat2[k][j]
for r in result:
    print(r)



