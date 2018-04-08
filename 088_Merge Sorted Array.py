class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p, q = m - 1, n - 1
        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                nums1[p + q + 1] = nums1[p]
                p = p - 1
            else:
                nums1[p + q + 1] = nums2[q]
                q = q - 1
        nums1[:q + 1] = nums2[:q + 1]

    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
            while n > 0:
                if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
                    nums1[m + n - 1] = nums2[n - 1]
                        n -= 1
                else:
                    nums1[m + n - 1] = nums1[m - 1]
                        m -= 1
