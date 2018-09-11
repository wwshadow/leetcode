class Solution:
    def reSmallAndMaxx(self,root,small,maxx):
        if root == None:
            return True
        if root.val >= maxx or root.val <= small:
            return False
        return self.reSmallAndMaxx(root.left,small,root.val) and self.reSmallAndMaxx(root.right,root.val,maxx)
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.reSmallAndMaxx(root,-2**32,2**32-1)
