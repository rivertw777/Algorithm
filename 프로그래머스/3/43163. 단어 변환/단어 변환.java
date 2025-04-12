import java.util.*;

class Solution {
    int answer = 0;
    
    void dfs(String begin, String target, String[] words, int count) {
        if (begin.equals(target)) {
            answer = count;
            return;
        }
        
        for (String word: words) {            
            int dif = 0;
            for (int i = 0; i < word.length(); i++) {
                if (begin.charAt(i) != word.charAt(i)) {
                    dif += 1;
                }
            }
                        
            if (dif == 1) {
                List<String> wordList = new ArrayList<>();
                for (String w : words) {
                    if (!w.equals(word)) {
                        wordList.add(w);
                    }
                }
                String[] copy = wordList.toArray(new String[0]);
                dfs(word, target, copy, count + 1);
            }
        }
    }
    
    public int solution(String begin, String target, String[] words) {
        dfs(begin, target, words, 0);
        return answer;
    }
}