package baekjoon.queue_stack_deque.p12789;

import java.io.*;
import java.util.Stack;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int len = Integer.parseInt(br.readLine());
        String[] numbersStr = br.readLine().split(" ");

        int[] numbers = new int[len];
        for(int i=0; i<len; i++)
            numbers[i] = Integer.parseInt(numbersStr[i]);

        Stack<Integer> numberStack = new Stack<>();
        // 3, 2, 1, 4, 5
        int cnt = 1, i = 0;

        while(i<len){
            if(numbers[i] == cnt){
                cnt++; i++;
            }
            else if(!numberStack.isEmpty() && numberStack.peek() == cnt){
                cnt++;
                numberStack.pop();
            }
            else {
                numberStack.push(numbers[i++]);
            }
        }
        while(!numberStack.isEmpty()){
            if(cnt!=numberStack.pop()) break;
            else cnt++;
        }
        System.out.println(cnt==len+1?"Nice":"Sad");
    }
}
