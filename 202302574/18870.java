import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<Integer, Integer> map = new HashMap<>();

        int num = Integer.parseInt(br.readLine());
        String[] str = br.readLine().split(" ");
        int[] sortedArr = new int[num];

        for(int i=0; i<num; i++)
            sortedArr[i] = Integer.parseInt(str[i]);

        Arrays.sort(sortedArr);

        int rank = 0;
        for(int key : sortedArr) {
            if (!map.containsKey(key))
                map.put(key, rank++);
        }

        StringBuilder sb = new StringBuilder();
        for(int i=0; i<num; i++){
            sb.append(map.get(Integer.parseInt(str[i]))).append(" ");
        }

        System.out.print(sb);
    }
}