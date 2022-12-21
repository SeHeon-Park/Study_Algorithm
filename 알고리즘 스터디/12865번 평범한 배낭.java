import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int[][] M;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int k = Integer.parseInt(input[1]);
        M = new int[n+1][2];
        M[0][0] = 0;
        M[0][1] = 0;
        dp = new int[n+1][k+1];
        for (int i=1; i<=n; i++) {
            String[] weight = br.readLine().split(" ");
            for (int j = 0; j < 2; j++) {
                M[i][j] = Integer.parseInt(weight[j]);
            }
        }

        for (int i=1; i<=n; i++) {
            for (int j=1; j<=k; j++){
                if (M[i][0] <= j) dp[i][j] = Math.max(M[i][1] + dp[i-1][j-M[i][0]], dp[i-1][j]);
                else dp[i][j] = dp[i-1][j];
            }
        }
        System.out.println(dp[n][k]);

    }

}