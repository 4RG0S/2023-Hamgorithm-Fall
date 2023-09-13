package baekjoon.p18258;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static final int QUEUESIZE = 2_000_000;
    public static int[] queue = new int[QUEUESIZE];
    public static int rear = -1;
    public static int front = -1;
    public static void Push(int data){
        rear = (rear+1)%QUEUESIZE;
        queue[rear] = data;
    }
    public static int Pop(){
        if(IsQueueEmpty()) return -1;
        front = (front+1)%QUEUESIZE;
        return queue[front];
    }
    public static int PeekFront(){
        if(IsQueueEmpty()) return -1;
        int NewFront = (front+1)%QUEUESIZE;
        return queue[NewFront];
    }
    public static int PeekRear(){
        if(IsQueueEmpty()) return -1;
        return queue[rear];
    }
    public static boolean IsQueueEmpty(){
        return rear == front;
    }
    public static int Size(){
        if(rear<front) return rear+(QUEUESIZE-front);
        return rear-front;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        String user;
        for(int i=0; i<n; i++){
            user = br.readLine();
            if(user.equals("pop")){
                sb.append(Pop()).append("\n");
            }
            else if(user.equals("size")){
                sb.append(Size()).append("\n");
            }
            else if(user.equals("empty")){
                if(IsQueueEmpty()) sb.append("1").append("\n");
                else sb.append("0").append("\n");
            }
            else if(user.equals("front")){
                sb.append(PeekFront()).append("\n");
            }
            else if(user.equals("back")){
                sb.append(PeekRear()).append("\n");
            }
            else{
                Push(Integer.parseInt(user.substring(5)));
            }
        }
        System.out.println(sb);
    }
}
