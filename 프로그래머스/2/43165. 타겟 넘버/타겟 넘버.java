class Solution {
    int answer = 0;

    public int solution(int[] numbers, int target) {
        dfs(0, 0, numbers, target);
        return answer;
    }

    void dfs(int index, int total, int[] numbers, int target) {
        if (index == numbers.length && total == target) {
            answer++;
            return;
        }
        if (index == numbers.length) {
            return;
        }

        dfs(index + 1, total + numbers[index], numbers, target);
        dfs(index + 1, total - numbers[index], numbers, target);
    }
}
