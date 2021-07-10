import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Hash{
    public List<List<String>> groupAnagrams(String[] strs){
        HashMap<String,ArrayList<String>> result = new HashMap<>();
        for(String str : strs){
            char[] char_array = str.toCharArray();
            int[] count_table = new int[26];
            for(char c : char_array){
                count_table[c-'a']++;
            }
            // make array as string in order to be hashable
            // [1,12,3] -> "#1#12#3"
            StringBuilder sb = new StringBuilder();
            for(int block : count_table){
                sb.append("#");
                sb.append(block);
            }
            String key = sb.toString();
            if(!result.containsKey(key)) result.put(key, new ArrayList<>());
            result.get(key).add(str);
        }
        return new ArrayList(result.values());
    }
}