from leetcode.longest_common_prefix import longestCommonPrefix
from leetcode.palindrome_number import isPalindrome
from leetcode.reverse_integer import reverse

def test_longest_common_prefix():
    strs = ["flower","flow","flight"] 
    ans1 = longestCommonPrefix(strs, strs)
    assert ans1 == "fl"

def test_palindrome_number():
    x = 121
    ans1 = isPalindrome(x, x)
    assert ans1 is True

def test_reverse_integer():
    x = -123
    ans1 = reverse(x, x)
    assert ans1 == -321