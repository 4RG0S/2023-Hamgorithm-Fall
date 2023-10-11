package baekjoon.recursive_function.p2447;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Main {
    public static boolean[][] isBlank;
    public static int max;
    public static void star(int n){
        if(n==0) return;
        for(int i=0; i<max; i++){
            for(int j=0; j<max; j++) {
                if ((i/n)%3 == 1 && (j/n)%3 == 1)
                    // (i/100)%10 => 10진법상 뒤에서 셋째(100) 자릿수 ex) (1234/100)%10 = 2
                    // 마찬가지로, i에 대하여 n = 3^k일 때, 3진법상 뒤에서 (k+1)번째 자릿수가 (i/n)%3이다.
                    isBlank[i][j] = true;

            }
        }
        star(n/3);

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        isBlank = new boolean[n][n]; max = n;
        star(n);

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                sb.append(isBlank[i][j]?" ":"*");
            }
            sb.append("\n");
        }

        System.out.print(sb);
    }
}

//public class Main {
//    public static boolean[][] isBlank;
//    public static void star(int n){
//        if(n==1) return;
//        for(int i=0; i<n; i++){
//            for(int j=0; j<n; j++) {
//                if ( (i/n)%3 == 1 && (j/n)%3 == 1)
//                    isBlank[i][j] = true;
//            }
//        }
//        star(n/3);
//
//    }
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringBuilder sb = new StringBuilder();
//
//        int n = Integer.parseInt(br.readLine());
//        isBlank = new boolean[n][n];
//        star(n);
//
//        for(int i=0; i<n; i++){
//            for(int j=0; j<n; j++){
//                sb.append(isBlank[i][j]?"*":" ");
//            }
//            sb.append("\n");
//        }
//
//        System.out.print(sb);
//    }
//}
