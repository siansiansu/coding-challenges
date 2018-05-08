#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        p1 = 0
        ans = []
        for p2 in range(len(S)):
            if p2 == len(S) - 1 or S[p2] != S[p2 + 1]:
                if p2 - p1 + 1 >= 3:
                    ans.append([p1, p2])
                p1 = p2 + 1
        return ans


if __name__ == "__main__":
    print(Solution().largeGroupPositions("abcdddeeeeaabbbcd"))