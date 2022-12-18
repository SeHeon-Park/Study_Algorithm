# 파이썬 풀이
import sys, math
input = sys.stdin.readline

n, m, b = map(int, input().split())
MIN, MAX = 256, 0
time = math.inf

M = []
for i in range(n):
    a = list(map(int, input().split()))
    M += a
    MIN = min(MIN, min(a))
    MAX = max(MAX, max(a))
M.sort(reverse=True)

for k in range(MIN, MAX+1, 1):
    time_temp = 0
    flag = 0
    block = b
    for i in range(n*m):
        if M[i] < k and block >= k-M[i]:
            time_temp += (k - M[i])
            block -= (k - M[i])
        elif (M[i] < k and block < (k - M[i])) or (time < time_temp):
            flag = 1
            break
        elif M[i] > k:
            time_temp += ((M[i] - k) * 2)
            block += (M[i] - k)
    if flag != 1 and time >= time_temp:
        time = time_temp
        height = k

print(time, height)


# 자바 풀이 (시간 초과)
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

public class Main {

    static Integer[] M;
    static int MAX = 0;
    static int MIN = 256;
    static long time = 987654321L;
    static int height;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);
        int b = Integer.parseInt(input[2]);
        M = new Integer[n*m];
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                int h = Integer.parseInt(s[j]);
                M[i*m + j] = h;
                MAX = Math.max(MAX, h);
                MIN = Math.min(MIN, h);
            }
        }
        Arrays.sort(M, Collections.reverseOrder());

        for (int k = MIN; k <= MAX; k++) {
            int timeTemp = 0;
            int flag = 0;
            int block = b;
            for (int i = 0; i < n * m; i++) {
                if (M[i] < k && block >= (k - M[i])) {
                    timeTemp += (k - M[i]);
                    block -= (k - M[i]);
                } else if ((M[i] < k && block < (k - M[i])) || (time < timeTemp)) {
                    flag = 1;
                    break;
                } else if (M[i] > k) {
                    timeTemp += ((M[i] - k) * 2);
                    block += (M[i] - k);
                }
            }
            if (flag != 1 && time >= timeTemp) {
                time = timeTemp;
                height = k;
            }
        }

        System.out.println(time+" "+height);
    }
}


