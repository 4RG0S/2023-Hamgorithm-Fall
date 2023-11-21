import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Character> list = new ArrayList<>();
        StringBuilder sb = new StringBuilder();

        String input = br.readLine();
        for(int i=0; i<input.length(); i++){
            list.add(input.charAt(i));
        }

        list.sort(Comparator.reverseOrder());

        for(char a : list)
            sb.append(a);
        System.out.print(sb);

    }
}