def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        if not root:
            return []
        s=[]
        s.append(root)
        while(s!=[]):
            root=s[-1]
            s.pop()
            l.append(root.val)
            if(root.right!=None):
                s.append(root.right)
            if(root.left!=None):
                s.append(root.left)
        return l
