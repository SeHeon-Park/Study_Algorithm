import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int[][] M;
    static int[][] dxy = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};
    static int n;
    static int k;

    static class Node{
        public int x;
        public int y;
        public ArrayList<Integer> n;

        public Node(int x, int y, int number){
            this.x = x;
            this.y = y;
            n = new ArrayList<>();
            n.add(number);
        }
        public Node(int x, int y){
            this.x = x;
            this.y = y;
            n = new ArrayList<>();
        }

        public void addTokens(ArrayList<Integer> t){
            n.addAll(t);
        }

        public ArrayList<Integer> removeTokens(int number){
            ArrayList<Integer> temp1 = new ArrayList<>();
            int idx = 0;
            for (int i=0; i<n.size(); i++){
                if (n.get(i) == number){
                    idx = i;
                    break;
                }
                temp1.add(n.get(i));
            }

            ArrayList<Integer> temp2 = new ArrayList<>();

            for (int j=idx; j<n.size(); j++){
                temp2.add(n.get(j));
            }
            this.n = temp1;
            return temp2;
        }


        public Node findNode(int x, int y){
            if (this.x==x && this.y==y)
                return this;
            return null;
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        k = Integer.parseInt(input[1]);
        M = new int[n][n];
        for (int i=0; i<n; i++){
            String[] m = br.readLine().split(" ");
            for (int j=0; j<n; j++){
                M[i][j] = Integer.parseInt(m[j]);
            }
        }

        ArrayList<Node> N = new ArrayList<>();
        HashMap<Integer, Integer> dir = new HashMap<>();
        HashMap<Integer, Integer[]> location = new HashMap<>();

        for (int i=0; i<k; i++){
            String[] m = br.readLine().split(" ");
            int y = Integer.parseInt(m[0])-1;
            int x = Integer.parseInt(m[1])-1;
            int d = Integer.parseInt(m[2])-1;

            N.add(new Node(x, y, i+1));
            dir.put(i+1, d);
            location.put(i+1, new Integer[]{x, y});
        }

        int ans = 1;
        outerLoop:
        while (true){
            for (int i=1; i<k+1; i++){
                Integer[] l = location.get(i);
                Integer d = dir.get(i);

                int x = l[0]+dxy[d][0];
                int y = l[1]+dxy[d][1];

                // 다음 곳이 벽 or 파란색
                if (x<0 || x>n-1 || y<0 || y>n-1 || M[y][x]==2){
                    if (d == 0) d=1;
                    else if (d == 1) d=0;
                    else if (d == 2) d=3;
                    else  d=2;
                    dir.put(i, d);
                }

                int nx = l[0]+dxy[d][0];
                int ny = l[1]+dxy[d][1];

                // 벽 or 파란색 (안움직임)
                if (nx<0 || nx>n-1 || ny<0 || ny>n-1 || M[ny][nx]==2){
                    continue;
                }

                // 현재 위치 노드 찾기
                Node cur = null;
                for (Node node : N) {
                    Node temp = node.findNode(l[0], l[1]);
                    if (temp != null) {
                        cur = temp;
                        break;
                    }
                }

                ArrayList<Integer> na = cur.removeTokens(i);

                if (cur.n.size() == 0) {
                    N.remove(cur);
                }

                for (Integer number : na) {
                    location.put(number, new Integer[]{nx, ny});
                }

                Node cur2 = null;
                for (Node node : N) {
                    Node temp = node.findNode(nx, ny);
                    if (temp != null) {
                        cur2 = temp;
                        break;
                    }
                }

                if (cur2 == null){
                    Node node = new Node(nx, ny);
                    cur2 = node;
                    N.add(node);
                }


                // 하얀색
                if (M[ny][nx] == 0){
                    cur2.addTokens(na);
                }
                // 빨간색
                else if (M[ny][nx] == 1){
                    Collections.reverse(na);
                    cur2.addTokens(na);
                }

                if (cur2.n.size() >= 4){
                    break outerLoop;
                }

            }
            ans += 1;
            if (ans > 1000) {
                ans = -1;
                break ;
            }
        }

        System.out.println(ans);

    }



}