class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] dp = new int[n][m];

        // 시작점 초기화
        dp[0][0] = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // 물 웅덩이 체크
                boolean isPuddle = false;
                for (int[] puddle : puddles) {
                    if (puddle[0] == j + 1 && puddle[1] == i + 1) {
                        isPuddle = true;
                        break;
                    }
                }

                if (isPuddle) {
                    dp[i][j] = 0; // 물 웅덩이는 0으로 설정
                    continue;
                }

                // (0,0)은 이미 1로 초기화했으므로, (0,0)이 아닌 경우에만 계산
                if (i == 0 && j == 0) continue;

                // 위쪽에서 오는 경우
                if (i > 0) {
                    dp[i][j] = (dp[i][j] + dp[i - 1][j]) % 1000000007;
                }
                // 왼쪽에서 오는 경우
                if (j > 0) {
                    dp[i][j] = (dp[i][j] + dp[i][j - 1]) % 1000000007;
                }
            }
        }

        return dp[n - 1][m - 1];
    }
}
