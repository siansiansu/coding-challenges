#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """ 
        answer = []
        S = S.split()[:]
        for i in range(len(S)):
            if S[i][0].lower() in vowel:
                word = S[i] + 'ma' + (i + 1) * "a"
            else:
                word = S[i][1:] + S[i][0] + "ma" + (i + 1) * "a"
            answer.append(str(word))
        return " ".join(answer)

if __name__ == "__main__":
    S = "I speak Goat Latin"
    print(Solution().toGoatLatin(S))
