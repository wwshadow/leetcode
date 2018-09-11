class Solution:
    def isSametree(self,p,q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            left = self.isSametree(p.left,q.right)
            right = self.isSametree(q.right,p.left)
            return left and right
        else:
            return False
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.isSametree(root.left,root.right)


#查看如下 https://blog.csdn.net/IT_job/article/details/80216423
# Definition for a binary tree node.

# class TreeNode:

#     def __init__(self, x):

#         self.val = x

#         self.left = None

#         self.right = None



# class Solution:
#
#     def isSymmetric(self, root):
#
#         """
#
#         :type root: TreeNode
#
#         :rtype: bool
#
#         """
#
#         #思路主要参考leetcode100题，这里将根节点的左右节点假设成两颗独立的树，这样解题跟100就是类似的了,区别：递归调用时，因是对称，所以是左树左节点与右树右节点，左树右节点与右树左节点
#
#         #先定义，后调用
#
#         def isSameTree(p,q):
#
#             if not p and not q:#两二叉树皆为空，递归边界，两者皆为空返回真
#
#                 return True
#
#             if p and q and p.val==q.val:
#
#                 l=isSameTree(p.left,q.right)#，与leetcode100有区别。递归，每次重新从函数入口处进行，每次进行递归边界判断
#
#                 r=isSameTree(p.right,q.left)
#
#                 return l and r#and操作，需要l与r皆为true时，才返回真。只用最后一次递归边界return值
#
#             else:
#
#                 return False
#
#         if not root:
#
#             return True
#
#         else:
#
#             #p=root.left;q=root.right
#
#             return isSameTree(root.left,root.right)