# Print numbers from 1 to n without the help of loops. You only need to complete the function printNos() that takes N as parameter and prints number from 1 to N recursively.

# Don't print newline, it will be added by the driver code.

# Examples

# Input: n = 10
# Output: 1 2 3 4 5 6 7 8 9 10

# https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-1-to-n-without-using-loops


class Solution:    
    #Complete this function
    def printNos(self,N):
        if(N>0):
            self.printNos(N-1)
            print(N,end = " ")
            
        #Your code here

