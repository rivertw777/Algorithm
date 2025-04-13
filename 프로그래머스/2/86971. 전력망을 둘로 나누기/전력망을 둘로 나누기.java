import java.util.*;

class Solution {
    public int dfs(int v, List<Integer>[] graph, boolean[] visited) {
        visited[v] = true;
        int cnt = 1;
        for (int i = 0; i < graph[v].size(); i++) {
            int u = graph[v].get(i);
            if (!visited[u]) {
                cnt += dfs(u, graph, visited);
            }
        }
        return cnt;
    }
    
    public int solution(int n, int[][] wires) {
        List<Integer>[] graph = new ArrayList[n + 1];
        
        for (int i = 0; i < n + 1; i++) {
            graph[i] = new ArrayList<>();        
        }
        
        for (int i = 0; i < wires.length; i++) {
            int a = wires[i][0];
            int b = wires[i][1];
            graph[a].add(b);
            graph[b].add(a);
        }
        
        int answer = 100;
        for (int i = 0; i < n-1; i++) {
            boolean[] visited = new boolean[n+1];
            int a = wires[i][0];
            int b = wires[i][1];
            visited[a] = true;
            int temp = Math.abs(dfs(b, graph, visited) - dfs(a, graph, visited));
            answer = Math.min(temp, answer);
        }
        return answer;
    }
    
    
}