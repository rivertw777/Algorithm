import java.util.*;

class Solution {
    public int solution(int[][] tri) {
        for (int i = 1; i < tri.length; i++) {
            for (int j = 0; j < tri[i].length; j++) {
                if (j == 0) {
                    tri[i][j] += tri[i-1][0];
                } else if (j == tri[i].length - 1) {
                    tri[i][j] += tri[i-1][j-1];
                } else {
                    tri[i][j] += Math.max(tri[i-1][j-1], tri[i-1][j]);
                }
            }
        }
        
        List<Integer> answer = new ArrayList<>();
        for (int num: tri[tri.length - 1]) {
            answer.add(num);
        }            
        return Collections.max(answer);
    }
}