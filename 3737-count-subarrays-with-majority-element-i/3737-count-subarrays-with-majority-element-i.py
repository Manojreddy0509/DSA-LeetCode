class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        s=0
        for i in range(n):
            c=0
            for j in range(i,n):
                if nums[j]==target:
                    c+=1
                m=j-i+1
                if c>m//2:
                    s+=1
        return s
                

        