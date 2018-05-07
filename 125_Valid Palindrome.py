class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = [i.lower() for i in s if i.isalnum()]
        return ss == ss[::-1]
        
     
if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))