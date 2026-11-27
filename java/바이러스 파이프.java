class Solution {
    public int solution(int n, int infection, int[][] edges, int k) {
        // 일단 dfs로 푸는 문제로 보여진다.
        // 파이프 통로를 종류별로 열어보고, 감염시키고, cnt의 최대치를 dfs를 통해 구해보자.

        boolean infected[] = new boolean[n+1];
        infected[infection] = true;

        return dfs(n, edges, k, 1, 0, infected);
    }
    private int dfs(int n, int[][] edges, int k, int cnt, int depth, boolean infected[]){
        if (depth == k || cnt == n) {
            return cnt;
        }

        int Maxcnt = cnt;
        for(int i=1; i<=3; i++){
            boolean[] nextInfected = infected.clone();
            int Nextcnt = cnt;
            boolean change = true;

            while(change){
                change = false;
                for(int j=0; j<edges.length; j++){
                    if(edges[j][2] == i){
                        int u = edges[j][0];
                        int v = edges[j][1];
                        if(nextInfected[u] && !nextInfected[v]){
                            nextInfected[v] = true;
                            Nextcnt++;
                            change = true;
                        }
                        else if(!nextInfected[u] && nextInfected[v]){
                            nextInfected[u] = true;
                            Nextcnt++;
                            change = true;
                        }
                    }
                }
            }
            if(Nextcnt > cnt){
                Maxcnt = Math.max(Maxcnt, dfs(n, edges, k, Nextcnt, depth + 1, nextInfected));
            }
        }

        return Maxcnt;
    }
}