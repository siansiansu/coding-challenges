class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs: return ''                  # 如果沒有字串則返回 ''
        for i, j in enumerate(zip(*strs)):      # 將字串 strs 拆開組合，使用一個迴圈逐一比較相同位置的不同字串
            if len(set(j)) > 1:                 # 使用一個判斷式判斷該組合的集合長度是否大於 1，若大於 1 則代表該組合的字串相異
                return strs[0][:i]              # 返回到該位置
        return min(strs)                        # 尋找最少共同的部分