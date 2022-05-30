## insert and sort
## pick one card at a time from unknown stack, and put the card to the right position into the stack which you have seen,
##one loop to iterate over the card stack which you have not seen
## onther loop to put the card to correct sorted postion


##iterate from second element because, 1st will be in the correct position as we have only seen first element
# [10,?,2,4,5] curr->3

from array import array
from this import d

import time
class Sort:
    def insertion_sort(nums):
        for i in range(1,len(nums)):
            curr = nums[i]
            j = i-1
            while(j>=0 and nums[j]>curr):
                nums[j+1] = nums[j]
                j=j-1
            nums[j+1] = curr
        return nums
    
    def bubble_sort(nums):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)-1):
                if nums[j]>nums[j+1]:
                    temp = nums[j+1]
                    nums[j+1]=nums[j]
                    nums[j]=temp
        return nums
    
    def bubble_optimize(nums):
        isSorted = True
        for i in range(0,len(nums)):
            for j in range(0,len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    temp = nums[j+1]
                    nums[j+1] =nums[j]
                    nums[j]=temp
                    isSorted = False
        if isSorted:
            return nums
        return nums


            
    


            
            


ms= Sort
start = time.time()
print(ms.bubble_optimize([400,5,3,2,1]))   
end = time.time()
print(float(end-start))      


            



            


