import java.util.*;

class Solution {
    public int[] solution(int b, int y) {
        int total = b + y;
        
        for (int i = 1; i < total + 1; i++) {
            if (total % i != 0) {
                continue;
            } 
            
            int j = total / i;
            
            if ((i - 2) * (j - 2) == y) {
                int max = Math.max(i, j);
                int min = Math.min(i, j);                
                return new int[]{max, min};
            }
        }
        return null;
    }
}