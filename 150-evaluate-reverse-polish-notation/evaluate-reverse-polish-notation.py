class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        op = ['+','-','*','/']
        q= collections.deque()
        for i in tokens:
            if i not in op:
                q.append(int(i))
            else:
                a = q.pop()
                b=q.pop()
                if i == '+':
                    q.append(a+b)
                elif i == '-':
                    q.append(b-a)
                elif i == '*':
                    q.append(a*b)
                elif i == '/':
                    q.append(int(b/a))
            # print(q)
        # print(q)
        return q.pop()