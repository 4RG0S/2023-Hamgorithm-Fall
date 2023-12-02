package baekjoon.p28278;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Main {
    public static int[] s_stack = new int[1_000_000];
    public static int s_top = -1;
    public static void Push(int data){
        s_stack[++s_top] = data;
    }
    public static int Pop(){
        if(IsStackEmpty()) return -1;
        return s_stack[s_top--];
    }
    public static int Peek(){
        if(IsStackEmpty()) return -1;
        return s_stack[s_top];
    }
    public static boolean IsStackEmpty(){
        return s_top == -1;
    }
    public static boolean IsStackFull(){
        return s_top == 1_000_000 - 1;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

            int cnt = Integer.parseInt(reader.readLine());

            String user;
            char digitStr;

            for (int i = 0; i < cnt; i++) {
                user = reader.readLine();
                digitStr = user.charAt(0);
                switch (digitStr) {
                    case '1':
                        Push(Integer.parseInt(user.substring(2)));
                        break;
                    case '2':
                        sb.append(Pop()).append("\n");
                        break;
                    case '3':
                        sb.append(s_top + 1).append("\n");
                        break;
                    case '4':
                        sb.append(IsStackEmpty() ? 1 : 0).append("\n");
                        break;
                    case '5':
                        sb.append(Peek()).append("\n");
                        break;
                }
            }
            reader.close();
            System.out.println(sb.toString());
    }

}
