class ProductNode:
    def __init__(node, product_id, name, quantity, price): # Using __init__ method for automatic invocation
        node.id = product_id
        node.name = name
        node.quantity = quantity
        node.price = price
        node.next = None
        node.prev = None

class InventoryDLL:
    def __init__(list): # using __init__ method for automatic invocation
        list.head = None
        list.tail = None

    def upsert(list, product_id, name, quantity, price):
        current = list.head

        # Check if the product exists and update it
        while current:
            if current.id == product_id:
                current.name = name
                current.quantity = quantity
                current.price = price
                return
            current = current.next

        # If product does not exist, create and insert at the end
        new_node = ProductNode(product_id, name, quantity, price)

        if not list.head:  # List is empty
            list.head = new_node
            list.tail = new_node
        else:
            list.tail.next = new_node
            new_node.prev = list.tail
            list.tail = new_node

    def search(list, product_id):
        current = list.head
        while current:
            if current.id == product_id:
                return {
                    "ID": current.id,
                    "Name": current.name,
                    "Quantity": current.quantity,
                    "Price": current.price
                }
            current = current.next
        return None

    def delete(self, product_id):
        current = self.head

        while current:
            if current.id == product_id:
                ## We need to check the position of the node to know how to delete it from the list.
                # Case 1: only node in the list
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None

                # Case 2: node is the head node
                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None

                # Case 3: node is the last node (tail)
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None

                # Case 4: node is somewhere in the middle
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return True  # return true if node was deleted successfully
            current = current.next

        return False  # not found, retrun false

    def get_inventory(list):
        # Iterate through the linked list and print the product details
        current = list.head
        inventory_list = []
        while current:
            inventory_list.append({
                "ID": current.id,
                "Name": current.name,
                "Quantity": current.quantity,
                "Price": current.price
            })
            current = current.next
        return inventory_list

# As an example I'm creating an inventory with 4 products
inventory = InventoryDLL()
inventory.upsert(10, "Laptop", 5, 1200.00)
inventory.upsert(20, "Monitor", 10, 300.00)
inventory.upsert(5, "Mouse", 50, 25.00)
inventory.upsert(15, "Keyboard", 20, 45.00)

print("=========================initial inventory=========================\n")
for product in inventory.get_inventory():
    print(product)

print("\n====================Search functionality=========================\n")
print("Search Product ID 10:", inventory.search(10)) ## search for product with ID 10 (should print laptop)
print("Search Product ID 100:", inventory.search(100)) ## search for product with ID 100 (should not get anything)

print("\n=====================Delete Functionality=======================")
print("\nDeleting Product ID 5") ## Deletes product with ID 5
inventory.delete(5)
print("\nInventory After Deletion (Sorted by ID):")
for product in inventory.get_inventory():
    print(product)


print("\n===================Update Product========================\n")
inventory.upsert(10, "Laptop", 9, 1200.00) ## Update the stock from 5 to 9
print("\nInventory After Update (Sorted by ID):")
for product in inventory.get_inventory():
    print(product)
