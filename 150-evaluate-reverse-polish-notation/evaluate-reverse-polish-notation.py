class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        op = ['+','-','*','/']
        q= collections.deque()
        for i in tokens:
            # print(q)
            if i not in op:
                q.append(int(i))
            else:
                if i == '+':
                    a=q.pop()
                    b=q.pop()
                    q.append(a+b)
                elif i == '-':
                    a=q.pop()
                    b=q.pop()
                    q.append(b-a)
                elif i == '*':
                    a=q.pop()
                    b=q.pop()
                    q.append(a*b)
                elif i == '/':
                    a=q.pop()
                    b=q.pop()
                    # print(a,b)
                    q.append(int(b/a))
        print(q)
        return q[-1]
