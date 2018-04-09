class Node:
 
  
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 

def maxDep(node):
    if node is None:
        return 0 ; 
 
    else :
 
     
        lDep = maxDep(node.left)
        rDep = maxDep(node.right)
 
      
        if (lDep > rDep):
            return lDep+1
        else:
            return rDep+1
 
 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
 
 
print "Height of tree is %d" %(maxDep(root))
