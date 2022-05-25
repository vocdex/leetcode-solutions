import string
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        pos=[string.ascii_lowercase.index(list(s)[i])+1 for i in range(len(list(s)))]
        pos_string=''.join(map(str,pos))
        while(k!=0):
            digit=[i for i in pos_string]
            sumdigit=sum(map(int,digit))
            k=k-1
            pos_string=list(str(sumdigit))
        return sumdigit
            