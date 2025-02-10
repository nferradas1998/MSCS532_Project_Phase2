class ProductNode:
    def __init__(node, product_id, name, quantity, price): # using __init__ function for automatic invocation
        node.id = product_id
        node.name = name
        node.quantity = quantity
        node.price = price
        node.left = None
        node.right = None

class InventoryBST:
    def __init__(inv): # using __init__ function for automatic invocation
        inv.root = None

    def upsert(inv, product_id, name, quantity, price):
        new_node = ProductNode(product_id, name, quantity, price)
        
        if not inv.root:
            inv.root = new_node
            return

        current = inv.root
        parent = None

        while current:
            parent = current
            if product_id == current.id: # check if product already exists
                # Update existing product
                current.name = name
                current.quantity = quantity
                current.price = price
                return
            elif product_id < current.id:
                current = current.left
            else:
                current = current.right

        # Insert new product
        if product_id < parent.id:
            parent.left = new_node
        else:
            parent.right = new_node

    def search(inv, product_id):
        current = inv.root
        while current:
            if product_id == current.id:
                return {
                    "ID": current.id,
                    "Name": current.name,
                    "Quantity": current.quantity,
                    "Price": current.price
                }
            elif product_id < current.id:
                current = current.left
            else:
                current = current.right
        return None

    def delete(inv, product_id):
        current = inv.root
        parent = None

        # find the product node
        while current and current.id != product_id:
            parent = current
            if product_id < current.id:
                current = current.left
            else:
                current = current.right

        if not current:  # Product not found
            return False

        ## We need to check the use case to know how to delete the product
        # Case 1: Node with only one child or no child
        if not current.left or not current.right:
            new_child = current.left if current.left else current.right

            if not parent:  # Deleting root node
                inv.root = new_child
            elif parent.left == current:
                parent.left = new_child
            else:
                parent.right = new_child

        # Case 2: Node with two children
        else:
            successor_parent = current
            successor = current.right

            while successor.left:
                successor_parent = successor
                successor = successor.left

            # Copy successor's values to current node
            current.id, current.name, current.quantity, current.price = successor.id, successor.name, successor.quantity, successor.price

            # Remove the successor node
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        return True

    def inorder_traversal(inv):
        stack = []
        current = inv.root
        result = []

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append({
                "ID": current.id,
                "Name": current.name,
                "Quantity": current.quantity,
                "Price": current.price
            })
            current = current.right

        return result

# As an example I'm creating an inventory with 4 products
inventory = InventoryBST()
inventory.upsert(10, "Laptop", 5, 1200.00)
inventory.upsert(20, "Monitor", 10, 300.00)
inventory.upsert(5, "Mouse", 50, 25.00)
inventory.upsert(15, "Keyboard", 20, 45.00)

print("=========================initial inventory=========================\n")
for product in inventory.inorder_traversal():
    print(product)

print("\n====================Search functionality=========================\n")
print("Search Product ID 10:", inventory.search(10)) ## search for product with ID 10 (should print laptop)
print("Search Product ID 100:", inventory.search(100)) ## search for product with ID 100 (should not get anything)

print("\n=====================Delete Functionality=======================")
print("\nDeleting Product ID 5") ## Deletes product with ID 5
inventory.delete(5)
print("\nInventory After Deletion (Sorted by ID):")
for product in inventory.inorder_traversal():
    print(product)


print("\n===================Update Product========================\n")
inventory.upsert(10, "Laptop", 9, 1200.00) ## Update the stock from 5 to 9
print("\nInventory After Update (Sorted by ID):")
for product in inventory.inorder_traversal():
    print(product)

