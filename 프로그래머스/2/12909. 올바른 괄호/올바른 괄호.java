import java.util.Stack;
class Solution {
    boolean solution(String s) {
        boolean answer = true;  
        String res = "YES";
        Stack<Integer> st = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                st.push(1);
            } else if (s.charAt(i) == ')') {
                if (st.isEmpty()) {
                    answer = false;
                    break;
                } else {
                    st.pop();
                }
            }
        }

        if(!st.isEmpty()) {
            answer = false;
        }

        return answer;
    }   
}