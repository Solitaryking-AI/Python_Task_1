


# Part A — Spot the Bug


def add_item(item, cart=[]):
    cart.append(item)
    return cart


print("Part A Output:")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

# Explanation:
# Default mutable arguments are created only ONCE when the function is defined.
# So the same list is reused across function calls where no cart is provided.
#
# Output:
# ['apple']
# ['apple', 'banana']
# ['bread', 'milk']
# ['apple', 'banana', 'eggs']



# Part B — Correct Fix


def add_item_fixed(item, cart=None):

    # Create a fresh list every time if cart is not provided
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\nPart B Output:")
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))
print(add_item_fixed("eggs"))



# Part C — Shopping Cart


# Create cart function
def create_cart(owner, discount=0):

    # discount is immutable (int) -> safe default
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


# Add item to cart
def add_to_cart(cart, name, price, qty=1):

    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


# Tuple modification demo
def update_price(price_tuple, new_price):

    try:
        # Tuples are immutable -> this will raise TypeError
        price_tuple[0] = new_price

    except TypeError as e:
        print("\nTuple Error:", e)

    # Tuples cannot be modified after creation.
    # Their elements are fixed and immutable.


# Calculate total bill
def calculate_total(cart):

    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    # Apply discount
    discount_amount = (cart["discount"] / 100) * total
    final_total = total - discount_amount

    return final_total



# Demonstration


# Create two separate carts
cart1 = create_cart("Aarav", 10)
cart2 = create_cart("Meera", 5)

# Add items to first cart
add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 800, 2)

# Add items to second cart
add_to_cart(cart2, "Phone", 25000, 1)
add_to_cart(cart2, "Charger", 1200, 1)

# Display carts
print("\nCart 1:")
print(cart1)

print("\nCart 2:")
print(cart2)

# Calculate totals
print("\nCart 1 Total:", calculate_total(cart1))
print("Cart 2 Total:", calculate_total(cart2))

# Tuple immutability test
price_data = (1000, "Keyboard")
update_price(price_data, 2000)



# Discussion Points


# 1. Why is discount=0 safe but cart=[] dangerous?
#
# discount=0 is safe because integers are immutable.
# cart=[] is dangerous because lists are mutable and shared
# across function calls.


# 2. What is the difference between rebinding and mutating?
#
# Rebinding means assigning a variable to a new object.
# Example:
# x = [1, 2]
# x = [5, 6]
#
# Mutating means changing the existing object itself.
# Example:
# x.append(3)


# 3. Which of these are mutable?
#
# list  -> Mutable
# tuple -> Immutable
# dict  -> Mutable
# set   -> Mutable
# str   -> Immutable
# int   -> Immutable


# 4. When you pass a list into a function and modify it,
#    do changes reflect outside? Why?
#
# Yes. Lists are mutable objects.
# The function receives a reference to the same list object,
# so modifications affect the original list outside the function.