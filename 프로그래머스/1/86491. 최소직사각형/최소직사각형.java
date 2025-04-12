import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        List<Integer> x = new ArrayList<>();
        List<Integer> y = new ArrayList<>();
        
        for (int i = 0; i < sizes.length; i++) {
            int a = 0;
            int b = 0;
            
            if (sizes[i][0] >= sizes[i][1]) {
                a = sizes[i][0];
                b = sizes[i][1];
            } else {
                a = sizes[i][1];
                b = sizes[i][0];
            }
                
            x.add(a);
            y.add(b);
        }
        
        return Collections.max(x) * Collections.max(y);
    }
}