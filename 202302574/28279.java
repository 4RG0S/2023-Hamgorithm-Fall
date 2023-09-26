import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Deque<Integer> deque = new ArrayDeque<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        for(int i=0; i<n; i++){
            String[] user = br.readLine().split(" ");
            switch(user[0].charAt(0)){
                case '1':
                    deque.addFirst(Integer.parseInt(user[1]));
                    break;
                case '2':
                    deque.addLast(Integer.parseInt(user[1]));
                    break;
                case '3':
                    sb.append(deque.isEmpty()?-1:deque.removeFirst()).append("\n");
                    break;
                case '4':
                    sb.append(deque.isEmpty()?-1:deque.removeLast()).append("\n");
                    break;
                case '5':
                    sb.append(deque.size()).append("\n");
                    break;
                case '6':
                    sb.append(deque.isEmpty()?1:0).append("\n");
                    break;
                case '7':
                    sb.append(deque.isEmpty()?-1:deque.getFirst()).append("\n");
                    break;
                case '8':
                    sb.append(deque.isEmpty()?-1:deque.getLast()).append("\n");
                    break;
            }
        }
        System.out.println(sb);
    }
}