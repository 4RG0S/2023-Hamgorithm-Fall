import java.io.*;

public class Main {
    public static int GCD(int a, int b) {
        if (a == 0) return b;
        return GCD(b % a, a);
    }
    public static int LCM(int a, int b){
        return a*b/GCD(a, b);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Fraction f1 = new Fraction();
        Fraction f2 = new Fraction();

        String[] arr1 = br.readLine().split(" ");
        String[] arr2 = br.readLine().split(" ");

        f1.n = Integer.parseInt(arr1[0]);
        f1.d = Integer.parseInt(arr1[1]);
        f2.n = Integer.parseInt(arr2[0]);
        f2.d = Integer.parseInt(arr2[1]);
        f1.renew();
        f2.renew();

        Fraction fNew = new Fraction();
        fNew = fNew.plus(f1, f2);

        System.out.printf("%d %d", fNew.n, fNew.d);
    }
}
class Fraction {
    int n, d;//분자 : numerator, 분모 : denominator
    public void renew(){
        int gcd = Main.GCD(n, d);
        n /= gcd;
        d /= gcd;
    }
    public Fraction plus(Fraction f1, Fraction f2){
        Fraction fNew = new Fraction();

        int lcm = Main.LCM(f1.d, f2.d);
        int temp1 = lcm/f1.d;
        int temp2 = lcm/f2.d;

        fNew.n = temp1*f1.n + temp2*f2.n;
        fNew.d = lcm;
        fNew.renew();
        return fNew;
    }
}