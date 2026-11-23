# 1. Python Examples: Recursion, Dynamic Arrays, and Linked Lists
# A. Recursion Example
# Recursion is when a function calls itself to solve a smaller part of a problem until it hits a stopping point (called the base case). Without a stopping point, the function would just keep calling itself forever and crash.

# Here is a simple countdown and a sum-of-numbers example:
# Simple Recursion Example:

# Example 1: Counting down to 1
def countdown(number):
    # Stopping point (Base Case): stop when we reach 0
    if number == 0:
        print("Done!")
        return
    
    print(number)
    # The function calls itself with a smaller number
    countdown(number - 1)


# Example 2: Adding numbers from 1 up to n (e.g., 1 + 2 + 3 + 4 = 10)
def add_numbers(n):
    # Stopping point: if n is 1, just return 1
    if n == 1:
        return 1
    
    # Otherwise, add n to the result of add_numbers(n - 1)
    return n + add_numbers(n - 1)


# --- Testing the functions ---
print("--- Countdown ---")
countdown(5)

print("\n--- Adding Numbers ---")
total = add_numbers(4)
print("Sum from 1 to 4 is:", total)

# B. Dynamic Arrays Example
# Normally, in some programming languages, an array has a fixed size—if you make space for 3 items, you can't add a 4th one. A Dynamic Array solves this by growing automatically when it gets full.

# In Python, a normal list is already a dynamic array! We can add as many items as we want using .append() without worrying about the size:
# Dynamic Array Example:

# Start with an empty list (dynamic array)
my_list = []

print("Starting length:", len(my_list))

# Adding items one by one - the array grows automatically!
my_list.append("Apple")
my_list.append("Banana")
my_list.append("Orange")
print("After adding 3 items:", my_list, "| Length:", len(my_list))

# We can keep adding more without setting a size limit first
my_list.append("Mango")
my_list.append("Pineapple")
print("After adding 2 more items:", my_list, "| Length:", len(my_list))

# Removing an item also resizes it automatically
my_list.remove("Banana")
print("After removing Banana:", my_list, "| Length:", len(my_list))

# C. Linked List Example
# A Linked List is like a treasure hunt or a train where each coach is connected to the next one. Instead of storing all items together in one block like an array, each item is kept in a Node that holds:

# 1. The data (the value).
# 2. A next link pointing to the next node.

# Simple Linked List Example:

# Blueprint for a single Node (one coach of the train)
class Node:
    def __init__(self, data):
        self.data = data   # The value we want to store
        self.next = None   # Points to the next node (empty at first)


# Creating 3 separate nodes
node1 = Node("First")
node2 = Node("Second")
node3 = Node("Third")

# Linking the nodes together
node1.next = node2   # First points to Second
node2.next = node3   # Second points to Third

# Walking through the linked list starting from the first node (head)
print("--- Printing the Linked List ---")
current = node1
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")

