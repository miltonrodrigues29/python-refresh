class Array:
    def average_of_array(nums):
        total =0
        for i in nums:
            total = total+i
        
        return total/len(nums)


n = int(input("Enter the number of elements in an array :"))
nums=[]
for i in range(0,n):
    temp = int(input("Enter {0} Element :".format(i+1)))
    nums.append(temp)

t = Array
print(int(t.average_of_array(nums)))
