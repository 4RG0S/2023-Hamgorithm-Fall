import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int i, cnt=0;
        int n = Integer.parseInt(br.readLine());
        
        for(i=1; i*i<=n; i++)
            cnt++;
        
        System.out.print(cnt);
    }
}