class Solution(object):
   def is_valid_parentheses(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char) 
        elif char in bracket_map.keys():
            if not stack or stack[-1] != bracket_map[char]:
                return False  
            stack.pop() 
            
    return not stack  # If the stack is empty, all brackets are matched

# Get user input
user_input = input("Enter a string of parentheses: ")
if is_valid_parentheses(user_input):
    print("The string is valid.")
else:
    print("The string is invalid.")






    



  

