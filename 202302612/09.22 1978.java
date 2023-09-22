import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int count = 0;
        for(int i =0; i<N; i++) {
        	int c = sc.nextInt();
        	
        	if(num(c)) {
        		count++;
        	
        	}
        	
		}
        System.out.println(count);
 
	
	}
	
	
	public static boolean num(int n) {
		if(n != 1) {
		for(int k = 2; k<n; k++) {
			if(n%k == 0) {
				return false;
			}
			
			
		}
		return true;
		}
		return false;
}
}
