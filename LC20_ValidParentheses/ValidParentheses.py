# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Input: s = "()[]{}"
# Output: true
# Input: s = "(]"
# Output: false
# Input: s = "([)]"
# Output: false
# Input: s = "{[]}"
# Output: true

def isValid(str: str) -> bool:
    if len(str) == 0: # return true if there is nothing
        return True
    stack = []
    for char in str:
        if char == '(' or char == '[' or char == "{":
            stack.append(char)  # put all left bracket in to stack
        else:
            if len(stack) == 0: # more right bracket than left
                return False
            temp = stack.pop()
            if temp == '(' and char != ')':
                return False
            elif temp == '[' and char != ']':
                return False
            elif temp == '{' and char != '}':
                return False
    return False if len(stack) != 0 else True # more left bracket than right

# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print(isValid(""))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))
print(isValid("()[]{}("))
print(isValid("()[]{})"))