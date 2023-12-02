import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int i=1, idx=0;
        while(i*(i+1)/2<n) {
            i++;
        }
        idx = n-i*(i-1)/2;
        System.out.print(i%2==0?(idx+"/"+(i-idx+1)):i-idx+1+"/"+idx);
    }
}