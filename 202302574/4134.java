import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static boolean isPrime(long a){
        if(a==0 || a==1) return false;
        for(long i=2; i*i<=a; i++){
            if(a%i==0) return false;
        }
        return true;
    }
    public static long nextPrime(long a){
        while(true){
            if(isPrime(a)) return a;
            a++;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        long n = Integer.parseInt(br.readLine());
        for(long i=0; i<n; i++){
            long user = Long.parseLong(br.readLine());
            sb.append(nextPrime(user)).append("\n");
        }
        System.out.println(sb);
    }
}