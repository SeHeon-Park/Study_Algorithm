import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static ArrayList<Integer[]> M;
    static Queue<Integer[]> Q;
    static int[][] visited;
    static int ans = 0;
    static int flag = 0;
    static int[][] dxy = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int l = Integer.parseInt(input[1]);
        int r = Integer.parseInt(input[2]);
        M = new ArrayList<>();
        for (int i=0; i<n; i++){
            String[] s = br.readLine().split(" ");
            Integer[] in = new Integer[s.length];
            for (int j=0; j<s.length; j++){
                in[j] = Integer.parseInt(s[j]);
            }
            M.add(in);
        }
        Q = new LinkedList<>();
        int m = M.get(0).length;

        while (true){
            flag = 0;
            visited = new int[n][m];
            for (int i=0; i<n; i++){
                for (int j=0; j<m; j++){
                    if (visited[i][j] == 1) continue;
                    visited[i][j] = 1;
                    Q.add(new Integer[]{j, i});
                    HashSet<Integer[]> S = new HashSet<>();
                    S.add(new Integer[]{j, i});
                    int cnt = M.get(i)[j];
                    int idx = 1;
                    while (!Q.isEmpty()){
                        Integer[] ma = Q.poll();
                        for (int[] d : dxy) {
                            int x = ma[0] + d[0];
                            int y = ma[1] + d[1];
                            if (x<0 || x>m-1 || y<0 || y>n-1 || visited[y][x] == 1) continue;
                            if (Math.abs(M.get(y)[x]-M.get(ma[1])[ma[0]]) < l || Math.abs(M.get(y)[x]-M.get(ma[1])[ma[0]])>r) continue;
                            visited[y][x] = 1;
                            cnt += M.get(y)[x];
                            idx += 1;
                            S.add(new Integer[]{x, y});
                            Q.add(new Integer[]{x, y});
                        }
                    }
                    if (idx > 1) {
                        flag = 1;
                        int value = (int) Math.floor(cnt/idx);
                        for (Integer[] mat : S) {
                            M.get(mat[1])[mat[0]] = value;
                        }
                    }
                }
            }
            if (flag != 0)
                ans += 1;
            else break;
        }

        System.out.println(ans);

    }
}

