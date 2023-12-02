package baekjoon.queue_stack_deque.p9012;
import java.util.Stack;
import java.io.*;
public class Main {
    public static boolean VPS(String arr){
        Stack<Character> stack = new Stack<>();

        for(int i=0; i<arr.length(); i++){
            if(arr.charAt(i) == '(') stack.push('(');
            else if(!stack.isEmpty()) stack.pop();
            else return false;
        }
        return stack.isEmpty();
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++){
            if(VPS(br.readLine())) sb.append("YES").append('\n');
            else sb.append("NO").append('\n');
        }
        System.out.print(sb);
    }
}