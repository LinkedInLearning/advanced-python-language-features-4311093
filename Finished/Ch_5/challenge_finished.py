# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Structural Pattern Matching

# The Challenge:
# Our program will process the content of a restaurant to-go order.
# 1. Each order contains a list of items with type, name, quantity, and price
#       Type will either be "main", "side", or "drink"
# 2. Each item has a weight, so we know what size delivery bag to use.
#       Order weight < 1250g, small bag, otherwise large bag.
# 3. If an order contains 3 or more of a "side" item, that item total is discounted 10%
#       Example: 4 "side" items at 1.00 would be 4.00, minus 10% is 3.60
# 4. Orders with more than 10 total items get additional 15% off the total.
# 5. Output should be:
#       Order Total Price
#       Order item count
#       Order Total Weight
#       Size of bag to use (S or L)

# Weight in grams of each item
ITEM_WEIGHTS = {
    "Burger": 125,
    "Chicken Wings": 275,
    "Pizza Slice": 170,
    "Burrito": 150,
    "Fries": 140,
    "Onion Rings": 150,
    "Churros": 75,
    "Milkshake": 225,
    "Soda": 130
}

test_orders = [
    [
        ["main", "Burger", 1, 6.99],
        ["side", "Fries", 1, 2.99],
        ["main", "Pizza Slice", 1, 5.79],
        ["side", "Onion Rings", 3, 2.49],
        ["drink", "Milkshake", 1, 4.69]
    ],
    [
        ["main", "Pizza Slice", 2, 5.79],
        ["main", "Burrito", 4, 4.99],
        ["side", "Churros", 4, 2.99],
        ["side", "Fries", 2, 2.99],
        ["drink", "Soda", 4, 0.99]
    ]
]


# process each order
for order in test_orders:
    # set the initial variables for the totals
    total_price = 0.0
    total_weight = 0
    item_count = 0
    bag_size = None

    for item in order:
        match item:
            # if this order has an item with quantity >= 3 apply the discount
            case "side", name, quantity, price if quantity >= 3:
                total_price += (quantity * price) * 0.9
                total_weight += (ITEM_WEIGHTS[name] * quantity)
                item_count += quantity
            case _, name, quantity, price:
                total_price += (quantity * price)
                total_weight += (ITEM_WEIGHTS[name] * quantity)
                item_count += quantity
            case _:
                print(f"Error: Badly formed order item: {item}")

    if (item_count >= 10):
        total_price = total_price * .85

    print(f"Order total: {total_price:.2f}")
    print(f"Item count: {item_count}")
    print(f"Order weight: {total_weight} grams")
    print(f"Bag size: {'S' if total_weight < 1250 else 'L'}")
    print("-------------------")
