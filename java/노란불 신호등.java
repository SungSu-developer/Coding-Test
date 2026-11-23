class Solution {
    public int solution(int[][] signals) {
        // 신호등은 초 노 빨 순서로 반복
        // 모든 신호등이 노란불 -> 정전
        // 전체 싸이클은 최대공배수 여까지 아무일도 없으면 -1
        // 모든 신호등이 현재 시간 % 한 싸이클 길이 = signals[0]+1 ~ signals[0] + signals[1] 면 노란불 

        int n = signals.length;
        int[] signals_len = new int[n];
        int maxTime = 1;

        for (int i = 0; i < n; i++) {
            int len = signals[i][0] + signals[i][1] + signals[i][2];
            signals_len[i] = len;
            maxTime = lcm(maxTime, len);
        }

        for (int time = 1; time <= maxTime; time++) {
            boolean allYellow = true;

            for (int i = 0; i < n; i++) {
                int rem = time % signals_len[i];
                int yellowStart = signals[i][0] + 1;
                int yellowEnd = signals[i][0] + signals[i][1];

                if (rem < yellowStart || rem > yellowEnd) {
                    allYellow = false;
                    break;
                }
            }

            if (allYellow) {
                return time;
            }
        }

        return -1;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }

    private int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }
}