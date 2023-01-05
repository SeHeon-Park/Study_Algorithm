import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> L = new ArrayList<>();
        L.add(0);
        int[] DP = new int[n+1];
        for (int i=0; i<n; i++){
            int l = Integer.parseInt(br.readLine());
            L.add(l);
        }
        for (int i=1; i<n+1; i++){
            for (int j=i-1; j>-1; j--){
                if (L.get(i) > L.get(j)) {
                    DP[i] = Math.max(DP[i], DP[j] + 1);
                }
            }
        }
        Arrays.sort(DP);
        System.out.println(n-DP[n]);
    }
}