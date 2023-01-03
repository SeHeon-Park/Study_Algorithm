import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;


public class Main {

    static Map<Integer, ArrayList<Integer>> P;
    static Map<Integer, Integer> A;
    static Queue<Integer> Q;
    static ArrayList<Integer> ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);
        Q = new PriorityQueue<>();
        P = new HashMap<>();
        A = new HashMap<>();
        ans = new ArrayList<>();
        for (int i=0; i<n; i++){
            A.put(i+1, 0);
        }

        for (int i=0; i<m; i++){
            String[] prev = br.readLine().split(" ");
            int a = Integer.parseInt(prev[0]);
            int b = Integer.parseInt(prev[1]);
            A.put(b, A.get(b)+1);
            if (P.containsKey(a)){
                ArrayList<Integer> I = P.get(a);
                I.add(b);
            }
            else {
                ArrayList<Integer> temp = new ArrayList<>();
                temp.add(b);
                P.put(a, temp);
            }
        }

        for (Map.Entry<Integer, Integer> e : A.entrySet()) {
            if (e.getValue() == 0){
                Q.add(e.getKey());
            }
        }

        while (!Q.isEmpty()){
            Integer number = Q.poll();
            ans.add(number);
            if (P.containsKey(number)){
                ArrayList<Integer> info = P.get(number);
                for (Integer i : info) {
                    A.put(i, A.get(i)-1);
                    if (A.get(i) == 0) Q.add(i);
                }
            }
        }

        for (Integer a : ans) {
            System.out.print(a + " ");
        }

    }



}