# Define a TreeNode class for a binary search tree (BST)
class TreeNode:
    def __init__(self, value):
        # Initialize a TreeNode with a given value
        self.right = None  # Right child node
        self.left = None   # Left child node
        self.value = value  # Node's value
        
    def insert(self, value):
        # Insert a new value into the BST
        if value < self.value:
            # If the new value is less than the current node's value, go to the left subtree
            if self.left is None:
                # If there's no left child, create a new node with the value
                self.left = TreeNode(value)
            else:
                # If there's a left child, recursively insert the value into the left subtree
                self.left.insert(value)
        else:
            # If the new value is greater than or equal to the current node's value, go to the right subtree
            if self.right is None:
                # If there's no right child, create a new node with the value
                self.right = TreeNode(value)
            else:
                # If there's a right child, recursively insert the value into the right subtree
                self.right.insert(value)
                
    def inorder_traversal(self):
        # Perform an inorder traversal of the BST (left-root-right)
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()
        
    def preorder_traversal(self):
        # Perform a preorder traversal of the BST (root-left-right)
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
        
    def postorder_traversal(self):
        # Perform a postorder traversal of the BST (left-right-root)
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)
        
    def find(self, value):
        # Search for a value in the BST and return True if found, False otherwise
        if value < self.value:
            if self.left is None:
                # Value not found in the left subtree
                return False
            else:
                # Recursively search in the left subtree
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                # Value not found in the right subtree
                return False
            else:
                # Recursively search in the right subtree
                return self.right.find(value)
        else:
            # Value found in the current node
            return True

# Create a sample BST and perform some operations
tree = TreeNode(6)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(19)
tree.insert(29)
tree.insert(11)
tree.insert(4)
tree.insert(2)

# Perform a postorder traversal and print the results
tree.postorder_traversal()

# Search for values in the BST
print(tree.find(7))  # Should print False
print(tree.find(11))  # Should print True
