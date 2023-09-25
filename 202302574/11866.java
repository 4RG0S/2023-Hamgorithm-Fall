import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main  {
    public static boolean[] visited;
    public static int N, K, cnt = 1, idx = -1;//가장 마지막으로 방문한 인덱스값
    public static int popN(){
        int count = 0;
        while(true) {
            if (count == K) break;
            idx = (idx + 1) % N;
            if (!visited[idx]) count++;
        }
        visited[idx] = true;
        return idx+1;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] arr = br.readLine().split(" ");
        N = Integer.parseInt(arr[0]);
        K = Integer.parseInt(arr[1]);

        visited = new boolean[N];

        sb.append("<");
        while(cnt<N){
            sb.append(popN()).append(", ");
            cnt++;
        }
        sb.append(popN()).append(">");

        System.out.println(sb);
    }
}
