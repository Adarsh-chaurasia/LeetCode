nums=[10,20,30,5,10,50]
sum_=nums[0]
for i in range(1,len(nums)-1):
    if nums[i]<nums[i+1]:
        sum_+=nums[i+1]
    else:
        sum_=nums[i+1]
                
print(sum_)
