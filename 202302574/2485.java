import java.io.*;

public class Main {
    public static int GCD(int a, int b){
        if(a==0) return b;
        return GCD(b%a, a);
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int i, point, pointNew;
        
        int n = Integer.parseInt(br.readLine());
        int[] intervals = new int[n-1]; // 가로수 사이의 간격을 저장하는 배열
        
        point = Integer.parseInt(br.readLine());
        for(i=0; i<n-1; i++){
            pointNew = Integer.parseInt(br.readLine());
            intervals[i] = pointNew - point;
            point = pointNew;
        }
        
        int gcdIntervals, sum = 0; 
        // 간격들의 최대공약수를 구하고, 위의 각 배열 요소에서 구한 최대공약수를 나누고 1을 빼서 모두 더한다.

        gcdIntervals = intervals[0];
        for(i=1; i<n-1; i++)
            gcdIntervals = GCD(gcdIntervals, intervals[i]);
        
        for(i=0; i<n-1; i++)
            sum+= intervals[i]/gcdIntervals-1;
       
        System.out.print(sum);
    }
}