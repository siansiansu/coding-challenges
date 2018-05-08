#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import re
        import collections

        sub = re.split(r'[^a-zA-Z]{1,2}', paragraph)
        return sub



if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(Solution().mostCommonWord(paragraph, banned))
