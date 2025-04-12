import java.util.*;

class Solution {
    public int solution(int N, int number) {
        List<Set<Integer>> dp = new ArrayList<>();
        
        // Add empty set at position 0
        dp.add(new HashSet<>());
        
        int x = 0;
        for (int i = 1; i <= 8; i++) {
            // N 1 ~ 8개 사용
            Set<Integer> currentSet = new HashSet<>();
            dp.add(currentSet);
            
            x = (10 * x) + N;
            currentSet.add(x);  // N, NN, NNN...
            
            for (int j = 1; j < i; j++) {
                for (int op1 : dp.get(j)) {
                    for (int op2 : dp.get(i - j)) {
                        currentSet.add(op1 + op2);
                        currentSet.add(op1 - op2);
                        currentSet.add(op1 * op2);
                        if (op2 != 0) {
                            currentSet.add(op1 / op2);
                        }
                    }
                }
            }
            
            if (currentSet.contains(number)) {
                return i;
            }
        }
        
        return -1;
    }
}