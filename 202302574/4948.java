import java.io.*;

public class Main {
    public static final int N = 2*123_456;
    public static boolean[] isPrime = new boolean[N+1];
    public static void clear(){
        int i, j;
        
        for(i=2; i<=N; i++)
            isPrime[i] = true;

        for(i=2; i*i<=N; i++){
            if(isPrime[i]) {
                for (j = i * i; j <= N; j += i)
                    isPrime[j] = false;
            }
        }
    }
    public static int cntPrime(int n){
        int cnt=0;
        for(int i=n+1; i<=2*n; i++) {
            if (isPrime[i]) cnt++;
        }
        return cnt;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        clear();
        int num;

        while(true){
            num = Integer.parseInt(br.readLine());
            if(num==0) break;
            sb.append(cntPrime(num)).append("\n");
        }
        System.out.print(sb);
    }
}