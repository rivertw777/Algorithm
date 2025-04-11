import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> hm = new HashMap<>();
        
        for (String p : participant)
            hm.put(p, hm.getOrDefault(p, 0) + 1);
        
        for (String c : completion)
            hm.put(c, hm.get(c) - 1);
        
        for (String p : hm.keySet())
            if (hm.get(p) > 0)
                return p;
        return null;
        
    }
}