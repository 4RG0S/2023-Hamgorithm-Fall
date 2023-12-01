import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(true) {
        	int a = sc.nextInt();
        	if( a == 0 ) {
        		break;
        	}
        	else {
        		String b = Integer.toString(a);
        		String[] arr = new String[b.length()];
        		for (int i = 0; i < b.length(); i++) {
                 arr[i] = String.valueOf(b.charAt(i));
             }
        		  if (isPalindrome(arr)) {
        	            System.out.println("yes");
        	        } else {
        	            System.out.println("no");
        	        }

        
        	}
        }
    
    
    
    }
    public static boolean isPalindrome(String[] arr) {
        int left = 0;
        int right = arr.length - 1;
        
        while (left < right) {
            if (!arr[left].equals(arr[right])) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
}