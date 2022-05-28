"""
List Methods
As we start exploring lists further in the next exercises, we will encounter the concept of a method.

In Python, for any specific data-type ( strings, booleans, lists, etc. ) there is built-in functionality that we can use to create, manipulate, and even delete our data. We call this built-in functionality a method.

For lists, methods will follow the form of list_name.method(). Some methods will require an input value that will go between the parenthesis of the method ( ).

An example of a popular list method is .append(), which allows us to add an element to the end of a list.
"""


example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
print(example_list)

#Using Remove
example_list.remove(5)
print(example_list)

"""
Growing a List: Append
We can add a single element to a list using the .append() Python method.

Suppose we have an empty list called garden:

garden = []
We can add the element "Tomatoes" by using the .append() method:

garden.append("Tomatoes")
 
print(garden)
Will output:

['Tomatoes']
We see that garden now contains "Tomatoes"!

When we use .append() on a list that already has elements, our new element is added to the end of the list:

# Create a list
garden = ["Tomatoes", "Grapes", "Cauliflower"]
 
# Append a new element
garden.append("Green Beans")
print(garden)
Will output:

['Tomatoes', 'Grapes', 'Cauliflower', 'Green Beans']
Let’s use the .append() method to manipulate a list.
"""

orders = ["daisies", "periwinkle"]
print(orders)

orders.append("tulips")
print(orders)

orders.append("roses")
print(orders)

print(orders)


# example 2
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:

new_orders = ["lilac", "iris"]
print(new_orders)

orders_combined = orders + new_orders
print(orders_combined)

broken_prices = [5, 3, 4, 5, 4] + 4
"TypeError: can only concatenate list (not 'int') to list"
