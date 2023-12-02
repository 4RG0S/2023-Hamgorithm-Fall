import java.io.*;
import java.util.*;

class Person implements Comparable<Person>{
    int age;
    String name;

    public Person(int age, String name){
        this.age = age;
        this.name = name;
    }
    
    @Override
    public int compareTo(Person o) {
        return this.age - o.age;
    }
    
    public String toString(){
        return age + " " + name;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        List<Person> list = new ArrayList<>();
        String[] info;

        for(int i=0; i<n; i++){
            info = br.readLine().split(" ");
            list.add(new Person(Integer.parseInt(info[0]), info[1]));
        }
        Collections.sort(list);

        StringBuilder sb = new StringBuilder();
        for(Person p : list)
            sb.append(p).append("\n");

        System.out.print(sb);
    }
}