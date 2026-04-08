import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class a6{
    public static void main(String[] args){

        List<Map<String,Object>> users = new ArrayList<>();

        Map<String,Object> user1 = new HashMap<>();
        user1.put("id",101);
        user1.put("name","Francis");
        user1.put("active",true);
        users.add(user1);


        Map<String,Object> user2 = new HashMap<>();
        user2.put("id",102);
        user2.put("name","Admin");
        user2.put("active",true);
        users.add(user2);

        System.out.println("n--- All Users ---");
        for( Map<String,Object> user:users){

            Boolean isActive = (Boolean) user.get("active");
            
            if(Boolean.TRUE.equals(isActive)){
                System.out.println(user.get("name") + " is active");
            }

        } 
    }
}