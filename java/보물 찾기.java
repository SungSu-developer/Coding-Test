import java.util.function.Function;

class Solution {
    public int solution(int[] depth, int money, Function<Integer, Integer> excavate) {

        // mid를 가운데 열이 아닌 좌우 거의 비슷한 depth를 찾아서 정해야겠다.
        // 반례를 찾았다. mid가 money보다 크면 그대로 끝이다 양옆을 비교하여 mid를 찾는 것은 방법이 아니다.
        // 본인 포함 경우의 수가 작은 열부터 -> 큰 열로 찾아보는 게 좋아보인다.
        // 본인 ~ (left or right)까지 중에 가장 적은 경우의수를 나타내는 2차원 배열 필요

        int n = depth.length;
        long[][] dp = new long[n][n];
        int[][] choice = new int[n][n];

        for (int i = 0; i < n; i++) {
            dp[i][i] = depth[i];
            choice[i][i] = i;
        }

        for (int len = 2; len <= n; len++) {
            for (int left = 0; left <= n - len; left++) {
                int right = left + len - 1;
                dp[left][right] = Long.MAX_VALUE;

                for (int k = left; k <= right; k++) {
                    long leftCost = (k > left) ? dp[left][k - 1] : 0;
                    long rightCost = (k < right) ? dp[k + 1][right] : 0;
                    long totalCost = depth[k] + Math.max(leftCost, rightCost);

                    if (totalCost < dp[left][right]) {
                        dp[left][right] = totalCost;
                        choice[left][right] = k;
                    }
                }
            }
        }

        int left = 0;
        int right = n - 1;

        while (left <= right) {
            int mid = choice[left][right];
            int res = excavate.apply(mid + 1);

            if (res == 0) {
                return mid + 1;
            } else if (res == 1) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return 0;
    }
}