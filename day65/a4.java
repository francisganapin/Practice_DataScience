import java.util.List;
import java.util.Map;

public class ModernCollection{
    public static void main(String[] args){

        List<String> frameworks = List.of("Django","Spring","Laravel");
        System.out.println(frameworks);

        Map<String,Integer> scores = Map.of({
            "Francis",78,
            "Admin",99,
        });
        System.out.println(scores.get("Francis"));
    }
    
}