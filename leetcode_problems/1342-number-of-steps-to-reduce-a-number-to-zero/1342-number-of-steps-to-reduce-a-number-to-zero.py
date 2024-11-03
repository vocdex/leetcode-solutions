class Solution:
    def numberOfSteps(self, num, steps=0):
        if not num:
            return steps
        else:
            match num % 2:
                case 0: return self.numberOfSteps(num//2, steps+1)
                case 1: return self.numberOfSteps(num-1,  steps+1)
        