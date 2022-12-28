import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int[][] M;
    static int[][] dxy = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};
    static HashSet<Load> load;
    static int[][] cow;
    static int n;
    static int k;
    static int r;
    static int ans;

    static class Load {
        public int sx;
        public int sy;
        public int ex;
        public int ey;

        public Load(int sx, int sy, int ex, int ey) {
            this.sx = sx;
            this.sy = sy;
            this.ex = ex;
            this.ey = ey;
        }

        @Override
        public int hashCode() {
            return Objects.hash(sx, sy, ex, ey);
        }

        @Override
        public boolean equals(Object obj) {
            if (this.getClass() != obj.getClass()) return false;
            Load o = (Load) obj;
            return (o.sx == this.sx) && (o.sy == this.sy) && (o.ex == this.ex) && (o.ey == this.ey);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        k = Integer.parseInt(input[1]);
        r = Integer.parseInt(input[2]);
        M = new int[n][n];
        load = new HashSet<>();
        cow = new int[k][2];
        for (int i = 0; i < r; i++) {
            String[] m = br.readLine().split(" ");
            int r1 = Integer.parseInt(m[0])-1;
            int c1 = Integer.parseInt(m[1])-1;
            int r2 = Integer.parseInt(m[2])-1;
            int c2 = Integer.parseInt(m[3])-1;
            load.add(new Load(c1, r1, c2, r2));
            load.add(new Load(c2, r2, c1, r1));
        }

        for (int i=0; i<k; i++){
            String[] m = br.readLine().split(" ");
            int r = Integer.parseInt(m[0])-1;
            int c = Integer.parseInt(m[1])-1;
            cow[i][0] = c;
            cow[i][1] = r;
        }

        Queue<Integer[]> Q = new LinkedList<>();
        for (int i=0; i<k-1; i++) {
            int[][] visited = new int[n][n];
            int[][] arr = new int[n][n];
            arr[cow[i][1]][cow[i][0]] = 1;
            visited[cow[i][1]][cow[i][0]] = 1;
            Q.add(new Integer[]{cow[i][0], cow[i][1]});
            while (!Q.isEmpty()){
                Integer[] poll = Q.poll();
                int qx = poll[0];
                int qy = poll[1];
                for (int[] xy : dxy) {
                    int x = qx + xy[0];
                    int y = qy + xy[1];
                    if (x<0 || x>n-1 || y<0 || y>n-1 || visited[y][x] == 1) continue;
                    if (load.contains(new Load(qx, qy, x, y))) continue;
                    visited[y][x] = 1;
                    arr[y][x] = 1;
                    Q.add(new Integer[]{x, y});
                }
            }
            for (int j=i+1; j<k; j++){
                if (arr[cow[j][1]][cow[j][0]] == 0) ans += 1;
            }
        }
        System.out.println(ans);
    }

}
