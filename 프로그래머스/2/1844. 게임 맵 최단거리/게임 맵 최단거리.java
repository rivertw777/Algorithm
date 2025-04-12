import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        int answer = 0;
        
        int[] dx = new int[]{1, -1, 0, 0};
        int[] dy = new int[]{0, 0, 1, -1};
        
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0,0});
        
        while (!q.isEmpty()) {
            int[] item = q.poll();
            int x = item[0];
            int y = item[1];
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                    continue;    
                }
                
                if (maps[nx][ny] != 0 && maps[nx][ny] == 1) {
                    maps[nx][ny] = maps[x][y] + 1;
                    q.offer(new int[]{nx, ny});
                    
                    if (maps[n-1][m-1] != 1) {
                        return maps[n-1][m-1];
                    }
                }
            }
        }
        return -1;
    }
}