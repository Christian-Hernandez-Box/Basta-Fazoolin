import pytest
from main import Business, Franchise, Menu

@pytest.fixture
def brunch_menu():
    return Menu(
        name="Brunch",
        items={
            'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 
            'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 
            'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
        },
        start_time=1100,
        end_time=1400
    )

@pytest.fixture
def dinner_menu():
    return Menu(
        name="Dinner",
        items={
            'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 
            'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 
            'mushroom ravioli (vegan)': 13
        },
        start_time=1700,
        end_time=2300
    )

@pytest.fixture
def franchise(brunch_menu, dinner_menu):
    return Franchise(
        address="123 Main St",
        menus=[brunch_menu, dinner_menu]
    )

@pytest.fixture
def business(franchise):
    franchise2 = Franchise(
        address="456 Elm St",
        menus=[]
    )
    return Business(
        name="Test Business",
        franchises=[franchise, franchise2]
    )

def test_calculate_bill(brunch_menu):
    purchased_items = ['pancakes', 'coffee', 'mimosa']
    expected_bill = 7.50 + 1.50 + 10.50
    assert brunch_menu.calculate_bill(purchased_items) == expected_bill

def test_available_menus(franchise, brunch_menu, dinner_menu):
    available_menus = franchise.available_menus(1200)
    assert brunch_menu in available_menus
    assert dinner_menu not in available_menus

def test_list_franchises(business):
    expected_addresses = ["123 Main St", "456 Elm St"]
    assert business.list_franchises() == expected_addresses