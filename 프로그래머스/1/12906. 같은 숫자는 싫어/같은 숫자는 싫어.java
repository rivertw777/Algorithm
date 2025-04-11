import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> st = new Stack<>();
        
        for (int number: arr) {
            if (st.size() == 0 || st.peek() != number) {
                st.push(number);
            }
        }
        return st.stream().mapToInt(i->i).toArray();
    }
}