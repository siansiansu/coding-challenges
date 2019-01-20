class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse = s[::-1].split()
        return ' '.join([word[::-1] for word in reverse])

if __name__ == "__main__":   
    print(Solution().reverseWords("the sky is blue"))  
