import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        HashSet<Integer> set = new HashSet<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        String[] strSet = br.readLine().split(" ");

        for(String s : strSet)
            set.add(Integer.parseInt(s));

        int m = Integer.parseInt(br.readLine());

        String[] targets = br.readLine().split(" ");
        StringBuilder sb = new StringBuilder();

        for(String s : targets){
                sb.append(set.contains(Integer.parseInt(s))?1:0).append(" ");
        }
        System.out.print(sb);
    }
}