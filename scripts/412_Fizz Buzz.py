class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1, n + 1):
            n = str(i)
            if i % 3 ==0 and i % 5 == 0:
                n = 'FizzBuzz'
            elif i % 3 == 0:
                n = 'Fizz'
            elif i % 5 == 0:
                n = 'Buzz'
            else:
                n = str(i) 
            ans.append(n)
        return ans
            
        
if __name__ == "__main__":    
    print(Solution().fizzBuzz(15))