import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
class Solution {
    public String solution(int[] numbers) {
       List<String> result = Arrays.stream(numbers).mapToObj(n -> String.valueOf(n)).collect(Collectors.toList());
        Collections.sort(result, (s1, s2) -> (s2+s1).compareTo(s1+s2));

        if(result.get(0).equals("0")) {
            return "0";
        }

        return result.stream().collect(Collectors.joining());
    }
}