class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])
                
            elif s[i] in ')}]':
                if not stack:
                    return False
                last_open = stack.pop()
                if s[i] == ')' and last_open != '(' or \
                   s[i] == '}' and last_open != '{' or \
                   s[i] == ']' and last_open != '[':
                    return False
            else:
                # Ignore characters other than parentheses, square brackets, and curly braces
                pass

        return not stack 