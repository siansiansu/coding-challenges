class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, lookup = [], {'(': ')', '[': ']', '{': '}'}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif not stack:
                return False
            elif lookup[stack.pop()] != parenthese:
                return False
        return not stack
    
    
if __name__ == "__main__":
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("()[{]}()[]{}"))