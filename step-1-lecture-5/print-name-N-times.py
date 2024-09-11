# https://www.geeksforgeeks.org/problems/print-gfg-n-times/

class Solution:
    def printGfg(self, n):
        # Code here
        if(n>0):
            self.printGfg(n-1)
            print("GFG", end=" ")
