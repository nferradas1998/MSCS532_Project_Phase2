class Node:
    def __init__(node, key, value): # using __init__ function for automatic invocation
        node.key = key
        node.value = value
        node.prev = None
        node.next = None

class DoublyLinkedList:
    def __init__(list): # using __init__ function for automatic invocation
        list.head = None
        list.tail = None
    
    def add_item(list, key, value):
        new_node = Node(key, value)
        if not list.head:  # If the list is empty, set head and tail to new node
            list.head = list.tail = new_node
        else:
            list.tail.next = new_node  # Link the last node to the new node
            new_node.prev = list.tail  # Set new node's previous pointer
            list.tail = new_node  # Update tail pointer
    
    def find_item(list, key):
        current = list.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None  # Key not found
    
    def delete(list, key):
        current = list.head
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next  # Link previous node to next node
                else:
                    list.head = current.next  # If deleting head, move head pointer
                if current.next:
                    current.next.prev = current.prev  # Link next node to previous node
                else:
                    list.tail = current.prev  # If deleting tail, move tail pointer
                return True
            current = current.next
        return False  # Key not found
    
    def print_list(list):
        current = list.head
        while current:
            print(f"{current.key}: {current.value}")
            current = current.next

inventory = DoublyLinkedList()

# Adding items to inventory
inventory.add_item("item_1", {"name": "Arcade Machine", "quantity": 5, "price": 1500})
inventory.add_item("item_2", {"name": "Joystick", "quantity": 20, "price": 30})

# find an item
print("Item 1 Details:", inventory.find_item("item_1"))

# delete an item
inventory.delete("item_2")
print("Item 2 After Deletion:", inventory.find_item("item_2"))

# Print inventory
inventory.print_list()
