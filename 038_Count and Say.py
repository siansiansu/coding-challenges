#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in range(n-1):
            new_res = ''
            pre = res[0]
            count = 0
            for j in range(len(res)):
                if res[j] == pre:
                    count += 1
                else:
                    new_res += str(count) + pre
                    count = 1
                    pre = res[j]
            res = new_res + str(count) + pre
        return res
            
if __name__ == "__main__":
    print(Solution().countAndSay(10))
        