#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        ## BRUTE FORCE
    #     # code here 
    #     lcm = 0
    #     hcf = 1
        
    #     for i in range(min(A, B), 0, -1):
    #         if(i%A==0) and (i%B==0):
    #             hcf = i
    #             break
        
        
    #     lcm = A*B//hcf
            
    #     return (lcm,hcf)

        # Calculate GCD using the Euclidean algorithm
      def gcd(x, y):
          while y:
              x, y = y, x % y
          return x
      
      # Calculate GCD of a and b
      hcf = gcd(A, B)
      
      # Calculate LCM using the relationship LCM(a, b) = (a * b) // GCD(a, b)
      lcm = (A * B) // hcf
      
      return [lcm, hcf]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends