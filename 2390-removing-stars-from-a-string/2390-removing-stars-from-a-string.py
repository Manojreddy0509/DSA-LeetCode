class Solution:
    def removeStars(self, s: str) -> str:
        stk=[]
        for ch in s:
            if ch!="*":
                stk.append(ch)
            else:
                stk.pop()
        ans=""
        for ch in stk:
            ans+=ch
        return ans
        