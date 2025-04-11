import java.util.*;

class Solution {
    public List<Integer> solution(int[] p, int[] s) {
        List<Integer> answer = new ArrayList<>();
        
        int n = p.length;
        List<Integer> pList = new ArrayList<>();
        List<Integer> sList = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            pList.add(p[i]);
            sList.add(s[i]);
        }
        
        while (!pList.isEmpty()) {
            for (int i = 0; i < pList.size(); i++) {
                pList.set(i, pList.get(i) + sList.get(i));
            }
            
            int cnt = 0;
            
            while (!pList.isEmpty() && pList.get(0) >= 100) {
                pList.remove(0);
                sList.remove(0);
                cnt++;
            }
            if (cnt != 0) {
                answer.add(cnt);
            }
        }
        return answer;
    }
}