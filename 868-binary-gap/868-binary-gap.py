class Solution:
    def binaryGap(self, n: int) -> int:
        N=bin(n)[2:]
        if(N.count('1'))==1:
            return 0
        b=0
        maxb=0
        for k in N:
            if int(k)==0:
                b+=1
            elif int(k)==1:
                maxb=max(b,maxb)
                b=0
        return maxb+1