class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for m in moves:
            if m == 'U': y += 1
            elif m == 'D': y -= 1
            elif m == 'R': x += 1
            elif m == 'L': x -= 1
        return x == y == 0 

    def judgeCircle2(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')

if __name__ == "__main__":    
    print(Solution().judgeCircle('UD'))  
    print(Solution().judgeCircle2('UD')) 



if __name__ == "__main__":    
    print(Solution().judgeCircle('UD'))    