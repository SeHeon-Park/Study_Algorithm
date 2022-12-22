// 유니온 파인드
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        parent = new int[n];

        for (int i=0; i<n; i++){
            parent[i] = i;
        }

        for (int i=0; i<n; i++){
            String[] city = br.readLine().split(" ");
            for (int j=0; j<n; j++){
                if (Integer.parseInt(city[j]) == 1){
                    unionFind(i, j);
                }
            }
        }

        String[] path = br.readLine().split(" ");
        for (int i=0; i<m-1; i++){
            int cur = Integer.parseInt(path[i])-1;
            int target = Integer.parseInt(path[i+1])-1;
            if (parent[cur] != parent[target]) {
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }

    static int findParents(int city) {
        if (city != parent[city])
            parent[city] = findParents(parent[city]);
        return parent[city];
    }

    static void unionFind(int c1, int c2){
        c1 = findParents(c1);
        c2 = findParents(c2);

        if (c1 > c2)
            parent[c1] = c2;
        else
            parent[c2] = c1;
    }

}


// bfs
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    static int[][] M;
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        M = new int[n][n];

        for (int i=0; i<n; i++){
            String[] city = br.readLine().split(" ");
            for (int j=0; j<n; j++){
                M[i][j] = Integer.parseInt(city[j]);
            }
        }

        String[] path = br.readLine().split(" ");
        for (int i=0; i<m-1; i++){
            int cur = Integer.parseInt(path[i])-1;
            int target = Integer.parseInt(path[i+1])-1;
            if (!bfs(cur, target)) {
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }

    static boolean bfs(int cur, int target){
        Queue<Integer> Q = new LinkedList<>();
        int[] visited = new int[n];
        visited[cur] = 1;
        Q.add(cur);
        while (Q.size() != 0){
            Integer city = Q.poll();
            if (city == target){
                return true;
            }
            for(int i=0; i<n; i++){
                if (M[city][i] == 0 || visited[i] == 1) continue;
                visited[i] = 1;
                Q.add(i);
            }
        }
        return false;
    }

}