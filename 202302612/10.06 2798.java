import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int m = Integer.MIN_VALUE; 
        int[] arr = new int[a];

        for (int i = 0; i < a; i++) {
            arr[i] = sc.nextInt();
        }

        for (int j = 0; j < a; j++) {
            for (int k = j + 1; k < a; k++) {
                for (int l = k + 1; l < a; l++) {
                    int c = arr[j] + arr[k] + arr[l];
                    if (c <= b && c > m) {
                        m = c;
                    }
                }
            }
        }

        System.out.println(m);
    }
}
