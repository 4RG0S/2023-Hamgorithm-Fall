import java.io.*;


public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int L = Integer.parseInt(br.readLine());
		String S = br.readLine();
		long rs = 0;
		long p = 1;
		for(int i = 0; i < L; i++) {
			rs += ((S.charAt(i) - 96) * p);
			
			p = (p * 31) % 1234567891;
		}
		System.out.println(rs % 1234567891);
	}

}