class HashTable:
    def __init__(table, size=100): # Using __init__ methos for automatic invocation
        table.size = size
        table.table = [[] for _ in range(size)]  # Create a list of empty lists for chaining

    def hash(table, key):
        return hash(key) % table.size # Going to use this simple hash function for now, this cannot be used for the final implementation since it would create too many collisions

    def upsert(table, key, value):
        index = table.hash(key)
        for pair in table.table[index]:
            if pair[0] == key: # check if item exists
                pair[1] = value  # update existing item
                return
        table.table[index].append([key, value])  # insert new item

    def search(table, key):
        index = table.hash(key)
        for pair in table.table[index]:
            if pair[0] == key:
                return pair[1]  # Return the value
        return None  # return none when nothing is found

    def delete(table, key):
        index = table.hash(key)
        for i, pair in enumerate(table.table[index]):
            if pair[0] == key:
                del table.table[index][i]  # Remove the item
                return True # return true when item was deleted
        return False  # return false when nothing was found and hence nothing was deleted

    def print_table(table): # Function to show the effect of operatons
        for i, bucket in enumerate(table.table):
            if bucket:
                print(f"Index {i}: {bucket}")

inventory = HashTable(size=50)

# Adding items to the inventory
inventory.upsert("item_1", {"name": "Arcade Machine", "quantity": 5, "price": 1500})
inventory.upsert("item_2", {"name": "Joystick", "quantity": 20, "price": 30})

inventory.print_table()

# Searching for an item
print("Item 1 Details:", inventory.search("item_1"))

# Updating an existing item
inventory.upsert("item_1", {"name": "Arcade Machine", "quantity": 4, "price": 1500})
print("Updated Item 1 Details:", inventory.search("item_1"))

# Deleting an item
inventory.delete("item_2")
print("Item 2 After Deletion:", inventory.search("item_2"))

# Display full inventory
inventory.print_table()
