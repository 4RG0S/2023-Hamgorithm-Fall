import java.io.*;

public class Main {
    public static double getScore(String str) {
        char a = str.charAt(0);
        if(a == 'F') return 0.0;
        char b = str.charAt(1);
        return (4.0 - (int)(a - 'A')) + (b == '0' ? 0 : 0.5);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double score, credit, sum=0, n=0;
        int cnt = 0;
        for(int i=0; i<20; i++){
            String[] arr = br.readLine().split(" ");
            credit = Double.parseDouble(arr[1]);
            if(arr[2].charAt(0) == 'P')
                continue;
            score = getScore(arr[2]);
            sum += credit * score;
            n+=credit;
        }
        System.out.print(sum/n);
    }
}