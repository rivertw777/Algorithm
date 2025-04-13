import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        Arrays.sort(times);
        
        long start = 1;
        long end = (long)times[times.length-1] * n;
        
        while (start < end) {
            long mid = ((long)start + end) / 2;
            
            long total = 0;
            for (int time: times) {
                total += mid / time;
            }
            
            if (total >= n) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return end;
    }
}
