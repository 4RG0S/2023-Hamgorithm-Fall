import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        int cnt = 0, end;

        for(end=666; cnt<n; end++){
            if(String.valueOf(end).contains("666"))
                cnt++;
        }

        System.out.print(end-1);
    }
}