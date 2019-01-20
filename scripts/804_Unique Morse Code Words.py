class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
        ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...",
        "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        letters = [chr(x) for x in range(97, 123)]

        mdict = {c: m for c, m in zip(letters, morse)}

        return len(set(''.join(map(mdict.get, w)) for w in words))


if __name__ == "__main__":
    print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))



class Solution(object):
    def uniqueMorseRepresentations2(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", 
                 ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
                 "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        results = set()
        for i in words:
            string = ''
            for j in i:
                string += morse[ord(j) - 97]
            results.add(string)
        return len(results)

 if __name__ == "__main__":
    print(Solution().uniqueMorseRepresentations2(["gin", "zen", "gig", "msg"]))       
