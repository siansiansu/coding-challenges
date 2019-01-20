#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 13:49:02 2018

@author: siansiansu
"""
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        
        out = []
        for i in words:
            for j in keyboard:
                if set(i.lower()).issubset(set(j)):
                    out.append(i)
        return out
                
                
if __name__ == "__main__":
    print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))


