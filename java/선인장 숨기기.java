class Solution {
    public int[] solution(int m, int n, int h, int w, int[][] drops) {
        int[] answer = {0,0};
        // 전략 : 비가 온 시간을 좌표에 표시, 배열을 순회하면서 비가 안온곳부터 찾기, 없으면 숫자가 가장 높은곳이 비가 늦게온 구역

        int[][] arr = new int[m][n];

        for(int i=0; i<drops.length; i++){
            int r = drops[i][0];
            int c = drops[i][1];
            if(arr[r][c] == 0){
                arr[r][c] = i+1;
            }
        }
        // arr은 비온 시간대로 배열 그려놓음 (비가 안왔다면 0)
        
        // 누적합 배열 하나 만들기

        int[][] psum = new int[m+1][n+1];

        for(int i=1; i<=m; i++){
            for(int j=1; j<=n; j++){
                psum[i][j] = arr[i-1][j-1] + psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1];
            }
        }

        // 누적합 만들었으니 0인 구역 찾기
        for (int i = 0; i <= m - h; i++) {
            for (int j = 0; j <= n - w; j++) {
                int total = psum[i + h][j + w] - psum[i][j + w] - psum[i + h][j] + psum[i][j];
                if (total == 0) {
                    return new int[]{i, j};
                }
            }
        }
        // 0인 구역 있으면 return

        int left = 1;
        int right = drops.length;

        while(left <= right){
            int mid = (left + right)/2;
            int[][] wetsum = new int[m+1][n+1];
            for(int i=1; i<=m; i++){
                for(int j=1; j<=n; j++){
                    int wet = (arr[i-1][j-1] != 0 && arr[i-1][j-1] <= mid) ? 1 : 0;
                    wetsum[i][j] = wet + wetsum[i-1][j] + wetsum[i][j-1] - wetsum[i-1][j-1];
                }
            }
            boolean found = false;
            for(int i=0; i<= m-h; i++){
                for(int j=0; j<= n-w; j++){
                    int total = wetsum[i+h][j+w] - wetsum[i][j+w] - wetsum[i+h][j] + wetsum[i][j];
                    if(total == 0){
                        found = true;
                        answer = new int[]{i,j};
                        break;
                    }
                }
                if(found){
                    break;
                }
            }
            if(found == true){
                left = mid+1;
            }
            else{
                right = mid-1;
            }
        }

        return answer;
    }
}