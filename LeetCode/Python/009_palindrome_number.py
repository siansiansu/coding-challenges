class Solution(object):
    def isPalindrome(self, x):
        # 使用 Python slice 的技巧，如果倒著的數字也一樣的話則返回 True。
        return str(x) == str(x)[::-1]
