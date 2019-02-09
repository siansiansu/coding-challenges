from leetcode.longest_common_prefix import Solution

def test_longest_common_prefix():
    strs = ["flower","flow","flight"] 
    ans1 = Solution.longestCommonPrefix(strs, strs)
    assert ans1 == "fl"