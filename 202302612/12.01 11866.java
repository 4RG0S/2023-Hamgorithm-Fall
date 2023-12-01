import java.util.Scanner;
import java.util.LinkedList;
 
public class Main {
 
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);	
		LinkedList<Integer> list = new LinkedList<Integer>();
 
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		for(int i = 1; i <= a; i++) {
			list.add(i);
		}
		
		
		StringBuilder sb = new StringBuilder();
		sb.append('<');
		
		int index = 0;	
		
		while(list.size() > 1) {
			index = (index + ( b- 1)) % list.size();
			
			 
			sb.append(list.remove(index)).append(", ");
		}
		sb.append(list.remove()).append('>');
		System.out.println(sb);
	}
}