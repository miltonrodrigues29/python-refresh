class Array:
    def get_median(nums):
        nums.sort() #nlog(n)
        if len(nums)%2 == 0:
            a = nums[int(len(nums)/2)]
            b = nums[int(len(nums)/2)-1]
            return (a+b)/2
        else:
            return nums[int(len(nums)/2)]


o = Array
print(o.get_median([1,2,3,4]))