import java.io.*;

public class Main {
    public static boolean isGroup(String voca){
        boolean[] isCheck = new boolean[26];
        
        char unit = voca.charAt(0), nextUnit;
        isCheck[(int)unit-'a'] = true;
        
        for(int i=1; i<voca.length(); i++){
            nextUnit = voca.charAt(i);
            if(unit != nextUnit){
                if(isCheck[(int)nextUnit-'a'])
                    return false;
                else
                    isCheck[(int)nextUnit-'a'] = true;
            }
            unit = nextUnit;
        }
        return true;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        int cnt = 0;
        for(int i=0; i<num; i++){
            String voca = br.readLine();
            if(isGroup(voca)) cnt++;
        }
        System.out.print(cnt);
    }
}