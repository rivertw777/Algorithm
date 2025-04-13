import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        List<Integer>[] graph = new ArrayList[n+1];
        int[] distance = new int[n + 1];
        
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < n + 1; i++) {
            distance[i] = Integer.MAX_VALUE;
        }
        
        for (int i = 0; i < edge.length; i++) {
            graph[edge[i][0]].add(edge[i][1]);
            graph[edge[i][1]].add(edge[i][0]);
        }
        
        PriorityQueue<int[]> q = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        q.add(new int[]{0, 1}); 
        distance[1] = 0;
        while (!q.isEmpty()) {
            int[] item = q.poll();
            int dist = item[0];
            int cur = item[1];
            
            if (dist > distance[cur]) {
                continue;
            }
            
            for (int i = 0; i < graph[cur].size(); i++) {
                int cost = dist + 1;
                if (cost < distance[graph[cur].get(i)]) {
                    distance[graph[cur].get(i)] = cost;
                    q.add(new int[]{cost, graph[cur].get(i)});
                }
            }            
        }
                        
        int max = 0;
        for (int i = 0; i < distance.length; i++) {
            if (distance[i] != Integer.MAX_VALUE) {
                max = Math.max(max, distance[i]);
            }
        }
                
        int answer = 0;
        for (int i = 0; i < distance.length; i++) {
            if (distance[i] == max) {
                answer += 1;
            }
        }
        return answer;
    }
}