import java.util.*;

 
public class Main {
	public static void main(String[] args)  {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		int f = 1;
		int s = 1;
		
		for(int i = 0; i<b; i++) {
			f *= (a- i);
			s *= (i + 1);
			
		}
		System.out.println(f/s);
	
	}
}



