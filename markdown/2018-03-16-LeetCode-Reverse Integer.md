Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

* Input: 123
* Output:  321

Example 2:

* Input: -123
* Output: -321

Example 3:

* Input: 120
* Output: 21

## Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = (x>0)-(x<0)
        x = int(str(sign*x)[::-1])
        x = 0 if abs(x) > 0x7FFFFFFF else x
        
        return sign*x       

if __name__ == "__main__":
    print (Solution().reverse(123))
    print (Solution().reverse(-123))
    print (Solution().reverse(120))
```

## Submission Detail

![](/images/2018-03-15-GmLRZ2.jpg)

## My Notes
* cmp函數不支援python3，用sign = (x>0)-(x<0)判斷正負號
* [::-1] slice寫法
* notice the 32-bit signed integer range