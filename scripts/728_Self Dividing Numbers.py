class Solution:
    def isDividingNumber(self, num):
        if '0' in str(num):
            return False
        return 0 == sum(num % int(i) for i in str(num))

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        answer = []
        for num in range(left, right + 1):
            if self.isDividingNumber(num):
                answer.append(num)
        return answer

if __name__ == "__main__":
    print(Solution().selfDividingNumbers(1, 22))





