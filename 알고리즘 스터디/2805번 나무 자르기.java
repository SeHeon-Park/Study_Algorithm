import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class Main {

    static int[] tree;
    static ArrayList<Long> ans = new ArrayList<>();
    static long m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);
        tree = new int[n];
        String[] info = br.readLine().split(" ");
        for (int i=0; i<n; i++){
            tree[i] = Integer.parseInt(info[i]);
        }
        Arrays.sort(tree);
        long min = 0, max = tree[n-1];

        while (true) {
            if (min > max) break;
            long mid = (min + max) / 2;
            long r = check(mid);
            if (r >= m) {
                ans.add(mid);
                min = mid+1;
            }
            else max = mid-1;
        }

        ans.sort(Comparator.naturalOrder());
        System.out.println(ans.get(ans.size()-1));
    }

    static long check(long h){
        long r = 0;
        for (int t : tree) {
            if (t > h) r += (t-h);
        }
        return r;
    }
}
