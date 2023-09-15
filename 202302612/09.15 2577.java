import java.util.*;
public class Main{
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int A= sc.nextInt();
		int B =sc.nextInt();
		int C = sc.nextInt();
		int D = A*B*C;
		
		int [] arr = new int[10];
	
		String ch = Integer.toString(D);
		
		 
		   for(int j =0; j<ch.length(); j++) {
			   char sibal = ch.charAt(j);
			   if(sibal >= '0' && sibal <= '9') {
				   int bibal = sibal - '0';
				   arr[bibal] += 1;
				   
			   }
		   }
		
		   
		   for(int k = 0; k<10; k++) {
			   System.out.println(arr[k]);
			   }
		   
		   }
		   }
		   


