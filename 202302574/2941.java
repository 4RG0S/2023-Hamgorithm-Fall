import java.util.Scanner;
public class Main {
    public static int numAlpha(String str){
        int idx = 0, len = str.length();
        int cnt = 0;
        while(idx<len-1){
            char unit = str.charAt(idx);
            char nextUnit = str.charAt(idx+1);
            if(unit == 'c'){
                if( nextUnit == '='|| nextUnit == '-')
                    idx++;
            } else if(unit == 'd'){
                if(nextUnit == '-')
                    idx++;
                else if(nextUnit == 'z' && idx<len-2 && str.charAt(idx+2) == '=')
                    idx+=2;
            } else if(unit == 'l' && nextUnit == 'j'){
                idx++;
            } else if(unit == 'n' && nextUnit == 'j'){
                idx++;
            } else if(unit == 's' && nextUnit == '='){
                idx++;
            } else if(unit == 'z' && nextUnit == '='){
                idx++;
            }
            idx++; cnt++;
        }
        return cnt+((idx==len-1)?1:0);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String voca = sc.next();
        System.out.print(numAlpha(voca));
    }
}