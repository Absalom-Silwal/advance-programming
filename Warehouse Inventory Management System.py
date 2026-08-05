"""
Task 2 : Comparing Complex Data types

"""
from typing import Dict

def create_inventory():
    inventories = {
        "P101": {
            "name": "Laptop",
            "category": "Electronics",
            "price": 1200,
            "quantity": 15
        },
        "P102": {
            "name": "Office Chair",
            "category": "Furniture",
            "price": 250,
            "quantity": 30
        },
        "P103": {
            "name": "Keyboard",
            "category": "Electronics",
            "price": 80,
            "quantity": 45
        },
        "P104": {
            "name": "Coffee Mug",
            "category": "Kitchen",
            "price": 15,
            "quantity": 80
        }
    }
    return inventories


def display_inventory(inventory):
    print("\nInventory Report")
    print("-" * 60)
    for product_id, product in inventory.items():
        print(
            f"{product_id:<6}"
            f"{product['name']:<20}"
            f"{product['category']:<15}"
            f"Qty:{product['quantity']}"
        )


def get_unique_categories(inventory):
    unique_categories= set(product["category"] for product in inventory.values())
    return unique_categories


def calculate_total_stock(inventory):
    return sum(
        product["quantity"]
        for product in inventory.values()
    )


def search_product(inventory, product_id):
    find_by_id = inventory.get(product_id)
    if find_by_id:
        print("\nInventory Found")
        print(find_by_id)
    else:
        print("\nProduct Not Found")


def main():
    try:
        inventory = create_inventory()
        display_inventory(inventory)
        categories = get_unique_categories(inventory)
        print("\nUnique Categories")
        print(categories)
        total_stock = calculate_total_stock(inventory)
        print(f"\nTotal Stock: {total_stock}")
        search_product(inventory, "P103")

        """ for Test Cases """
        inventory["P105"] = {
            "name": "Monitor",
            "category": "Electronics",
            "price": 350,
            "quantity": 20
        }
        print('\nResults for Update')
        print("-"*100)
        display_inventory(inventory)
        search_product(inventory,"P105")
        categories_after_insertion = get_unique_categories(inventory)
        print(f"\nCategories after Insertion:{categories_after_insertion}")
    except Exception as e:
        print(f"An error has occured:{e}")


if __name__ == "__main__":

    main()