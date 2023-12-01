import java.util.Scanner;
 
public class Main {
	public static int argora(int a,int b, int c) {
		if(a > b && a> c) {
			return 1;
		}
		else if ( b> a && b > c) {
			return 0;
		}
		else if (c > a && c > b) {
			return -1;
		}
		else {
		return 2;
	}
	}

 
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
	
		while (true) {
		
		int a = in.nextInt();
		int b = in.nextInt();
		int c = in.nextInt();
	
		if(a == 0 && b == 0 && c ==0) {
			break;
		}
		else {
			
			if(argora(a,b,c) == 1) {
				if(a*a == b*b + c*c) {
					System.out.println("right");
				}
				else {
					System.out.println("wrong");
				}
				
			}
			else if (argora(a,b,c) == 0) {
				if (b*b == a*a + c*c) {
					System.out.println("right");
				}
				else{
					System.out.println("wrong");
				}
			}
			else if (argora(a,b,c) == -1) {
				if(c*c == a*a + b*b) {System.out.println("right");
			}
				else {
					System.out.println("wrong");
				}
				
			
		}
			else if(argora(a,b,c) == 2) {
				System.out.println("wrong");
			}
			
	}}
}
}
	