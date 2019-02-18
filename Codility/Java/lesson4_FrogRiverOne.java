// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");
import java.util.HashSet;
import java.util.Set;


class Solution {
    public int solution(int X, int[] A) {
        // write your code in Java SE 8
        Set<Integer> s = new HashSet<Integer>();
        
        for (int i = 0; i < A.length; i++) {
            s.add(A[i]);
            if (s.size() == X) {
                return i;
            }
        }
        return -1;
    }
}