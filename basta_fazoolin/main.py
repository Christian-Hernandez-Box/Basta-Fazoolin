class Business:
    def __init__(self, name: str, franchises: list):
        """
        Initialize a Business with a name and a list of franchises.
        """
        self.name = name
        self.franchises = franchises

    def list_franchises(self) -> list:
        """
        Return a list of all franchise addresses.
        """
        return [franchise.address for franchise in self.franchises]

    def __repr__(self) -> str:
        return f"Business(name={self.name}, franchises={self.franchises})"


class Franchise:
    def __init__(self, address: str, menus: list):
        """
        Initialize a Franchise with an address and a list of menus.
        """
        self.address = address
        self.menus = menus

    def __repr__(self) -> str:
        return f"Franchise(address={self.address})"

    def available_menus(self, time: int) -> list:
        """
        Return a list of menus available at a given time.
        """
        available_menus = [menu for menu in self.menus if menu.start_time <= time <= menu.end_time]
        return available_menus


class Menu:
    def __init__(self, name: str, items: dict, start_time: int, end_time: int):
        """
        Initialize a Menu with a name, items, start time, and end time.
        """
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self) -> str:
        return f"{self.name} menu is available from: {self.start_time} - {self.end_time}"

    def calculate_bill(self, purchased_items: list) -> float:
        """
        Calculate the total bill for a list of purchased items.
        """
        total = sum(self.items[item] for item in purchased_items if item in self.items)
        return total


# Define menu items outside the class
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13
}

kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

arepas_items = {
    'arepa pabellon': 7.00, 
    'pernil arepa': 8.50, 
    'guayanes arepa': 8.00, 
    'jamon arepa': 7.50
}