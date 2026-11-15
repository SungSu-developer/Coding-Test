class Solution {
    public int solution(int[][] cost, int[][] hint) {
        int answer = 0;
        // 최소 가격으로 스테이지 클리어하기

        // [[160, 140, 120, 110, 60], [290, 270, 260, 120, 10], [160, 130, 120, 60, 20], [160, 120, 80, 70, 20], [110, 70, 60, 30, 20]] 요게 cost
        // [[40, 2, 3], [40, 5, 3], [20, 5, 4], [50, 5, 5]] 요게 힌트번들

        // 풀이 1. 힌트 개수 계산 -> 개수,가격 비교 -> 대입 (구현 가능한지도 모르겠긴함)
        // 풀이 2. dfs로 완탐 때리기?
        // dfs 해보고 시간초과나면 1해보자

        answer += cost[0][0];

        answer = dfs(0, answer, new int[cost.length - 1], cost, hint);

        return answer;
    }

    private int dfs(int depth, int money, int[] have, int[][] cost, int[][] hint) {
        if (depth == hint.length) {
            return money;
        }

        for (int i = 1; i < hint[depth].length; i++) {
            have[hint[depth][i] - 2] += 1;
        }

        int idx1 = Math.min(have[depth], cost[depth + 1].length - 1);
        int buy = dfs(depth + 1, money + hint[depth][0] + cost[depth + 1][idx1], have, cost, hint);
        // 힌트 샀을 때

        for (int i = 1; i < hint[depth].length; i++) {
            have[hint[depth][i] - 2] -= 1;
        }
        int idx2 = Math.min(have[depth], cost[depth + 1].length - 1);
        int nobuy = dfs(depth + 1, money + cost[depth + 1][idx2], have, cost, hint);
        // 힌트 안샀을 때

        return Math.min(buy, nobuy);
    }
}