import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] weightInfo = new int[n][2];
        int[] ans = new int[n];
        int[] color = new int[n];
        Map<Integer, Integer> colorInfo = new HashMap<>();

        for (int i=0; i<n; i++){
            String[] input = br.readLine().split(" ");
            int c = Integer.parseInt(input[0])-1;
            int w = Integer.parseInt(input[1]);
            colorInfo.put(i, c);
            weightInfo[i][0] = i;
            weightInfo[i][1] = w;
        }

        Arrays.sort(weightInfo, Comparator.comparing((int a[]) -> a[1]));

        int total = 0;
        ArrayList<Integer> prev = new ArrayList<>();
        Map<Integer, Integer> prevColor = new HashMap<>();

        ans[weightInfo[0][0]] = 0;
        prev.add(weightInfo[0][1]);
        prevColor.put(colorInfo.get(weightInfo[0][0]), 1);
        color[colorInfo.get(weightInfo[0][0])] += weightInfo[0][1];
        total += weightInfo[0][1];

        for(int i=1; i<n; i++){
            int idx = weightInfo[i][0];
            int w = weightInfo[i][1];
            int c = colorInfo.get(idx);

            ans[idx] = total-color[c]; // 컬러 같은 것

            // 컬러 다르고 무게 같은 것
            if (prev.get(prev.size()-1) == w){
                if (prevColor.containsKey(c)){
                    ans[idx] -= (prev.size() - prevColor.get(c))*w;
                    prevColor.put(c, prevColor.get(c)+1);
                }
                else {
                    ans[idx] -= (prev.size()*w);
                    prevColor.put(c, 1);
                }
                prev.add(w);
            }
            else{
                prev = new ArrayList<>();
                prevColor = new HashMap<>();
                prev.add(w);
                prevColor.put(c, 1);
            }
            total += w;
            color[c] += w;
        }


        for (int a : ans) {
            System.out.println(a);
        }

    }


}