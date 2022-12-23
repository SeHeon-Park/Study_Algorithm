import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int ans = 0;
    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int v = Integer.parseInt(input[0]);
        int e = Integer.parseInt(input[1]);

        List<Integer[]> M = new ArrayList<>();

        parent = new int[v];
        for (int i=0; i<v; i++){
            parent[i] = i;
        }

        for (int i = 0; i < e; i++) {
            String[] ve = br.readLine().split(" ");
            int l = Integer.parseInt(ve[0]) - 1;
            int r = Integer.parseInt(ve[1]) - 1;
            int w = Integer.parseInt(ve[2]);
            M.add(new Integer[]{l, r, w});
        }

        M.sort(Comparator.comparingInt((Integer[] a) -> a[2]));

        for (Integer[] i : M) {
            if (union(i[0], i[1])) ans += i[2];
        }

        System.out.println(ans);

    }

    static int find_parent(int a){
        if (a != parent[a]) parent[a] = find_parent(parent[a]);
        return parent[a];
    }

    static boolean union(int a, int b){
        a = find_parent(a);
        b = find_parent(b);
        if (a == b) return false;
        parent[a] = b;
        return true;
    }
}