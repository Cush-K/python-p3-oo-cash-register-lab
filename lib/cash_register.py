#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0, total = 0, items = None):
      self.discount = discount
      self.total = total
      self.items = items if items is not None else []
      self.items_prices = []

    def add_item(self, title, price, quantity=1):
      self.total += price * quantity
      self.items.extend([title]*quantity)
      self.items_prices.extend([price]*quantity)
    
    def apply_discount(self):
      if self.discount > 0:
        self.total -= self.total * self.discount / 100
        print(f"After the discount, the total comes to ${self.total:.0f}.")
      else:
        print("There is no discount to apply.")

    def items_list(self):
      return self.items
    
    def void_last_transaction(self):
      if self.items:
        
        last_item = self.items[-1]
        last_item_price = None
        count=0
        
        for item in range(len(self.items)-1, -1, -1):
          if self.items[item] == last_item:
            last_item_price = self.items_prices[item]
            self.total -= last_item_price
            self.items.pop(item)
            self.items_prices.pop(item)
            count += 1
        
        if count == 0:
          print("No items to void.")
      else:
        print("No items to void.")
    
    
# purchase = CashRegister("mangoes")
# purchase.add_item("eggs", 10, 12)
# purchase.apply_discount
# print(purchase.items_list)