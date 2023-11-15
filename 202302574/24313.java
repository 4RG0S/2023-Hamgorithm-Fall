import java.io.*;

public class Main {
    public static boolean isO(int a1, int a0, int c, int n0) {
        if (c < a1) return false;
        if (c == a1) return a0 <= 0;
        return a1 <= n0 * (c - a1);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] a = br.readLine().split(" ");
        int a1 = Integer.parseInt(a[0]), a0 = Integer.parseInt(a[1]);

        int c = Integer.parseInt(br.readLine()), n0 = Integer.parseInt(br.readLine());

        System.out.print(isO(a1, a0, c, n0) ? "1" : "0");
    }
}