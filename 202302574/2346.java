import java.io.*;
import java.util.*;

public class Main {
    public static int N, idx = -1;// 마지막으로 출력한 원소의 인덱스값
    
    public static int[] queue;// 원소값은 풍선 안에 들어있는 종이에 적혀있는 값
    public static boolean[] visited;
    
    public static int popN(int n){
        int count = 0;
        int s = n<0?-1:1;
        while(true) {
            if (count == n*s) break;
            idx = ((idx + s) + N) % N;
            if (!visited[idx]) count++;
        }
        visited[idx] = true;
        return idx+1;
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        String[] temp = br.readLine().split(" ");

        visited = new boolean[N];
        queue = new int[N];
        for(int i=0; i<N; i++)
            queue[i] = Integer.parseInt(temp[i]);

        int end = 1;
        for(int i=0; i<N; i++){
            sb.append(popN(end)).append(" ");
            end = queue[idx];
        }
        System.out.println(sb);
    }
}