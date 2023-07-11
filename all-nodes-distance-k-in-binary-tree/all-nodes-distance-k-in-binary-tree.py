# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        q=collections.deque()
        hashmap={}

        q.append(root)

        while q:

            for _ in range(len(q)):
                pop=q.popleft()

                if pop.left:
                    hashmap[pop.left]=pop
                    q.append(pop.left)

                if pop.right:
                    hashmap[pop.right]=pop
                    q.append(pop.right)



        q=collections.deque()
                
        q.append(target)
        visited=set([target])
        
        while q and k:
            for _ in range(len(q)):
                pop = q.popleft()
                print(pop.val)
                # print(hashmap[pop])
                if pop.left and pop.left not in visited :
                    q.append(pop.left)
                    visited.add(pop.left)
                    print(pop.left.val)
                if pop.right and pop.right not in visited :
                    q.append(pop.right)
                    visited.add(pop.right)
                    print(pop.right.val)

                if pop in hashmap and hashmap[pop] and hashmap[pop] not in visited:
                    q.append(hashmap[pop])
                    visited.add(hashmap[pop])
                    print(hashmap[pop].val)

            k=k-1
        res=[]

        for i in q:
            res.append(i.val)
        return res


