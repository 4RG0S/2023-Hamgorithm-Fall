import java.io.*;

public class Main {
    public static int max;
    public static boolean[] isBlank;
    
    public static void setBlank(int n){
        if(n==0) return;
        for(int i=0; i<max; i++){
            if((i/n)%3==1) isBlank[i] = true;
        }
        setBlank(n/3);
    }
    
    public static int setMax(int n){
        int temp = 1;
        for(int i=0; i<n; i++)
            temp*=3;
        return temp;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int temp = 1, n;

        String input;
        while((input = br.readLine()) != null){
            n = Integer.parseInt(input);
            max = setMax(n);

            isBlank = new boolean[max];
            setBlank(max);

            for(int i=0; i<max; i++)
                sb.append(isBlank[i]?" ":"-");

            sb.append("\n");
        }
        System.out.print(sb);
    }
}