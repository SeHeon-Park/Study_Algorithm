import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {

    static int[] p;

    static class Edge implements Comparable<Edge>{
        int current;
        int target;
        int cost;

        Edge(int current, int target, int cost){
            this.current = current;
            this.target = target;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge o) {
            return this.cost- o.cost;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        p = new int[n];
        for (int i=0; i<n; i++) p[i] = i;
        PriorityQueue<Edge> Q = new PriorityQueue<>();
        for (int i=0; i<m; i++){
            String[] info = br.readLine().split(" ");
            Q.add(new Edge(Integer.parseInt(info[0])-1,
                    Integer.parseInt(info[1])-1, Integer.parseInt(info[2])));
        }
        int ans=0;
        while (!Q.isEmpty()){
            Edge e = Q.poll();
            if (union(e.current, e.target)){
                ans += e.cost;
            }
        }
        System.out.println(ans);
    }

    static int findParent(int a){
        if (p[a] != a) p[a] = findParent(p[a]);
        return p[a];
    }

    static boolean union(int a, int b){
        a = findParent(a);
        b = findParent(b);
        if (a == b) return false;
        p[a] = b;
        return true;
    }


}
