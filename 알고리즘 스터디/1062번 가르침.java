import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int k;
    static int[] alp;
    static ArrayList<String> arr;
    static int ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        k = Integer.parseInt(input[1])-5;
        if (k < 0){
            System.out.println(0);
            return;
        }
        arr = new ArrayList<>();
        alp = new int[26];
        alp[(int)'a'-97] = 1;
        alp[(int)'n'-97] = 1;
        alp[(int)'t'-97] = 1;
        alp[(int)'i'-97] = 1;
        alp[(int)'c'-97] = 1;
        for (int i=0; i<n; i++){
            arr.add(br.readLine());
        }
        dfs(0, 0);
        System.out.println(ans);
    }

    static void dfs(int idx, int cnt){
        if (cnt == k){ // 2. 목적지 인가
            int temp = 0;
            for (String s : arr) {
                for(int i=4; i<s.length()-3; i++){
                    if (alp[(int)s.charAt(i)-97] == 0) {
                        temp -= 1;
                        break;
                    }
                }
                temp += 1;
            }
            ans = Math.max(ans, temp);
            return;
        }
        for (int i=idx; i<26; i++){ // 3. 연결된 곳을 순회
            if (alp[i] == 1) continue; // 4. 갈 수 있는가?
            alp[i] = 1; // 1. 체크인
            dfs(i+1, cnt+1); // 5. 간다
            alp[i] = 0; // 6. 체크아웃
        }
    }

}
