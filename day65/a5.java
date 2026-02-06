import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class a5{
    public static void main(String[] args){

        List<Integer> price = new ArrayList<>();
        price.add(500);
        price.add(100);
        price.add(200);


        System.out.println("Before" + price);
        Collections.sort(price);
        System.out.println("Sorted" + price);

        Collections.sort(price,Collections.reverseOrder());
        System.out.println("Reverse" + price);
    }
}