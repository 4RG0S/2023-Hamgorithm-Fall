import java.io.*;

public class Main {
    public static long combination(int n, int r){ //nCr = n!/(r!*(n-r)!)
        long result = 1, temp = 1;
        int min = Math.min(n - r, r);
        int max = Math.max(n - r, r);
        for(int i=max+1; i<=n; i++) result*=i;
        for(int i=1; i<=min; i++) result/=i;
        return result;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int num = Integer.parseInt(br.readLine());
        int m, n;
        for(int i=0; i<num; i++){
            String[] arr = br.readLine().split(" ");
            m = Integer.parseInt(arr[0]);
            n = Integer.parseInt(arr[1]);
            sb.append(combination(n,m)).append("\n");
        }
        System.out.print(sb);
    }
}