# https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/

class Solution:
    def printNos(self, n):
        # Code here
        count = n
        if(n == 0):
            return
        print(count, end = " ")
        self.printNos(n-1)