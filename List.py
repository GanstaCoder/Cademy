"""
List Methods
As we start exploring lists further in the next exercises, we will encounter the concept of a method.

In Python, for any specific data-type ( strings, booleans, lists, etc. ) there is built-in functionality that we can use to create, manipulate, and even delete our data. We call this built-in functionality a method.

For lists, methods will follow the form of list_name.method(). Some methods will require an input value that will go between the parenthesis of the method ( ).

An example of a popular list method is .append(), which allows us to add an element to the end of a list.
"""

example_list = [1, 2, 3, 4]

# Using Append
example_list.append(5)
print(example_list)

# Using Remove
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

"""
Accessing List Elements
We are interviewing candidates for a job. We will call each candidate in order, represented by a Python list:

calls = ["Juan", "Zofia", "Amare", "Ezio", "Ananya"]
First, we’ll call "Juan", then "Zofia", etc.

In Python, we call the location of an element in a list its index.

Python lists are zero-indexed. This means that the first element in a list has index 0, rather than 1.

Here are the index numbers for the list calls:

Element	Index
"Juan"	0
"Zofia"	1
"Amare"	2
"Ezio"	3
"Ananya"	4

In this example, the element with index 2 is "Amare".

We can select a single element from a list by using square brackets ([]) and the index of the list item. If we wanted to select the third element from the list, we’d use calls[2]:

print(calls[2])
Will output:

Amare
Note: When accessing elements of a list, you must use an int as the index. If you use a float, you will get an error. This can be especially tricky when using division. For example print(calls[4/2]) will result in an error, because 4/2 gets evaluated to the float 2.0.

To solve this problem, you can force the result of your division to be an int by using the int() function. int() takes a number and cuts off the decimal point. For example, int(5.9) and int(5.0) will both become 5. Therefore, calls[int(4/2)] will result in the same value as calls[2], whereas calls[4/2] will result in an error.

Instructions
1.
Use square brackets ([ and ]) to select the 4th employee from the list employees. Save it to the variable employee_four.

Checkpoint 2 Passed

2.
Paste the following code into script.py:

print(employees[8])
What happens? Why?

Checkpoint 3 Passed

3.
Selecting an element that does not exist produces an IndexError.

In the line of code that you pasted, change 8 to an index that exists so that you don’t get an IndexError.

Run your code again!
"""

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]
print(employees[4])
print(employees[6])

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1]
print(shopping_list[-1])

index5_element = shopping_list[5]
print(shopping_list[5])

# Your code below:
order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)

order_list.remove("Flatbread")
print(order_list)

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)

new_store_order_list.remove("Mango")
print(new_store_order_list)

# Broken
new_store_order_list.remove("Onions")
print(new_store_order_list)

# Your code below:
class_name_test = [["Jenny", 90],
                   ["Alexus", 85.5],
                   ["Sam", 83],
                   ["Ellie", 101.5]
                   ]
print(class_name_test)
sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)

# TEST
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below:
subjects = [
    "physics",
    "calculus",
    "poetry",
    "history"
]

grades = [
    98,
    97,
    85,
    88
]

gradebook = [
    ["physics", 98],
    ["calculus", 97],
    ["poetry", 85],
    ["history", 88]
]

# print(gradebook)

gradebook.append(["computer science", 100])
# print(gradebook)
gradebook.append(["visual arts", 93])
# print(gradebook)
gradebook[-1][-1] = 98
# print(gradebook)
gradebook.remove(["poetry", 85])
# print(gradebook)

gradebook.append(["poetry", "Pass"])
# print(gradebook)

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)


inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]


inventory_len = len(inventory)

first = inventory[0]
#print(first)
last = inventory[-1]
#print(last)
inventory_2_6 = inventory[2:6]
#print(inventory_2_6)
first_3 = inventory[0:3]
#print(first_3)
twin_beds = inventory.count('twin bed')
#print(twin_beds)
removed_item = inventory.pop(4)
#print(removed_item)
inventory.insert(10, "19th Century Bed Frame")
#print(inventory)
inventory.sort()
#print(inventory)
inventory = sorted(inventory)
#print(inventory)