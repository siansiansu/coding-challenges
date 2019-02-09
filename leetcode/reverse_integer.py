def reverse(self, x: 'int') -> 'int':
    sign = (x>0)-(x<0)
    
    if abs(x) > 0x7FFFFFFF:
        return 0
    else:
        return sign * int(str(abs(x))[::-1])