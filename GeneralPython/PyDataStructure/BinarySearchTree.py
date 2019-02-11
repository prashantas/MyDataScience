# Node Class
# http://www.geekviewpoint.com/python/bst/add
# https://www.laurentluce.com/posts/binary-search-tree-library-in-python/

import queue
from collections import deque as dq


class Node:
    def __init__(self,data):
    
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return {"data:{}".format(self.data)}
    def __repr__(self):
        return {"data:{}".format(self.data)}

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    @staticmethod
    def inorder(root):
        if root:
            Node.inorder(root.left)
            print(root.data, end=" ")
            Node.inorder(root.right)

    @staticmethod
    def preorder(root):
        if root:
            print(root.data, end = " ")
            Node.preorder(root.left)
            Node.preorder(root.right)
    
    @staticmethod
    def preorderNonRecursive(root):
        stack = list()
        result = list()
        if root is None:
            return result
        stack.append(root)
        while len(stack) != 0:
            n1 = stack.pop()
            result.append(n1.data)
            if n1.right != None:
                stack.append(n1.right)
            if n1.left != None:
                stack.append(n1.left)
        return result

    @staticmethod
    def createTree(tlist):
        for n, item in enumerate(tlist):
            if n == 0:
                root = Node(item)
            else:
                root.insert(item)
        return root

    @staticmethod
    def inorderNonRecursive(root):
        result = list()
        if root is None:
            return result
        stack = list()

        p = root

        while len(stack)!=0 or p is not None:
            if p is not None:
                stack.append(p) # push operation
                p = p.left
            else:
                node = stack.pop()
                result.append(node.data)
                p = node.right

        return result

    @staticmethod
    def levelOrderTraversal(root):
        if root.data is None:
            return None
        #q = queue.Queue(maxsize=100)
        q = dq()
        q.appendleft(root)
        while len(q)>0:
            size = len(q)
            #print("size:{}".format(size), end="::")
            while size > 0:
                node = q.pop()
                size = size -1 
                print("{}".format(node.data), end=" ")
                if node.left is not None:
                    q.appendleft(node.left)
                if node.right is not None:
                    q.appendleft(node.right)
            print("\n")

    @staticmethod
    def depthOfBST(root):
        if root is None:
            return 0
        ldepth = Node.depthOfBST(root.left)
        rdepth = Node.depthOfBST(root.right)
        if ldepth > rdepth:
            return ldepth+1
        else:
            return rdepth+1

    @staticmethod
    def breadthFirstEachLevelNewLineSpiralView(root):
        if root is None:
            return
        s1 = list()  # stack 1
        s2 = list()  # stack 2

        s1.append(root)

        while(len(s1)>0 or len(s2)>0):
            print("\n")
            while(len(s1)>0):
                node1 = s1.pop()
                print(node1.data, end=" ")
                if node1.right is not None:
                    s2.append(node1.right)
                if node1.left is not None:
                    s2.append(node1.left)
            print("\n")
            while(len(s2)>0):
                node1 = s2.pop()
                print(node1.data, end=" ")
                if node1.left is not None:
                    s1.append(node1.left)
                if node1.right is not None:
                    s1.append(node1.right)
                
    @staticmethod
    def reflectionIterative(root):
        if root is None:
            return
        q = dq()
        q.appendleft(root)
        while len(q)>0:
            node = q.pop()
            if node.left is None and node.right is None:
                continue
            if node.left is not None and node.right is not None:
                tmp = node.left
                node.left = node.right
                node.right = tmp
                q.appendleft(node.left)
                q.appendleft(node.right)
            elif node.left is not None:
                node.right = node.left
                node.left = None
                q.appendleft(node.right)
            elif node.right is not None:
                node.left = node.right
                node.right = None
                q.appendleft(node.left)
    ######################################################################################
    @staticmethod
    def isBSTUtil(root, min__, max__):
        if root is None:
            return True
        if root.data <= min__ or root.data >= max__ :
            return False
        return Node.isBSTUtil(root.left,min__,root.data) and Node.isBSTUtil(root.right,root.data,max__)
    
    @staticmethod
    def isBST(root):
        import sys
        return Node.isBSTUtil(root, -sys.maxsize, sys.maxsize)
    ####################################################################################
    @staticmethod
    def mergeTrees(t1, t2):
        # https://www.cnblogs.com/jiagui/p/6994926.html
        # https://www.geeksforgeeks.org/merge-two-binary-trees-node-sum/
        pass

class BST: 
    def __init__(self):
        print("BST class initialized")  

    @staticmethod
    def levelOrderTraversal(root):
        if root.data is None:
            return None
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            print("size:{}".format(size), end="::")
            while size > 0:
                node = q.get()
                print("  {}".format(node.data), end=" ")
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
            print("here\n")


if __name__ == '__main__':
    ##bst = BST()
    root = Node.createTree([8,10,1,6,4,7,9,15])
    Node.inorder(root)
    print("\n#################################")
    print("inorder non recursixe")
    print(Node.inorderNonRecursive(root))
    print("\n##################################")
    ##print(root.data)
    Node.levelOrderTraversal(root)
    print("####################################")
    #Node.breadthFirstEachLevelNewLineSpiralView(root)
    ################################################
    #print("\ndepth of BST: {}".format(Node.depthOfBST(root)))
    #print("\n#########################################################")
    print("\nPreorder::")
    Node.preorder(root)
    print("\nPreorderNone resursice::")
    print(Node.preorderNonRecursive(root)) #working
    ##################################################
    '''
    print("mirror::")
    Node.reflectionIterative(root) # working
    Node.levelOrderTraversal(root) # working
    '''
    ###############################################
    print("ISBST::{}".format(Node.isBST(root)))
    



