nums1=[4,2,1]
nums2=[1,3,4,2]
result=[]

for each in range(len(nums1)):
    if nums1[each] in nums2:
        index_=nums2.index(nums1[each])
        if index_==len(nums2)-1:
            result.append(-1)
        else:
            if nums2[index_]>nums2[index_+1]:
                result.append(-1)
            else:
                result.append(nums2[index_+1])


print(result)
