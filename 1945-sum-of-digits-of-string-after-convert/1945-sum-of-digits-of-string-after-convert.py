import string
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        pos=[string.ascii_lowercase.index(list(s)[i])+1 for i in range(len(list(s)))]
        pos_string=''.join(map(str,pos))
        for i in range(k):
            pos_string = str(sum(map(int, pos_string)))
        return pos_string