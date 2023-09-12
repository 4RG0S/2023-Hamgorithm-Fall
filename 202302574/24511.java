package baekjoon.p24511;
import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        String[] idx = br.readLine().split(" ");
        String[] data = br.readLine().split(" ");

        int m = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");

        Deque<String> deque = new ArrayDeque<>();

        int i;
        for(i=0; i<n; i++){
            if(idx[i].equals("0"))
                deque.addLast(data[i]);
        }

        for(i=0; i<m; i++){
            deque.addFirst(input[i]);
            sb.append(deque.removeLast()).append(" ");
        }
        System.out.println(sb);
    }
}
