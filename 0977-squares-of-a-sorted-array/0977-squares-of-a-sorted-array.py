class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        j=n-1
        i=0
        p=n-1
        while i<=j:
            if (abs(nums[i])>abs(nums[j])):
                ans[p]=nums[i]**2
                i+=1
            else:
                ans[p]=nums[j]**2
                j-=1
            p-=1
        return ans

        
        