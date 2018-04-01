class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        letters = [chr(x) for x in range(97, 123)]

        mdict = {c: m for c, m in zip(letters, morse)}

        return len(set(''.join(map(mdict.get, w)) for w in words))


if __name__ == "__main__":
    print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
