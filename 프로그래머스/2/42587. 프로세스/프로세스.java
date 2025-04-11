import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        int l = location;

        Queue<Integer> q = new LinkedList<>();
        for(int i : priorities){
            q.add(i);
        }

        Arrays.sort(priorities);
        int size = priorities.length-1;

        while(!q.isEmpty()) {
            Integer i = q.poll();
            if (i == priorities[size - answer]) {
                answer++;
                l--;
                if(l <0)
                    break;
            } else {
                q.add(i);
                l--;
                if(l<0)
                    l=q.size()-1;
            }
        }
        return answer;
    }
}