import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static Comparator<String> comp = new Comparator<String>() {
        @Override
        public int compare(String o1, String o2) {
            if (o1.length() != o2.length())
                return o1.length() - o2.length();
            int i = 0;
            while (i < o1.length() && o1.charAt(i) == o2.charAt(i)) {
                i++;
            }
            return i == o1.length() ? 0 : (int) (o1.charAt(i) - o2.charAt(i));
        }
    };
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> list = new ArrayList<>();
        List<String> newList = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        
        int n = Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++){
            list.add(br.readLine());
        }
        
        newList = list.stream()
                .sorted(comp)
                .distinct()
                .collect(Collectors.toList());

        for(String s : newList){
            sb.append(s).append("\n");
        }
        System.out.print(sb);
    }
}