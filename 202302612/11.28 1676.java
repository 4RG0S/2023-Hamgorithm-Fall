import java.util.*;

 
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int count = 0;
		for (int i = 0; i<n; i++) {
			count += n/5;
			n /=5;
			
			
			}
		
		System.out.println(count);
	}
}