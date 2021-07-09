import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class Main{
    public static main(String[] args){
        // TODO
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList> result = new HashMap<>();

        for(String str: strs){
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String sortedString = new String(charArray);
            
            if(!result.containsKey(sortedString)) result.put(sortedString, new ArrayList<>());
            result.get(sortedString).add(str);
        }
        return new ArrayList(result.values());
    }
}