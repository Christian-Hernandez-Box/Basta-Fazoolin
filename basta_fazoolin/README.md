# Basta Fazoolin' with My Heart

## Project Overview

This project simulates a restaurant business with multiple franchises and menus. It includes classes to represent a `Business`, `Franchise`, and `Menu`, and provides functionality to calculate bills, list available menus, and more.

## Classes

### Business
Represents a business with multiple franchises.

- **Attributes:**
  - `name` (str): The name of the business.
  - `franchises` (list): A list of `Franchise` objects.

- **Methods:**
  - `list_franchises() -> list`: Returns a list of all franchise addresses.
  - `__repr__() -> str`: Returns a string representation of the business.

### Franchise
Represents a franchise with an address and multiple menus.

- **Attributes:**
  - `address` (str): The address of the franchise.
  - `menus` (list): A list of `Menu` objects.

- **Methods:**
  - `available_menus(time: int) -> list`: Returns a list of menus available at a given time.
  - `__repr__() -> str`: Returns a string representation of the franchise.

### Menu
Represents a menu with a name, items, start time, and end time.

- **Attributes:**
  - `name` (str): The name of the menu.
  - `items` (dict): A dictionary of items and their prices.
  - `start_time` (int): The start time of the menu.
  - `end_time` (int): The end time of the menu.

- **Methods:**
  - `calculate_bill(purchased_items: list) -> float`: Calculates the total bill for a list of purchased items.
  - `__repr__() -> str`: Returns a string representation of the menu.

## Menu Items

The project includes predefined menu items for different types of menus:

- **Brunch Items:**
  - Pancakes: $7.50
  - Waffles: $9.00
  - Burger: $11.00
  - Home Fries: $4.50
  - Coffee: $1.50
  - Espresso: $3.00
  - Tea: $1.00
  - Mimosa: $10.50
  - Orange Juice: $3.50

- **Early Bird Items:**
  - Salumeria Plate: $8.00
  - Salad and Breadsticks (serves 2, no refills): $14.00
  - Pizza with Quattro Formaggi: $9.00
  - Duck Ragu: $17.50
  - Mushroom Ravioli (vegan): $13.50
  - Coffee: $1.50
  - Espresso: $3.00

- **Dinner Items:**
  - Crostini with Eggplant Caponata: $13.00
  - Caesar Salad: $16.00
  - Pizza with Quattro Formaggi: $11.00
  - Duck Ragu: $19.50
  - Mushroom Ravioli (vegan): $13.00

- **Kids Items:**
  - Chicken Nuggets: $6.50
  - Fusilli with Wild Mushrooms: $12.00
  - Apple Juice: $3.00

- **Arepas Items:**
  - Arepa Pabellon: $7.00
  - Pernil Arepa: $8.50
  - Guayanes Arepa: $8.00
  - Jamon Arepa: $7.50

## Running Tests

This project uses `pytest` for unit testing. To run the tests, use the following command:

```sh
pytest test_main.py
