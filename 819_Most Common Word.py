#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.replace(".", "").split()
        counts = 0
        results = 0
        for i in range(len(paragraph)):
            if paragraph[i] in paragraph:
                counts += 1
            results = max(results, counts)
        return results



if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(Solution().mostCommonWord(paragraph, banned))
