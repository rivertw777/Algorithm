import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int n = jobs.length;
                
        Arrays.sort(jobs, (o1, o2) -> o1[0] - o2[0]);
        List<int[]> copy = new ArrayList<>(Arrays.asList(jobs)); 
        PriorityQueue<int[]> q = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        
        int answer = 0;
        int time = 0;
        while (!copy.isEmpty() || !q.isEmpty()) {            
            while (!copy.isEmpty() && copy.get(0)[0] <= time) {
                q.add(copy.remove(0));
            }
                        
            if (!q.isEmpty()) {
                int[] item = q.poll();
                time += item[1];
                answer += (time - item[0]);
            } else {
                time = copy.get(0)[0];
            }    
        }    
        return answer / n;
    }
}