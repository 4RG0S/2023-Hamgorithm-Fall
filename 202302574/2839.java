import java.io.*;

public class Main {
    public static int minCase(int k){
        int max = k/5;
        for(int i=max; i>=0; i--){
            for(int j=0; 5*i+3*j<=k; j++){
                if((5*i+3*j) == k) return i+j;
            }
        }
        return -1;
    }
    public static void main(String[] args) throws IOException { 
        //k에 대하여 5m + 3n = k(m, n은 음이 아닌 정수)를 만족시키는, m+n의 최솟값을 구하는 문제
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());

        System.out.print(minCase(k));
    }
}