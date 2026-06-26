class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #n=len(nums)
        #for i in range(n):
         #   one=nums[i]
          #  for j in range(i+1,n):
           #     two=nums[j]
            #    if one+two==target:
             #       return [i,j]
        
        n=len(nums)
        d={}
        for i in range(n):
            d[nums[i]]=i
        for i in range(n):
            tofind=target-nums[i]
            if tofind in d and d[tofind]!=i:
                return [d[tofind],i]             
        
            

        