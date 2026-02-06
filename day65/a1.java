import java.util.ArrayList;
import java.util.List;

public class a1{
    public static void main(String[] args){
        List<String> frameworks = new ArrayList<>();

        frameworks.add("Django");
        frameworks.add("Spring boots");
        frameworks.add("Laravel");


        System.out.println("First item: " + frameworks.get(0));
        frameworks.set(1,"Flask");


        System.out.println("n --- Framework List ---");
        for (String f : frameworks){
            System.out.println(f);
        }

        System.out.println("n--- Filtered List (starts with D)---");
        frameworks.stream()
        .filter(f -> f.startsWith("D"))
        .forEach(System.out::println);
        

    }
}