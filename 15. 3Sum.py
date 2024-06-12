# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ret = []
#         for i in range(len(nums)-2):
#             for j in range(i+1,len(nums)-1):
#                 for k in range(j+1,len(nums)):
#                     if nums[i]+nums[j]+nums[k]==0:
#                         if nums[i]==0 and nums[j]==0 and nums[k]==0:
#                             if [0,0,0] not in ret:
#                                 ret.append([nums[i],nums[j],nums[k]])
#                         if len(ret)>0:
#                             found = False
#                             for gg in ret:
#                                 if nums[i] in gg and nums[j] in gg and nums[k] in gg:
#                                     found = True
#                                     break
#                             if not found:
#                                 print("ins", [nums[i],nums[j],nums[k]])
#                                 ret.append([nums[i],nums[j],nums[k]])
#                         else:
#                             print("out", [nums[i],nums[j],nums[k]])
#                             ret.append([nums[i],nums[j],nums[k]])
                            
#         return ret

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            j=i+1
            k=len(nums)-1
            while(j<k):
                currsum = nums[j] + nums[k]
                if currsum==target:
                    ret.append([nums[i], nums[j], nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1    
                elif currsum> target:
                    k-=1
                else:
                    j+=1


        return ret

        