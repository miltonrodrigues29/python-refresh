# s=""
# dp = { len(s): 1}     
# if 1 in dp:
#     print("Yes")
# print(dp)


s="10101"
dp = {0:1,1:0,2:1,3:0,4:1,5:1}
for i in range(len(s)-1,-1,-1):
    print(i)