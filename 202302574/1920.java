import java.io.*;
import java.util.Arrays;

public class Main {
    public static int[] targets;
    
    public static boolean binarySearch(int key){
        int front = 0;
        int rear = targets.length-1;
        int mid = -1;
        while(front<=rear){
            mid = (front+rear)/2;
            if(key<targets[mid]){
                rear = mid-1;
            } else if(key>targets[mid]){
                front = mid+1;
            } else{
                return true;
            }
        }
        return false;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        targets = new int[n];

        String[] arr = br.readLine().split(" ");
        for(int i=0; i<n; i++) 
            targets[i] = Integer.parseInt(arr[i]);
        Arrays.sort(targets);

        int m = Integer.parseInt(br.readLine());
        String[] num = br.readLine().split(" ");

        for(int i=0; i<m; i++){
            int key = Integer.parseInt(num[i]);
            sb.append(binarySearch(key)?1:0).append("\n");
        }
        System.out.print(sb);
    }
}