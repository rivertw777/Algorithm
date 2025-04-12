import java.util.*;

class Solution {
    public int solution(int[] scoville, int k) {
        PriorityQueue<Integer> q = new PriorityQueue<>();
        for (int i = 0; i < scoville.length; i++) {
            q.add(scoville[i]);
        }
                
        int cnt = 0;
        while (!q.isEmpty()) {
            int first = q.poll();
                        
            if (first >= k) {
                return cnt;
            }
            
            if (!q.isEmpty()) {
                int second = q.poll();
                int newOne = first + (second * 2);
                cnt++;
                q.add(newOne);
            } else {
                break;
            }
        }
        
        return -1;
    }
}