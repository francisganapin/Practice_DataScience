import java.util.HashMap;
import java.util.Map;


public class a2{
    public static void main(String[] args){

        Map<String,Integer> userScores = new HashMap<>();

        userScores.put("John",95);
        userScores.put("Jane",100);
        userScores.put("Bob",85);

        Integer score = userScores.get("Francis");

        System.out.println("Francis's score: " + score);

        if(userScores.containsKey("Admin")){
            System.out.println("Admin is present");
        }

        System.out.println("n--- All Scores ---");
        for(Map.Entry<String,Integer> entry : userScores.entrySet()){
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }

    }
}