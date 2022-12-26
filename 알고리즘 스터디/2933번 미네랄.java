import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static String[][] M;
    static int[] L;
    static int[][] dxy = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    static Queue<Integer[]> Q;
    static int r;
    static int c;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        r = Integer.parseInt(input[0]);
        c = Integer.parseInt(input[1]);
        M = new String[r][c];
        for (int i=0; i<r; i++){
            String[] m = br.readLine().split("");
            System.arraycopy(m, 0, M[i], 0, c);
        }
        int cnt = Integer.parseInt(br.readLine());
        L = new int[cnt];
        String[] l = br.readLine().split(" ");
        for (int i=0; i<cnt; i++){
            L[i] = Integer.parseInt(l[i]);
        }

        int dir = 1; // 1:왼 -> 오, -1: 오->왼
        for (int h : L) {
            if (dir == 1) {
                leftRight(h);
            }
            else{
                rightLeft(h);
            }
            dir *= -1;
        }

        for (String[] strings : M) {
            for (String string : strings) {
                System.out.print(string);
            }
            System.out.println();
        }

    }

    static HashMap<Integer, ArrayList<Integer[]>> findCluster(int x, int y) {
        HashMap<Integer, ArrayList<Integer[]>> C = new HashMap<>();
        M[y][x] = ".";
        Q = new LinkedList<>();
        int[][] visited = new int[r][c];
        int cnt = 1;
        for (int[] xy : dxy) {
            int zx = x + xy[0];
            int zy = y + xy[1];
            if (zx < 0 || zx > c - 1 || zy < 0 || zy > r - 1 || Objects.equals(M[zy][zx], ".") || visited[zy][zx] == 1)
                continue;
            ArrayList<Integer[]> value = new ArrayList<>();
            value.add(new Integer[]{zx, zy});
            C.put(cnt, value);
            visited[zy][zx] = 1;
            Q.add(new Integer[]{zx, zy});
            while (!Q.isEmpty()) {
                Integer[] qxy = Q.poll();
                int qx = qxy[0];
                int qy = qxy[1];
                for (int[] d : dxy) {
                    int fx = qx + d[0];
                    int fy = qy + d[1];
                    if (fx < 0 || fx > c - 1 || fy < 0 || fy > r - 1 || Objects.equals(M[fy][fx], ".") || visited[fy][fx] == 1)
                        continue;
                    visited[fy][fx] = 1;
                    ArrayList<Integer[]> cv = C.get(cnt);
                    cv.add(new Integer[]{fx, fy});
                    Q.add(new Integer[]{fx, fy});
                }
            }
            cnt += 1;
        }
        return C;
    }

    static void leftRight(int height){
        int h = r-height;
        int t=0;
        while (true){
            if (t > c-1) return;
            if (Objects.equals(M[h][t], "x")) {;
                dropMinerals(findCluster(t, h));
                return;
            }
            t += 1;
        }
    }

    static void rightLeft(int height){
        int h = r-height;
        int t = c-1;
        while (true){
            if (t < 0) return;
            if (Objects.equals(M[h][t], "x")) {;
                dropMinerals(findCluster(t, h));
                return;
            }
            t -= 1;
        }
    }

    static void dropMinerals(HashMap<Integer, ArrayList<Integer[]>> cluster) {
        for (ArrayList<Integer[]> minerals : cluster.values()) {
            minerals.sort(Comparator.comparingInt((Integer a[]) -> -a[1])); // 높이로 내림차순 정렬
            if (minerals.get(0)[1] == r-1) continue;
            else {
                // 내려간 길이
                int minHeight = r;
                for (Integer[] b : minerals) {
                    int bx = b[0];
                    int by = b[1];
                    M[by][bx] = ".";
                    int l = 1;
                    by += 1;
                    while (true) {
                        if (minHeight <= l) break;
                        if (by == r-1) {
                            minHeight = l;
                            break;
                        }
                        if (Objects.equals(M[by + 1][bx], "x")) {
                            minHeight = l;
                            break;
                        }
                        by += 1;
                        l += 1;
                    }
                }
                for (Integer[] mineral : minerals) {
                    int x = mineral[0];
                    int y = mineral[1];
                    M[y + minHeight][x] = "x";
                }
            }
        }
    }

}
