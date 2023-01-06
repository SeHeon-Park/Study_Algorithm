import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;



public class Main {

    static int n;
    static int m;
    static ArrayList<Integer[]> NC;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);

        NC = new ArrayList<>();
        int cost = 0;
        String[] nInput = br.readLine().split(" ");
        String[] cInput = br.readLine().split(" ");
        for (int i=0; i<n; i++){
            NC.add(new Integer[]{Integer.parseInt(nInput[i]), Integer.parseInt(cInput[i])});
            cost += Integer.parseInt(cInput[i]);
        }
        int[][] dp = new int[n+1][cost+1];

        int ans = cost;

        for(int i=1; i<n+1; i++){
            for (int j=0; j<cost+1; j++){
                int w = NC.get(i-1)[0];
                int c = NC.get(i-1)[1];
                if (c > j) dp[i][j] = dp[i-1][j];
                else {
                    dp[i][j] = Math.max(dp[i-1][j], w+dp[i-1][j-c]);
                    if (dp[i][j] >= m) {
                        ans = Math.min(ans, j);
                    }
                }
            }
        }

        if (m == 0) System.out.println(0);
        else System.out.println(ans);



    }


}