import java.util.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();

        for (int i = 0; i < a; i++) {
            int b = sc.nextInt();
            int c = sc.nextInt();

            if (b == c) {
                System.out.println("1");
            } else {
                BigInteger qwar = new BigInteger("1");
                BigInteger qwbr = new BigInteger("1");
                BigInteger qwcr = new BigInteger("1");

                for (int j = b; j > 0; j--) {
                    qwar = qwar.multiply(BigInteger.valueOf(j));
                }

                for (int k = c; k > 0; k--) {
                    qwbr = qwbr.multiply(BigInteger.valueOf(k));
                }

                for (int r = (c - b); r > 0; r--) {
                    qwcr = qwcr.multiply(BigInteger.valueOf(r));
                }

                BigInteger result = qwbr.divide(qwcr.multiply(qwar));
                System.out.println(result);
            }
        }
    }
}
