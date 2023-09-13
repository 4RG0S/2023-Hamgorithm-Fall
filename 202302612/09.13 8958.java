import java.util.*;
public class Main{
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int b = sc.nextInt();
		String a = null;
		int cnt = 0;
		
		for(int i =0; i<b; i++) {
			int c= 0;
			cnt = 0;
			 a = sc.next();
			for(int j = 0; j<a.length(); j++) {
				if(a.charAt(j) == 'O') {
					cnt ++;
					c = c + cnt;
				}
				else if(a.charAt(j) == 'X'){
					cnt = 0;
				}
				
			}
			
			System.out.println(c);
			
		}
		
		
	
	
	}
}