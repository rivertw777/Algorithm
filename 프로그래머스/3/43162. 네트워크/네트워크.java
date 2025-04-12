import java.util.*;

class Solution {
    void bfs(int start, int[][] computers, boolean[] visited) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        visited[start] = true;
        
        while (!q.isEmpty()) {
            int item = q.poll();
            for (int i = 0; i < computers[item].length; i++) {
                if (computers[item][i] != 0 && visited[i] != true) {
                    visited[i] = true;
                    q.offer(i);
                }
            }
        }
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        
        for (int i = 0; i < n; i++) {
            if (visited[i] != true) {
                bfs(i, computers, visited);
                answer += 1;
            }
        }
        return answer;
    }
}