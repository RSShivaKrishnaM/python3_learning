class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        stack1.append(s[0])
        i = 0
        print(len(s))
        while len(stack1)>0 & i < len(s)-2:
            print("stack ele:",stack1,"and len of stack:",len(stack1))
            print("value of i:", i,"and len of s:", len(s))
            chara = s[i]
            if chara == '(':
                stack1.append(chara)
            elif chara == ')':
                if stack1[len(stack1)-1] == '(': 
                    stack1.pop()
                else:
                    return False
                    break
            elif chara == '{':
                stack1.append(chara)
            elif chara == '}':
                if stack1[len(stack1)-1] == '{':
                    stack1.pop()
                else:
                    return False
                    break
            elif chara == '[':
                stack1.append(chara)
            elif chara == ']':
                if stack1[len(stack1)-1] == ']':
                    stack1.pop()
                else:
                    return False
                    break
            i += 1
        
        return True
    
def main():
    sol =  Solution()   
    print(sol.isValid("{}()"))                              

if __name__ == "__main__":
    main()