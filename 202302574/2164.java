import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<Integer> queue = new ArrayDeque<>();

        int n = Integer.parseInt(br.readLine());
        int i, card;
        for(i=1; i<=n; i++)
            queue.addLast(i);
        while(queue.size() != 1) {
            queue.removeFirst();
            card = queue.removeFirst();
            queue.addLast(card);
        }
        System.out.println(queue.removeFirst());
    }
}