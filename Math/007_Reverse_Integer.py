#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = (x>0)-(x<0)
        x = sign * int(str(abs(x))[::-1])
        x = 0 if abs(x) > 0x7FFFFFFF else x
        
        return x

if __name__ == "__main__":
    print (Solution().reverse(123))
    print (Solution().reverse(-123))
    print (Solution().reverse(120))
