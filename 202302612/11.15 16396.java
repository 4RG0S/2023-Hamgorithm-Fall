import java.util.*;

 
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int c = 0;
		int count = 0;
		int [] arr = new int[10001];
		for (int i = 0; i<a; i++) {
			int b = sc.nextInt();
			int d = sc.nextInt();
				
			for(int j = b; j<d; j++) {
				arr[j] = 1;
			}
	
		}for(int k = 0; k<10001; k++) {
			count += arr[k];
		}
		System.out.println(count);
		
		
		
	}
}
		
	