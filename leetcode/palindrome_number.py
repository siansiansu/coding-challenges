def isPalindrome(self, x: 'int') -> 'bool':
    return str(x) == str(x)[::-1]         # 使用 Python slice 的技巧，如果倒著的數字也一樣的話則返回 True。