#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, dict = [], {'(': ')', '[': ']', '{': '}'}
        for parentheses in s:
            if parentheses in dict:       # 若dict有左括號，stack
                stack.append(parentheses)
            elif not stack:               # 若stack為空，return False
                return False
            elif dict[stack.pop()] != parentheses:  # 若找不到右括號
                return False                        # return False
        return not stack
    
    
if __name__ == "__main__":
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("()[{]}()[]{}"))
