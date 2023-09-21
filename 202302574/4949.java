package baekjoon.queue_stack_deque.p4949;

import java.io.*;
import java.util.Stack;

public class Main {
    public static String equ(String str){
        Stack<Character> stack = new Stack<>();
        for(int i=0; i<str.length(); i++){
            char ch = str.charAt(i);
            if(ch == '(') stack.push(ch);
            else if(ch == '[') stack.push(ch);
            else if(ch == ')'){
                if(stack.isEmpty()) return "no";
                else if(stack.peek() == '(') stack.pop();
                else return "no";
            }
            else if(ch == ']'){
                if(stack.isEmpty()) return "no";
                else if(stack.peek() == '[') stack.pop();
                else return "no";
            }
        }
        if(stack.isEmpty()) return "yes";
        else return "no";
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        StringBuilder sb = new StringBuilder();

        while(true){
            String str = br.readLine();
            if(str.equals(".")) break;
            sb.append(equ(str)).append("\n");
        }
        System.out.println(sb);
    }
}