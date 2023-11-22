import java.io.*;
import java.util.*;

class Point implements Comparable<Point>{
    int x, y;
    Point(int x, int y){
        this.x = x;
        this.y = y;
    }
    String getString(){
        return x + " " + y;
    }
    @Override
    public int compareTo(Point p) {
        if(y>p.y) return 1;
        else if(y<p.y) return -1;
        else return Integer.compare(x, p.x);
    }
}
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        String[] coordinate;
        List<Point> arrP = new ArrayList<>(n);
        for(int i=0; i<n; i++){
            coordinate = br.readLine().split(" ");
            arrP.add(new Point(Integer.parseInt(coordinate[0]), Integer.parseInt(coordinate[1])));
        }

        Collections.sort(arrP);

        StringBuilder sb = new StringBuilder();
        for(Point p : arrP){
            sb.append(p.getString()).append("\n");
        }
        System.out.print(sb);
    }
}