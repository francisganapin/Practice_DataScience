import java.util.HashMap;
import java.util.Map;

public class a3{
    public static void main(String[] args){


        Map<String,Integer> aScores = new HashMap<>();

        aScores.put("panget",100);
        aScores.put("Lord",91);
        aScores.put("Martin",85);
        aScores.put("Francis",78);

        Integer score = aScores.get("panget");
        System.out.println("Panget's score: " + score);

        if(aScores.containsKey("Francis")){
            System.out.println("Francis is present");
        }

        System.out.println("n--- All Scores ---");
        for(Map.Entry<String,Integer> entry : aScores.entrySet()){
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }

    }
}