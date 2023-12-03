    # BDD
# feature: is_balanced

 # Scenario: Balanced expression
  #  Given an expression "([]{})"
 #   When the is_balanced function is called
  #  Then the result should be True

 # Scenario: Unbalanced expression
 #   Given an expression "([)]"
 #   When the is_balanced function is called
 #   Then the result should be False


    #  pseudocode 
# Function is_balanced(expression):
 #   Initialize an empty stack
 #   For each character in the expression:
 #       If the character is an opening bracket:
 #           Push it onto the stack
 #       Else if the character is a closing bracket:
 #           If the stack is empty:
 #               Return False  # Unmatched closing bracket
 #           Pop the top element from the stack
 #           If the popped element is not the corresponding opening bracket:
 #    If the stack is not empty:
 #       Return False  # Unmatched opening bracket
 #   Return True  # All brackets are balanced

def is_balanced(expression):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != bracket_pairs[char]:
                return False

    return not stack

# Test cases
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False


