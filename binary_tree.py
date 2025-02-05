class Node:
    def __init__(node, key, value): # Using __init__ function for automatic invocation
        node.key = key
        node.value = value
        node.left = None
        node.right = None

class BinarySearchTree: # Using __init__ function for automatic invocation
    def __init__(tree):
        tree.root = None
    
    def insert(tree, key, value):
        tree.root = tree._insert_recursive(tree.root, key, value)
    
    def _insert_recursive(tree, node, key, value):
        if node is None:
            return Node(key, value)  # Create new node if empty spot found
        if key < node.key:
            node.left = tree._insert_recursive(node.left, key, value)
        elif key > node.key:
            node.right = tree._insert_recursive(node.right, key, value)
        else:
            node.value = value  # Update value if key already exists
        return node
    
    def search(tree, key):
        return tree._search_recursive(tree.root, key)
    
    def _search_recursive(tree, node, key):
        if node is None:
            return None  # Key not found
        if key == node.key:
            return node.value
        elif key < node.key:
            return tree._search_recursive(node.left, key)
        else:
            return tree._search_recursive(node.right, key)
    
    def delete(tree, key):
        tree.root = tree._delete_recursive(tree.root, key)
    
    def _delete_recursive(tree, node, key):
        """Helper method to recursively delete a node."""
        if node is None:
            return None
        
        if key < node.key:
            node.left = tree._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = tree._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right  # Return right child if left is None
            elif node.right is None:
                return node.left  # Return left child if right is None
            
            # Node with two children: Get the inorder successor (smallest in right subtree)
            temp = tree._find_min(node.right)
            node.key, node.value = temp.key, temp.value  # Copy successor data
            node.right = tree._delete_recursive(node.right, temp.key)  # Delete successor
        return node
    
    def _find_min(tree, node):
        while node.left is not None:
            node = node.left
        return node
    
    def inorder_traversal(tree):
        """Display all items in inventory in sorted order."""
        tree._inorder_recursive(tree.root)
    
    def _inorder_recursive(tree, node):
        if node:
            tree._inorder_recursive(node.left)
            print(f"{node.key}: {node.value}")
            tree._inorder_recursive(node.right)

# Example usage
inventory = BinarySearchTree()

# Adding items to inventory
inventory.insert("item_1", {"name": "Arcade Machine", "quantity": 5, "price": 1500})
inventory.insert("item_2", {"name": "Joystick", "quantity": 20, "price": 30})
inventory.insert("item_3", {"name": "Game Cartridge", "quantity": 10, "price": 40})

# Searching for an item
print("Item 1 Details:", inventory.search("item_1"))

# Deleting an item
inventory.delete("item_2")
print("Item 2 After Deletion:", inventory.search("item_2"))

# Display full inventory
inventory.inorder_traversal()
