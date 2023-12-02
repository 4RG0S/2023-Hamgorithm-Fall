import java.io.*;

public class Main {
    public static boolean[][] isblack;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] size = br.readLine().split(" ");
        int h = Integer.parseInt(size[0]);
        int w = Integer.parseInt(size[1]);

        isblack = new boolean[h][w];

        String blackWhite;
        for(int i=0; i<h; i++){
            blackWhite = br.readLine();
            for(int j=0; j<w; j++){
                if(blackWhite.charAt(j) == 'B')
                    isblack[i][j] = true;
            }
        }
        int cnt, min = 64;
        for(int i=0; i<=h-8; i++){
            for(int j=0; j<=w-8; j++){
                cnt = 0;
                for(int k=i; k<i+8; k++){
                    for(int l=j; l<j+8; l++){
                        if(k%2==0){
                            if(l%2==0){
                                if(isblack[k][l]) cnt++;
                            }
                            else{
                                if(!isblack[k][l]) cnt++;
                            }
                        }
                        else{
                            if(l%2==0){
                                if(!isblack[k][l]) cnt++;
                            }
                            else{
                                if(isblack[k][l]) cnt++;
                            }
                        }
                    }
                }
                cnt = Math.min(cnt, 64-cnt);
                min = Math.min(cnt, min);
            }
        }
        System.out.print(min);
    }
}