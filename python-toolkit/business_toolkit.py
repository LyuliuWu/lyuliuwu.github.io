"""
Small Business Toolkit
A collection of Python functions for everyday business calculations:
pricing, payroll, inventory, customer rules, and simple sales analysis.
"""

import math


# ---------- Pricing & Payments ----------

def split_bill(subtotal, service_fee, people):
    """Split a bill plus a service fee equally among people."""
    return (subtotal + service_fee) / people


def order_total(unit_price, quantity, discount):
    """Calculate an order total after a fixed-dollar discount."""
    return unit_price * quantity - discount


def add_sales_tax(prices, tax_rate):
    """Return a new list of prices with sales tax added."""
    return [round(price * (1 + tax_rate), 2) for price in prices]


def shipping_fee(subtotal, is_member):
    """Members or orders of $50+ ship free; otherwise shipping is $6."""
    if subtotal >= 50 or is_member:
        return 0
    else:
        return 6


# ---------- Payroll & Finance ----------

def weekly_pay(hours, hourly_rate, bonus):
    """Calculate weekly pay: hours x rate, plus a fixed bonus."""
    return hours * hourly_rate + bonus


def investment_value(principal, annual_rate, years):
    """Calculate the future value of an investment with compound growth."""
    return round(principal * (1 + annual_rate) ** years, 2)


# ---------- Inventory ----------

def pack_boxes(items, box_size):
    """Return (full boxes, leftover items)."""
    return (items // box_size, items % box_size)


def low_stock(products, stock, minimum):
    """Return the products whose stock is below the minimum level."""
    result = []
    for i in range(len(products)):
        if stock[i] < minimum:
            result.append(products[i])
    return result


# ---------- Customer Rules ----------

def membership_price(age, is_member):
    """Seniors (65+) pay $8, other members pay $12, everyone else pays $20."""
    if age >= 65:
        return 8
    elif is_member:
        return 12
    else:
        return 20


def mask_card(card_number):
    """Hide all but the last four digits of a card number."""
    return f"****{card_number[-4:]}"


def order_label(first, last, order_id):
    """Create a pickup label like 'Maya C. #42'."""
    return f"{first} {last[0]}. #{order_id}"


def strong_password(password):
    """A password is valid if it has 10+ characters and no spaces."""
    return len(password) >= 10 and " " not in password


# ---------- Sales Analysis ----------

def total_sales(sales):
    """Add up daily sales with a loop."""
    total = 0
    for amount in sales:
        total = total + amount
    return total


def best_day(sales):
    """Return the highest daily sales amount."""
    best = sales[0]
    for amount in sales:
        if amount > best:
            best = amount
    return best


def average_sale(sales):
    """Average of days with sales above zero (closed days are ignored)."""
    total = 0
    count = 0
    for amount in sales:
        if amount > 0:
            total = total + amount
            count = count + 1
    if count == 0:
        return 0
    return round(total / count, 2)


def delivery_distance(east, north):
    """Straight-line distance between a store and a delivery address."""
    return math.sqrt(east ** 2 + north ** 2)


# ---------- Demo ----------

if __name__ == "__main__":
    print("Split a $90 bill + $10 fee among 4 people:", split_bill(90, 10, 4))
    print("Order total (3 x $15, $5 off):", order_total(15, 3, 5))
    print("Prices with 6.625% NJ tax:", add_sales_tax([10, 25, 40], 0.06625))
    print("Shipping fee ($35, non-member):", shipping_fee(35, False))
    print("Weekly pay (20 hrs at $17, $30 bonus):", weekly_pay(20, 17, 30))
    print("$1,000 at 5% for 3 years:", investment_value(1000, 0.05, 3))
    print("Pack 50 items in boxes of 12:", pack_boxes(50, 12))
    print("Low stock:", low_stock(["pens", "paper", "tape"], [3, 40, 8], 10))
    print("Membership price (age 30, member):", membership_price(30, True))
    print("Masked card:", mask_card("4111222233334444"))
    print("Pickup label:", order_label("Maya", "Chen", 42))
    print("Strong password?", strong_password("rutgers2028"))
    week = [320, 0, 450, 510, 0, 600, 380]
    print("Total weekly sales:", total_sales(week))
    print("Best day:", best_day(week))
    print("Average open-day sale:", average_sale(week))
    print("Delivery distance (3 east, 4 north):", delivery_distance(3, 4))
