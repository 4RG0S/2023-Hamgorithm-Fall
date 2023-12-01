import java.util.*;


 
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int count = 0;
		int arr [] = new int[5];
		
		for (int i = 0; i<5; i++) {
			arr[i]= sc.nextInt();
			count += arr[i];
		}
		int avg = count/5;
		Arrays.sort(arr);
	
	
	System.out.println(avg);
	System.out.println(arr[2]);
	}
}

	