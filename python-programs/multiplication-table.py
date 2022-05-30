# n = int(input("Enter the Number :"))
# d = int(input("Enter the Number of Multiplication Table :"))
# print("Multiplication table for",d)
# for i in range(1,n+1):
#     print(d, " x ",i," = ",d*i)



from itertools import count


class Multiplication:
    def table(digit,n):
        print("Multiplication table for :",digit)
        counter =1
        while counter<=n:
            print(digit," x ",counter," : ",digit*counter)
            counter = counter+1


t = Multiplication
digit = int(input("Enter the value "));
n = int(input("Table till? "))
t.table(digit,n)



