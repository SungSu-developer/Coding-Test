class Solution {
    public long[] solution(int[] arr, long l, long r) {

        // 2중 for문으로 해결 시간초과 -> 슬라이딩 윈도우 써야할듯
        // k구하는 것도 brr 배열 없이 다 구해야할 것 같다.
        // 3,2,3,1,1 5,9 [2] 마지막, [3] 전체 [1] 전체
        // 9-5+1 = 5  처음 위치 찾는건 l - arr[i] 하다가 <= 0 나오면 그것의 절댓값+1 * arr[i] 하면 됨 1*2 해서 2나옴
        // 5, 절대값 + 1 = 1 하나 가져갔으니까 앞으로 4개 가져가야함
        // 3,3,3,1 올차례 4 - arr[i]  양수면 sqrt(arr[i]) 음수면 그냥 빼기 전의 수 * arr[i]
    
        long k = 0;
        long remL = l;
        long need = r - l + 1;

        for (int x : arr) {
            if (need == 0) break;

            if (remL > 0) {
                if (remL - x <= 0) {
                    long take = Math.min(need, x - remL + 1); // l r 같은 블록인 경우 처리
                    k += take * x;
                    need -= take;
                    remL = 0;
                } else {
                    remL -= x;
                }
            } else {
                if (need >= x) {
                    k += (long) x * x;
                    need -= x;
                } else {
                    k += need * x;
                    need = 0;
                }
            }
        }
        long c = 0;

        int right = 1;
        long midCount = 0;
        long midSum = 0;

        for (int left = 0; left < n - 1; left++) {
            if (right <= left) {
                right = left + 1;
                midCount = 0;
                midSum = 0;
            }

            while (right + 1 < n && 1 + (midCount + arr[right]) + 1 <= W) {
                long R = arr[right];
                if (arr[left] + midCount + R >= W) {
                    c += countPairs(arr[left], R, W - midCount, k - midSum);
                }
                midCount += R;
                midSum += R * R;
                right++;
            }

            if (right < n && 1 + midCount + 1 <= W && arr[left] + midCount + arr[right] >= W) {
                c += countPairs(arr[left], arr[right], W - midCount, k - midSum);
            }

            if (left + 1 < right) {
                long nextVal = arr[left + 1];
                midCount -= nextVal;
                midSum -= nextVal * nextVal;
            }
        }

        

        return new long[]{k, c};
    }
}

/*500 1 2 3 4 5 6 7 8 9 10

499, 550

-1 ( 500 * 1)



*/