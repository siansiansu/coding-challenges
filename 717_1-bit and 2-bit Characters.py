class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        size = len(bits)
        indicator = 0
        while indicator < size:
            if indicator == size - 1:
                return True
            
            if bits[indicator] == 0: 
                indicator += 1
            else: indicator += 2
        return False