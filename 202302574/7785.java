import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Set<String> set = new HashSet<>();
        List<String> list;
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        String[] in;
        String name;
        for(int i=0; i<n; i++){
            in = br.readLine().split(" ");
            name = in[0];
            if(!set.contains(name)) set.add(name);
            else set.remove(name);
        }

        list = new ArrayList<>(set);
        list.sort(Collections.reverseOrder());

        for(String s : list)
            sb.append(s).append("\n");
        
        System.out.print(sb);
    }
}