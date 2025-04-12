import java.util.*;

class Solution {
    public List<Integer> solution(int[] prices) {
        Queue<Integer> q = new LinkedList<>();
            
        for (int p: prices) {
            q.offer(p);
        }
                
        List<Integer> answer = new ArrayList<>();
        while (!q.isEmpty()) {
            int item = q.poll();
            
            int cnt = 0;
            for (int next: q) {
                cnt++;
                if (item <= next) {
                    continue;
                } else {
                    break;
                }
            }
            answer.add(cnt);
        }
        return answer;
    }
}