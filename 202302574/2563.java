import java.io.*;

public class Main {
    public static boolean[][] isBlack = new boolean[100][100];
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        String[] coordinate;
        int x, y;
        for(int i=0; i<n; i++){
            coordinate = br.readLine().split(" ");
            x = Integer.parseInt(coordinate[0]); // 1 <= x,y <= 100
            y = Integer.parseInt(coordinate[1]);

            for(int j=0; j<10; j++){
                for(int k=0; k<10; k++){
                    isBlack[x+j][y+k] = true;
                }
            }
        }
        
        int cnt=0;
        for(int i=0; i<100; i++){
            for(int j=0; j<100; j++){
                if(isBlack[i][j]) cnt++;
            }
        }
        System.out.print(cnt);
    }
}