class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1 or n==7:
            return True
        nst=str(n) # convert to string
        if len(nst)<2:
            return False
        l=[int(x)*int(x) for x in nst]
        if sum(l)==1:
            return True
        else:
            return self.isHappy(sum(l))