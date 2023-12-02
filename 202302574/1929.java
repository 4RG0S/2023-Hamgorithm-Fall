import java.io.*;

public class Main {
    public static boolean isPrime(int a){
        if(a==1) return false;
        for(long i=2; i*i<=a; i++){
            if(a%i==0) return false;
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] user = br.readLine().split(" ");
        int from = Integer.parseInt(user[0]);
        int to = Integer.parseInt(user[1]);
        for(int i=from; i<=to; i++){
            if(isPrime(i)) sb.append(i).append("\n");
        }
        System.out.println(sb);
    }
}