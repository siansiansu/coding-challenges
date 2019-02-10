class Solution(object):
    def reverse(self, x):
        sign = (x > 0)-(x < 0)                        # 判斷正負號。

        if abs(x) > 0x7FFFFFFF:                   # 超過大小限制 return 0。
            return 0
        else:
            return sign * int(str(abs(x))[::-1])  # 將數字反轉過來並加上正負號。
