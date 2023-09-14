package baekjoon.p10773;
import java.io.*;

public class Main {
    public static final int STACKSIZE = 1_000_000;
    public static int[] stack = new int[STACKSIZE];
    public static int top = -1;
    public static int Pop(){
        return stack[top--];
    }
    public static void Push(int data){
        stack[++top] = data;
    }
    public static boolean IsStackEmpty(){
        return top == -1;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++){
            int user = Integer.parseInt(br.readLine());
            if(user == 0) Pop();
            else Push(user);
        }
        int sum = 0;
        while(true){
            if(IsStackEmpty()) break;
            sum+= Pop();
        }
        System.out.println(sum);
    }
}
