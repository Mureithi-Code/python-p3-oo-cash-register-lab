#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize discount, total, and items
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = None 

    def add_item(self, title, price, quantity=1):
        """Add item to the register. If quantity > 1, add that many items."""
        self._update_total_and_items(title, price, quantity)
        self.last_transaction = (title, price, quantity)

    def apply_discount(self):
        """Apply discount if there is one."""
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Void the last transaction (remove last item(s) added)."""
        if self.last_transaction:
            last_item, price, quantity = self.last_transaction
            
            # Remove the correct number of items and subtract the correct amount
            self._remove_items_and_adjust_total(price, quantity)
            
            # Reset last transaction
            self.last_transaction = None 
            
            # If there are no items left, reset total to 0.0
            if not self.items:
                self.total = 0.0
        else:
            print("No items to void")

    def get_item_price(self, item):
        """Helper method to get the price of the item. Assumes items are unique."""
        item_prices = {
            "eggs": 0.98,
            "book": 5.00,
            "Lucky Charms": 4.50,
            "Ritz Crackers": 5.00,
            "Justin's Peanut Butter Cups": 2.50,
            "macbook air": 1000,
            "apple": 0.99,
            "tomato": 1.76
        }
        return item_prices.get(item, 0)  

    def _update_total_and_items(self, title, price, quantity):
        """Helper method to update total and items list."""
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def _remove_items_and_adjust_total(self, price, quantity):
        """Helper method to remove items and adjust total."""
        for _ in range(quantity):
            self.items.pop()  # Remove one item at a time
            self.total -= price  # Subtract the price of one item from total
