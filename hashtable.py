class InventoryHashTable:

    def __init__(table):
        # Initializing the table as a dictionary 
        table.inventory = {}

    def upsert(table, product_id, name, quantity, price): ## Use the id as the index for a simple first implementation
        table.inventory[product_id] = {
            "Name": name,
            "Quantity": quantity,
            "Price": price
        }

    def search(table, product_id):
        return table.inventory.get(product_id, None)

    def delete(table, product_id):
        return table.inventory.pop(product_id, None) is not None

    def get_inventory(table):
        return [{**{"ID": pid}, **details} for pid, details in table.inventory.items()]

# As an example I'm creating an inventory with 4 products
inventory = InventoryHashTable()
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
print("\nInventory After Deletion:")
for product in inventory.get_inventory():
    print(product)


print("\n===================Update Product========================\n")
inventory.upsert(10, "Laptop", 9, 1200.00) ## Update the stock from 5 to 9
print("\nInventory After Update:")
for product in inventory.get_inventory():
    print(product)
