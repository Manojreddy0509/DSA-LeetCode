class Solution:
    def average(self, salary: List[int]) -> float:
        n=len(salary)
        summ=sum(salary)
        l,s=0,float('inf')
        for num in salary:
            if num>l:
                l=num
        for num in salary:
            if num<s:
                s=num
        return ((summ-l-s)/(n-2))

        