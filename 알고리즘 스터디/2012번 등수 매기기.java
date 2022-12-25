import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static ArrayList<Integer> P;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        P = new ArrayList<>();
        for (int i=0; i<n; i++){
            int s = Integer.parseInt(br.readLine());
            P.add(s);
        }
        P.sort(Comparator.comparing((Integer p) -> p));

        long rank = 1;
        long ans = 0;
        for (Integer p : P) {
            ans += (Math.abs(p-rank));
            rank += 1;
        }

        System.out.println(ans);


    }
}
