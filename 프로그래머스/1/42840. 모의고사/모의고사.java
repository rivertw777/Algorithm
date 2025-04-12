import java.util.*;

class Solution {
    public List<Integer> solution(int[] answers) {        
        int[] p1 = new int[]{1,2,3,4,5};
        int[] p2 = new int[]{2,1,2,3,2,4,2,5};
        int[] p3 = new int[]{3,3,1,1,2,2,4,4,5,5};
        int[] score = new int[]{0,0,0};
        
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == p1[i % p1.length]) 
                score[0] += 1;
            if (answers[i] == p2[i % p2.length]) 
                score[1] += 1;
            if (answers[i] == p3[i % p3.length]) 
                score[2] += 1;            
        }
        
        int max = Math.max(score[0], Math.max(score[1], score[2])); 
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < score.length ; i++) {
            if (score[i] == max) {
                answer.add(i + 1);
            }
        }
        return answer;
    }
}