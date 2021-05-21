import java.util.Stack;

/* Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
* An input string is valid if:
* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.

* Input: s = "()[]{}"
* Output: true
* Input: s = "(]"
* Output: false
* Input: s = "([)]"
* Output: false
* Input: s = "{[]}"
* Output: true
*/

public class Main{
    public static void main(String[] args){
        System.out.println(isValid(""));
        System.out.println(isValid("()[]{}"));
        System.out.println(isValid("(]"));
        System.out.println(isValid("([)]"));
        System.out.println(isValid("{[]}"));
        System.out.println(isValid("()[]{}("));
        System.out.println(isValid("()[]{})"));
    }

    private static boolean isValid(String str){
        Stack<Character> stack = new Stack<>();
        for(char ch: str.toCharArray()){
            if(ch == '(' || ch == '[' || ch == '{'){
                stack.push(ch);
            }else{
                if(stack.isEmpty()) return false;
                char temp = stack.pop();
                if(temp == '(' && ch != ')') return false;
                if(temp == '[' && ch != ']') return false;
                if(temp == '{' && ch != '}') return false;
            }
        }
        return stack.isEmpty()? true : false;
    }
}