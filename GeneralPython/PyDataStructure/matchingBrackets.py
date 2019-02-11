# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/

def areParanthesisBalanced(expr):
    stack = list()

    for i,chr in enumerate(expr):
        #print(i, chr)
        if chr in ['(','{','[']:
            stack.append(chr)
            continue 
        
        # IF current current character is not opening 
        # bracket, then it must be closing. So stack 
        # cannot be empty at this point. 
        if len(stack) == 0 :
            return False

        if chr == ')':
            x = stack.pop()
            if x != '(':
                return False
        elif chr == '}':
            x = stack.pop()
            if x != '{':
                return False
        elif chr == ']':
            x = stack.pop()
            if x != '[':
                return False
    
    return len(stack) == 0


if __name__ == '__main__':
    print("#########")
    str__ = "{()}[]"
    print(areParanthesisBalanced(str__))
